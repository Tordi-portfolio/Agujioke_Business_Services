from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from core.models import Service

from .models import ServiceRequest

User = get_user_model()


class AuthAndDashboardTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_services", verbosity=0)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_registration_logs_user_in_and_creates_profile(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "tester",
                "first_name": "Test",
                "last_name": "User",
                "email": "tester@example.com",
                "password1": "S3cure-Passw0rd!x",
                "password2": "S3cure-Passw0rd!x",
            },
        )
        self.assertRedirects(response, reverse("dashboard"))
        user = User.objects.get(username="tester")
        self.assertTrue(hasattr(user, "profile"))

    def test_user_can_submit_and_view_own_request_only(self):
        owner = User.objects.create_user("owner", "o@example.com", "pass12345!")
        other = User.objects.create_user("other", "x@example.com", "pass12345!")
        service = Service.objects.first()

        self.client.login(username="owner", password="pass12345!")
        response = self.client.post(
            reverse("request_new"),
            {
                "service": service.pk,
                "title": "Need help",
                "details": "Details here",
                "urgency": "normal",
            },
        )
        req = ServiceRequest.objects.get(user=owner)
        self.assertRedirects(response, req.get_absolute_url())

        self.client.logout()
        self.client.login(username="other", password="pass12345!")
        self.assertEqual(self.client.get(req.get_absolute_url()).status_code, 404)
        self.assertEqual(other.service_requests.count(), 0)


class StaffPanelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_services", verbosity=0)
        cls.staff = User.objects.create_user(
            "boss", "boss@example.com", "pass12345!", is_staff=True
        )
        cls.client_user = User.objects.create_user(
            "client", "client@example.com", "pass12345!", first_name="Ada"
        )
        cls.req = ServiceRequest.objects.create(
            user=cls.client_user,
            service=Service.objects.first(),
            title="Import 2 containers",
            details="Details",
        )

    def test_anonymous_is_redirected_to_login(self):
        for name in ["staff_dashboard", "staff_request_list", "staff_inquiry_list"]:
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 302, name)
            self.assertIn(reverse("login"), response.url)

    def test_normal_client_is_forbidden(self):
        self.client.login(username="client", password="pass12345!")
        for url in [
            reverse("staff_dashboard"),
            reverse("staff_request_list"),
            reverse("staff_request_detail", args=[self.req.pk]),
        ]:
            self.assertEqual(self.client.get(url).status_code, 403, url)

    def test_staff_sees_all_requests(self):
        self.client.login(username="boss", password="pass12345!")
        self.assertContains(self.client.get(reverse("staff_dashboard")), "Review panel")
        response = self.client.get(reverse("staff_request_list"))
        self.assertContains(response, "Import 2 containers")

    def test_staff_can_accept_request(self):
        self.client.login(username="boss", password="pass12345!")
        response = self.client.post(
            reverse("staff_request_detail", args=[self.req.pk]),
            {"quick": "accepted", "status": "pending", "admin_note": "We will call you."},
        )
        self.assertEqual(response.status_code, 302)
        self.req.refresh_from_db()
        self.assertEqual(self.req.status, "accepted")
        self.assertEqual(self.req.decided_by, self.staff)
        self.assertIsNotNone(self.req.decided_at)

    def test_rejection_requires_a_reason(self):
        self.client.login(username="boss", password="pass12345!")
        response = self.client.post(
            reverse("staff_request_detail", args=[self.req.pk]),
            {"quick": "rejected", "status": "pending", "admin_note": ""},
        )
        self.assertEqual(response.status_code, 200)  # form re-rendered with error
        self.req.refresh_from_db()
        self.assertEqual(self.req.status, "pending")

    def test_client_sees_decision_on_own_dashboard(self):
        self.req.status = "rejected"
        self.req.admin_note = "Outside our scope."
        self.req.save()
        self.client.login(username="client", password="pass12345!")
        response = self.client.get(self.req.get_absolute_url())
        self.assertContains(response, "Outside our scope.")

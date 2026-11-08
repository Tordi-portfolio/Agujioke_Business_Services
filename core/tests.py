from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from .models import Inquiry, Service


class PublicSiteTests(TestCase):
    """Every public page must work for anonymous visitors (no login needed)."""

    @classmethod
    def setUpTestData(cls):
        call_command("seed_services", verbosity=0)

    def test_services_are_seeded(self):
        self.assertEqual(Service.objects.count(), 11)

    def test_public_pages_load_without_login(self):
        for name in ["home", "about", "service_list", "faq", "contact"]:
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200, name)

    def test_every_service_detail_page_loads(self):
        for service in Service.objects.all():
            response = self.client.get(service.get_absolute_url())
            self.assertEqual(response.status_code, 200, service.slug)
            self.assertContains(response, service.title)

    def test_contact_form_saves_inquiry(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Jane Doe",
                "email": "jane@example.com",
                "subject": "Hello",
                "message": "I would like to import goods.",
            },
        )
        self.assertRedirects(response, reverse("contact"))
        self.assertEqual(Inquiry.objects.count(), 1)

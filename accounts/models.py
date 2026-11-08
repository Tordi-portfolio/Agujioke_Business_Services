from django.conf import settings
from django.db import models
from django.urls import reverse

from core.models import Service


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    phone = models.CharField(max_length=40, blank=True)
    company = models.CharField("Company / organisation", max_length=150, blank=True)
    country = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bio = models.TextField("About you / your business", blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    @property
    def completeness(self):
        """Percentage of optional profile fields that are filled in."""
        fields = [
            self.user.first_name,
            self.user.last_name,
            self.user.email,
            self.phone,
            self.company,
            self.country,
            self.address,
            self.bio,
        ]
        filled = sum(1 for f in fields if f)
        return int(filled / len(fields) * 100)


class ServiceRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        IN_REVIEW = "in_review", "In review"
        ACCEPTED = "accepted", "Accepted"
        IN_PROGRESS = "in_progress", "In progress"
        COMPLETED = "completed", "Completed"
        REJECTED = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"

    class Urgency(models.TextChoices):
        NORMAL = "normal", "Normal"
        SOON = "soon", "Within 2 weeks"
        URGENT = "urgent", "Urgent"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="service_requests",
    )
    service = models.ForeignKey(
        Service, on_delete=models.PROTECT, related_name="requests"
    )
    title = models.CharField(max_length=200, help_text="A short summary of what you need.")
    details = models.TextField(
        help_text="Describe what you need, quantities, destinations, timelines, etc."
    )
    urgency = models.CharField(
        max_length=10, choices=Urgency.choices, default=Urgency.NORMAL
    )
    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.PENDING
    )
    admin_note = models.TextField(
        "Note to client",
        blank=True,
        help_text="Visible to the client on their dashboard (e.g. the reason for a rejection).",
    )
    decided_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="decisions",
    )
    decided_at = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.reference} – {self.title}"

    @property
    def reference(self):
        return f"REQ-{self.pk:05d}" if self.pk else "REQ-NEW"

    def get_absolute_url(self):
        return reverse("request_detail", args=[self.pk])

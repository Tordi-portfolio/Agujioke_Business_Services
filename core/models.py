from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Service(models.Model):
    """One of the business lines offered on the website."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    icon = models.CharField(
        max_length=8, blank=True, help_text="A single emoji used as the card icon."
    )
    tagline = models.CharField(max_length=200)
    summary = models.TextField(help_text="Short text shown on cards and lists.")
    overview = models.TextField(
        help_text="Long description. Separate paragraphs with a blank line."
    )
    offerings = models.TextField(
        help_text="What we offer. One item per line."
    )
    process = models.TextField(
        help_text="How it works. One step per line in the form: Title|Description"
    )
    audience = models.TextField(
        help_text="Who this service is for. One item per line."
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("service_detail", args=[self.slug])

    # ---- helpers used by the templates --------------------------------
    @property
    def overview_paragraphs(self):
        return [p.strip() for p in self.overview.split("\n\n") if p.strip()]

    @property
    def offerings_list(self):
        return [line.strip() for line in self.offerings.splitlines() if line.strip()]

    @property
    def audience_list(self):
        return [line.strip() for line in self.audience.splitlines() if line.strip()]

    @property
    def process_steps(self):
        steps = []
        for line in self.process.splitlines():
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                title, text = line.split("|", 1)
            else:
                title, text = line, ""
            steps.append({"title": title.strip(), "text": text.strip()})
        return steps


class FAQ(models.Model):
    """Frequently asked question. Leave `service` empty for site-wide FAQs."""

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="faqs",
        null=True,
        blank=True,
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class Inquiry(models.Model):
    """A message sent through the public contact form."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inquiries",
    )
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True
    )
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "inquiries"

    def __str__(self):
        return f"{self.subject} – {self.name}"

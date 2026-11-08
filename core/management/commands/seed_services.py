from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import FAQ, Service
from core.seed_data_part1 import SERVICES_PART1
from core.seed_data_part2 import GENERAL_FAQS, SERVICES_PART2


class Command(BaseCommand):
    help = "Loads (or refreshes) the default services and FAQs shown on the website."

    @transaction.atomic
    def handle(self, *args, **options):
        services = SERVICES_PART1 + SERVICES_PART2
        for data in services:
            data = dict(data)
            faqs = data.pop("faqs", [])
            slug = data.pop("slug")
            service, created = Service.objects.update_or_create(
                slug=slug, defaults=data
            )
            service.faqs.all().delete()
            for order, (question, answer) in enumerate(faqs, start=1):
                FAQ.objects.create(
                    service=service, question=question, answer=answer, order=order
                )
            self.stdout.write(
                f"{'Created' if created else 'Updated'}: {service.title}"
            )

        FAQ.objects.filter(service__isnull=True).delete()
        for order, (question, answer) in enumerate(GENERAL_FAQS, start=1):
            FAQ.objects.create(question=question, answer=answer, order=order)

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. {len(services)} services and {len(GENERAL_FAQS)} general FAQs loaded."
            )
        )

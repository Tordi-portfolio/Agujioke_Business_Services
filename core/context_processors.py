from django.conf import settings

from .models import Service


def site(request):
    """Makes site details and the services list available to every template."""
    return {
        "SITE": settings.SITE_CONFIG,
        "nav_services": Service.objects.filter(is_active=True),
    }

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "SB MUCH REX GLOBAL ENTERPRISES – Admin"
admin.site.site_title = "SB Much Rex Admin"
admin.site.index_title = "Manage the website"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("staff/", include("accounts.staff_urls")),
    path("", include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

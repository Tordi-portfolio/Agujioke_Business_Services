from django.contrib import admin

from .models import Profile, ServiceRequest


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "country", "phone")
    search_fields = ("user__username", "user__email", "company", "country")


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("reference", "title", "user", "service", "urgency", "status", "created")
    list_filter = ("status", "urgency", "service")
    list_editable = ("status",)
    search_fields = ("title", "details", "user__username", "user__email")
    readonly_fields = ("created", "updated", "decided_by", "decided_at")
    fieldsets = (
        (None, {"fields": ("user", "service", "title", "details", "urgency")}),
        ("Handling", {"fields": ("status", "admin_note", "decided_by", "decided_at")}),
        ("Timestamps", {"fields": ("created", "updated")}),
    )

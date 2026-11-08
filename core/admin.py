from django.contrib import admin

from .models import FAQ, Inquiry, Service


class FAQInline(admin.StackedInline):
    model = FAQ
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary")
    inlines = [FAQInline]


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "service", "order", "is_active")
    list_filter = ("service", "is_active")
    search_fields = ("question", "answer")


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "service", "created", "is_handled")
    list_filter = ("is_handled", "service", "created")
    list_editable = ("is_handled",)
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created",)

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import InquiryForm
from .models import FAQ, Service


def home(request):
    faqs = FAQ.objects.filter(service__isnull=True, is_active=True)[:6]
    return render(request, "core/home.html", {"faqs": faqs})


def about(request):
    return render(request, "core/about.html")


def service_list(request):
    return render(request, "core/service_list.html")


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    others = Service.objects.filter(is_active=True).exclude(pk=service.pk)
    return render(
        request,
        "core/service_detail.html",
        {
            "service": service,
            "faqs": service.faqs.filter(is_active=True),
            "others": others,
        },
    )


def faq(request):
    general = FAQ.objects.filter(service__isnull=True, is_active=True)
    services = Service.objects.filter(is_active=True).prefetch_related("faqs")
    return render(request, "core/faq.html", {"general": general, "services": services})


def contact(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            if request.user.is_authenticated:
                inquiry.user = request.user
            inquiry.save()
            messages.success(
                request,
                "Thank you! Your message has been received and we will get back to you shortly.",
            )
            return redirect("contact")
    else:
        initial = {}
        if request.user.is_authenticated:
            initial["name"] = request.user.get_full_name() or request.user.username
            initial["email"] = request.user.email
        slug = request.GET.get("service")
        if slug:
            svc = Service.objects.filter(slug=slug).first()
            if svc:
                initial["service"] = svc.pk
                initial["subject"] = f"Enquiry about {svc.title}"
        form = InquiryForm(initial=initial)
    return render(request, "core/contact.html", {"form": form})

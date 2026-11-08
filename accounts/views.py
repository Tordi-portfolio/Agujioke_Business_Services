from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from core.models import Inquiry, Service

from .forms import ProfileForm, RegisterForm, ServiceRequestForm, UserForm
from .models import Profile, ServiceRequest


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, f"Welcome, {user.first_name}! Your account has been created."
            )
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    requests_qs = request.user.service_requests.select_related("service")
    stats = {
        "total": requests_qs.count(),
        "pending": requests_qs.filter(
            status__in=[ServiceRequest.Status.PENDING, ServiceRequest.Status.IN_REVIEW]
        ).count(),
        "active": requests_qs.filter(
            status__in=[ServiceRequest.Status.ACCEPTED, ServiceRequest.Status.IN_PROGRESS]
        ).count(),
        "completed": requests_qs.filter(status=ServiceRequest.Status.COMPLETED).count(),
    }
    context = {
        "profile": profile,
        "recent_requests": requests_qs[:8],
        "stats": stats,
        "inquiries": Inquiry.objects.filter(user=request.user)[:5],
    }
    return render(request, "accounts/dashboard.html", context)


@login_required
def request_list(request):
    status = request.GET.get("status", "")
    qs = request.user.service_requests.select_related("service")
    if status in dict(ServiceRequest.Status.choices):
        qs = qs.filter(status=status)
    return render(
        request,
        "accounts/request_list.html",
        {
            "requests": qs,
            "status": status,
            "statuses": ServiceRequest.Status.choices,
        },
    )


@login_required
def request_new(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(
                request, f"Request {obj.reference} submitted. We will review it shortly."
            )
            return redirect(obj)
    else:
        initial = {}
        slug = request.GET.get("service")
        if slug:
            svc = Service.objects.filter(slug=slug, is_active=True).first()
            if svc:
                initial["service"] = svc.pk
                initial["title"] = f"{svc.title} request"
        form = ServiceRequestForm(initial=initial)
    return render(request, "accounts/request_form.html", {"form": form})


@login_required
def request_detail(request, pk):
    obj = get_object_or_404(ServiceRequest, pk=pk, user=request.user)
    return render(request, "accounts/request_detail.html", {"req": obj})


@login_required
@require_POST
def request_cancel(request, pk):
    obj = get_object_or_404(ServiceRequest, pk=pk, user=request.user)
    if obj.status in (ServiceRequest.Status.PENDING, ServiceRequest.Status.IN_REVIEW):
        obj.status = ServiceRequest.Status.CANCELLED
        obj.save(update_fields=["status", "updated"])
        messages.info(request, f"Request {obj.reference} was cancelled.")
    else:
        messages.error(request, "Only pending requests can be cancelled.")
    return redirect(obj)


@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("dashboard")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(
        request,
        "accounts/profile_form.html",
        {"user_form": user_form, "profile_form": profile_form},
    )

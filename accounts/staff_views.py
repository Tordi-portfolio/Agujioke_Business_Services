"""Staff-only review panel.

Only logged-in users with `is_staff=True` can open these pages:
  * anonymous visitors are sent to the login page
  * logged-in clients (not staff) get a 403 "Access denied" page
"""
from functools import wraps

from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from core.models import Inquiry, Service

from .forms import StaffDecisionForm
from .models import ServiceRequest

Status = ServiceRequest.Status


def staff_required(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        if not request.user.is_staff:
            raise PermissionDenied
        return view(request, *args, **kwargs)

    return wrapper


def _notify_client(request, req):
    """Email the client about a decision/update (console backend in development)."""
    if not req.user.email:
        return
    lines = [
        f"Hello {req.user.first_name or req.user.username},",
        "",
        f"There is an update on your request {req.reference} ({req.title}).",
        f"Status: {req.get_status_display()}",
    ]
    if req.admin_note:
        lines += ["", "Note from our team:", req.admin_note]
    lines += ["", "View it on your dashboard:", request.build_absolute_uri(req.get_absolute_url())]
    send_mail(
        subject=f"Update on your request {req.reference}",
        message="\n".join(lines),
        from_email=None,  # uses DEFAULT_FROM_EMAIL
        recipient_list=[req.user.email],
        fail_silently=True,
    )


@staff_required
def dashboard(request):
    qs = ServiceRequest.objects.all()
    counts = {value: qs.filter(status=value).count() for value, _ in Status.choices}
    needs_review = qs.filter(status__in=[Status.PENDING, Status.IN_REVIEW]).select_related(
        "user", "service"
    )
    context = {
        "counts": counts,
        "total": qs.count(),
        "needs_review": needs_review[:10],
        "needs_review_total": needs_review.count(),
        "new_inquiries": Inquiry.objects.filter(is_handled=False)[:5],
        "new_inquiries_total": Inquiry.objects.filter(is_handled=False).count(),
    }
    return render(request, "staff/dashboard.html", context)


@staff_required
def request_list(request):
    qs = ServiceRequest.objects.select_related("user", "service", "user__profile")

    status = request.GET.get("status", "")
    service_slug = request.GET.get("service", "")
    q = request.GET.get("q", "").strip()

    if status in dict(Status.choices):
        qs = qs.filter(status=status)
    if service_slug:
        qs = qs.filter(service__slug=service_slug)
    if q:
        qs = qs.filter(
            Q(title__icontains=q)
            | Q(details__icontains=q)
            | Q(user__username__icontains=q)
            | Q(user__email__icontains=q)
            | Q(user__first_name__icontains=q)
            | Q(user__last_name__icontains=q)
            | Q(user__profile__company__icontains=q)
        )

    page = Paginator(qs, 20).get_page(request.GET.get("page"))
    params = request.GET.copy()
    params.pop("page", None)

    return render(
        request,
        "staff/request_list.html",
        {
            "page": page,
            "statuses": Status.choices,
            "services": Service.objects.all(),
            "status": status,
            "service_slug": service_slug,
            "q": q,
            "querystring": params.urlencode(),
        },
    )


@staff_required
def request_detail(request, pk):
    obj = get_object_or_404(
        ServiceRequest.objects.select_related("user", "user__profile", "service", "decided_by"),
        pk=pk,
    )
    old_status, old_note = obj.status, obj.admin_note

    if request.method == "POST":
        data = request.POST.copy()
        quick = data.get("quick")
        if quick in (Status.ACCEPTED, Status.REJECTED):
            data["status"] = quick
        form = StaffDecisionForm(data, instance=obj)
        if form.is_valid():
            updated = form.save(commit=False)
            if updated.status != old_status and updated.status in (
                Status.ACCEPTED,
                Status.REJECTED,
            ):
                updated.decided_by = request.user
                updated.decided_at = timezone.now()
            updated.save()
            if updated.status != old_status or updated.admin_note != old_note:
                _notify_client(request, updated)
            messages.success(
                request,
                f"{updated.reference} updated: {updated.get_status_display()}. The client can see this on their dashboard.",
            )
            return redirect("staff_request_detail", pk=updated.pk)
    else:
        form = StaffDecisionForm(instance=obj)

    return render(
        request,
        "staff/request_detail.html",
        {"req": obj, "form": form, "client": obj.user, "profile": getattr(obj.user, "profile", None)},
    )


@staff_required
def inquiry_list(request):
    show = request.GET.get("show", "new")
    qs = Inquiry.objects.select_related("service", "user")
    if show == "new":
        qs = qs.filter(is_handled=False)
    elif show == "handled":
        qs = qs.filter(is_handled=True)
    page = Paginator(qs, 20).get_page(request.GET.get("page"))
    return render(request, "staff/inquiry_list.html", {"page": page, "show": show})


@staff_required
@require_POST
def inquiry_toggle(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    inquiry.is_handled = not inquiry.is_handled
    inquiry.save(update_fields=["is_handled"])
    messages.success(
        request,
        "Marked as handled." if inquiry.is_handled else "Moved back to new enquiries.",
    )
    return redirect(request.POST.get("next") or "staff_inquiry_list")

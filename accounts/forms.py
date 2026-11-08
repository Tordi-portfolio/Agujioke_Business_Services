from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)

from core.forms import StyledFormMixin
from core.models import Service

from .models import Profile, ServiceRequest

User = get_user_model()


class StyledAuthenticationForm(StyledFormMixin, AuthenticationForm):
    pass


class StyledPasswordChangeForm(StyledFormMixin, PasswordChangeForm):
    pass


class RegisterForm(StyledFormMixin, UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email


class UserForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        qs = User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Another account already uses this email.")
        return email


class ProfileForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("phone", "company", "country", "address", "bio")
        widgets = {"bio": forms.Textarea(attrs={"rows": 4})}


class ServiceRequestForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ("service", "title", "details", "urgency")
        widgets = {"details": forms.Textarea(attrs={"rows": 7})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].queryset = Service.objects.filter(is_active=True)
        self.fields["service"].empty_label = "Choose a service…"


class StaffDecisionForm(StyledFormMixin, forms.ModelForm):
    """Used only on the staff panel to accept / reject / update a request."""

    class Meta:
        model = ServiceRequest
        fields = ("status", "admin_note")
        widgets = {"admin_note": forms.Textarea(attrs={"rows": 5})}

    def clean(self):
        cleaned = super().clean()
        status = cleaned.get("status")
        note = (cleaned.get("admin_note") or "").strip()
        if status == ServiceRequest.Status.REJECTED and not note:
            self.add_error(
                "admin_note", "Please give the client a short reason for the rejection."
            )
        return cleaned

from django import forms

from .models import Inquiry, Service


class StyledFormMixin:
    """Adds the `form-control` CSS class to every widget (used site-wide)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, (forms.CheckboxInput, forms.RadioSelect)):
                continue
            existing = widget.attrs.get("class", "")
            widget.attrs["class"] = f"{existing} form-control".strip()


class InquiryForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["name", "email", "phone", "service", "subject", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 6}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].queryset = Service.objects.filter(is_active=True)
        self.fields["service"].required = False
        self.fields["service"].empty_label = "General enquiry"
        self.fields["phone"].required = False

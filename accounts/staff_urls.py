from django.urls import path

from . import staff_views as v

urlpatterns = [
    path("", v.dashboard, name="staff_dashboard"),
    path("requests/", v.request_list, name="staff_request_list"),
    path("requests/<int:pk>/", v.request_detail, name="staff_request_detail"),
    path("enquiries/", v.inquiry_list, name="staff_inquiry_list"),
    path("enquiries/<int:pk>/toggle/", v.inquiry_toggle, name="staff_inquiry_toggle"),
]

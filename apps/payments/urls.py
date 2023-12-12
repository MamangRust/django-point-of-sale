from django.urls import path
from .views import (
    PaymentListView,
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
)

urlpatterns = [
    path("", PaymentListView.as_view(), name="payment-list"),
    path("create/", PaymentCreateView.as_view(), name="payment-create"),
    path("update/<int:pk>", PaymentUpdateView.as_view(), name="payment-update"),
    path("delete/<int:pk>", PaymentDeleteView.as_view(), name="payment-delete"),
]

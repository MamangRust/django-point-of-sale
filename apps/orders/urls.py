from django.urls import path
from .views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView


urlpatterns = [
    path("", OrderListView.as_view(), name="order-list"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("update/<int:pk>", OrderUpdateView.as_view(), name="order-update"),
    path("delete/<int:pk>", OrderDeleteView.as_view(), name="order-delete"),
]

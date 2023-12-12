from django.urls import path
from .views import (
    user_cart_list,
    user_cart_delete,
    user_cart_create,
    user_cart_update,
    update_quantity,
    removeAllCart,
)


urlpatterns = [
    path("", user_cart_list, name="user-cart-list"),
    path("create/", user_cart_create, name="user-cart-create"),
    path("update/<int:pk>/", user_cart_update, name="user-cart-update"),
    path("update-quantity/<int:id>/", update_quantity, name="user-cart-quantity"),
    path("delete/<int:pk>/", user_cart_delete, name="user-cart-delete"),
    path("remove-all-cart/", removeAllCart, name="user-remove-cart"),
]

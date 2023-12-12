"""
URL configuration for django_point_of_sale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path("auth/", include("apps.auth.urls")),
    path("user/", include("apps.user.urls")),
    path("product/", include("apps.product.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("", include("apps.home.urls")),
    path("order/", include("apps.orders.urls")),
    path("payment/", include("apps.payments.urls")),
    path("cart/", include("apps.user_cart.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render
from apps.product.models import Product
from django.contrib.auth.decorators import login_required
from apps.user_cart.models import UserCart


# Create your views here.
@login_required(login_url="/auth/login/")
def home(request):
    products = Product.objects.all()
    user_cart = UserCart.objects.all()

    return render(
        request=request,
        template_name="index.html",
        context={"products": products, "user_cart": user_cart},
    )

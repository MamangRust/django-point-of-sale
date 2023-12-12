from django.shortcuts import get_object_or_404
from .models import UserCart
from .forms import UserCartForm
from django.http import JsonResponse
from apps.user.models import User
from django.contrib.auth.decorators import login_required
from apps.product.models import Product


@login_required(login_url="/auth/login")
def user_cart_list(request):
    user_carts = UserCart.objects.all()
    user_carts_data = []

    for user_cart in user_carts:
        user_data = {
            "id": user_cart.user.id,
            "name": user_cart.user.name,
            "email": user_cart.user.email,
            "phone": user_cart.user.phone,
            "birthday": str(user_cart.user.birthday),
            "gender": user_cart.user.gender,
            "image": user_cart.user.image.url if user_cart.user.image else None,
        }
        product_data = {
            "id": user_cart.product.id,
            "name": user_cart.product.name,
            "description": user_cart.product.description,
            "price": str(user_cart.product.price),
            "image": user_cart.product.image.url if user_cart.product.image else None,
            "quantity": user_cart.product.quantity,
        }
        user_cart_data = {
            "id": user_cart.id,
            "user": user_data,
            "product": product_data,
            "quantity": user_cart.quantity,
        }
        user_carts_data.append(user_cart_data)

    return JsonResponse(user_carts_data, safe=False)


@login_required(login_url="/auth/login")
def user_cart_create(request):
    if request.method == "POST":
        form = UserCartForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("user")
            product_id = form.cleaned_data.get("product")
            quantity = form.cleaned_data.get("quantity")

            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)

            UserCart.objects.create(user=user, product=product, quantity=quantity)

            return JsonResponse({"message": "User cart created successfully"})
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        return JsonResponse({"error": "Invalid Request"}, status=400)


@login_required(login_url="/auth/login")
def update_quantity(request, id):
    if request.method == "POST":
        try:
            cart_item = UserCart.objects.get(id=id)
            new_quantity = request.POST.get("quantity")
            cart_item.quantity = new_quantity
            cart_item.save()
            return JsonResponse({"message": "Quantity updated successfully"})
        except UserCart.DoesNotExist:
            return JsonResponse({"error": "UserCart does not exist"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@login_required(login_url="/auth/login")
def user_cart_update(request, pk):
    user_cart = get_object_or_404(UserCart, pk=pk)
    if request.method == "POST":
        form = UserCartForm(request.POST)
        if form.is_valid():
            user_cart.user = form.cleaned_data.get("user")
            user_cart.product = form.cleaned_data.get("product")
            user_cart.quantity = form.cleaned_data.get("quantity")
            user_cart.save()

            return JsonResponse({"message": "User cart updated successfully"})
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        return JsonResponse({"error": "Invalid Request"}, status=400)


@login_required(login_url="/auth/login")
def user_cart_delete(request, pk):
    user_cart = get_object_or_404(UserCart, pk=pk)
    if request.method == "POST":
        user_cart.delete()
        return JsonResponse({"message": "User cart deleted successfully"})
    else:
        return JsonResponse({"error": "Invalid Request"}, status=400)


@login_required(login_url="/auth/login")
def removeAllCart(request):
    try:
        if request.method == "POST":
            user_carts = UserCart.objects.filter(user_id=request.user.id)
            user_carts.delete()
            return JsonResponse({"message": "All user carts removed successfully"})
        else:
            return JsonResponse({"error": "Invalid method"}, status=405)
    except UserCart.DoesNotExist:
        return JsonResponse({"error": "No carts found for this user"}, status=404)

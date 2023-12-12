from django.shortcuts import render, get_object_or_404
from django.views import View
from apps.product.models import Product
from apps.orders.models import Order, OrderItem
from apps.user.models import User
from decimal import Decimal
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.payments.models import Payment
from django.http import JsonResponse
from .forms import OrderCreateForm


# Create your views here.
class OrderListView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def get(self, request):
        order = Order.objects.all()

        return render(
            request=request,
            template_name="admin/order/index.html",
            context={"orders": order},
        )


class OrderCreateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def post(self, request):
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("user_id")
            product_id = form.cleaned_data.get("product_id")
            payment_id = form.cleaned_data.get("payment_id")
            price = form.cleaned_data.get("price")
            quantity = form.cleaned_data.get("quantity")

            try:
                user = get_object_or_404(User, id=user_id)
                product = get_object_or_404(Product, id=product_id)
                payment = get_object_or_404(Payment, id=payment_id)

                if product.quantity < quantity:
                    return JsonResponse(
                        {"error": "Not enough stock available"}, status=400
                    )

                order = Order.objects.create(user=user, payment=payment)
                order_item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=Decimal(price),
                    quantity=quantity,
                )

                product.quantity -= quantity
                product.save()

                return JsonResponse({"message": "Order created successfully"})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        else:
            errors = form.errors.as_json()

            return JsonResponse({"error": errors}, status=400)


class OrderUpdateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def post(self, request, pk):
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("user_id")
            product_id = form.cleaned_data.get("product_id")
            price = form.cleaned_data.get("price")
            quantity = form.cleaned_data.get("quantity")

            try:
                user = get_object_or_404(User, id=user_id)
                product = get_object_or_404(Product, id=product_id)

                order = get_object_or_404(Order, id=pk)
                order_items = OrderItem.objects.filter(order=order)

                for item in order_items:
                    product = item.product
                    product.quantity += item.quantity
                    product.save()

                if product.quantity < quantity:
                    return JsonResponse(
                        {"error": "Not enough stock available"}, status=400
                    )

                order.user = user
                order.save()

                order_items.delete()

                order_item = OrderItem.objects.create(
                    order=order, product=product, price=price, quantity=quantity
                )

                product.quantity -= quantity
                product.save()

                return JsonResponse({"message": "Order updated successfully"})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"error": errors}, status=400)


class OrderDeleteView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def delete(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        try:
            order.delete()
            return JsonResponse({"message": "Order deleted successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

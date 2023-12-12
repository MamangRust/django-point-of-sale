from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse
from apps.payments.models import Payment
from apps.orders.models import Order
from apps.product.models import Product
from django.db.models import Sum, Count
import json
from datetime import datetime


class DashboardView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def get(self, request):
        try:
            total_revenue = Payment.objects.aggregate(total_revenue=Sum("amount"))[
                "total_revenue"
            ]
            payment = Payment.objects.count()
            order = Order.objects.count()
            product = Product.objects.count()

            top_payment_methods = (
                Payment.objects.values("paymentMethod")
                .annotate(count=Count("paymentMethod"))
                .order_by("-count")[:5]
            )
            payment_methods_usage = {
                method["paymentMethod"]: method["count"]
                for method in top_payment_methods
            }

            yearly_revenue = self.calculate_yearly_revenue()

            response_data = {
                "total_revenue": total_revenue,
                "payment_methods_usage": json.dumps(payment_methods_usage),
                "yearly_revenue": yearly_revenue,
                "order": order,
                "payment": payment,
                "product": product,
            }

            return render(
                request=request,
                template_name="admin/dashboard.html",
                context=response_data,
            )

        except Exception as err:
            return JsonResponse({"error": str(err)}, status=400)

    def calculate_yearly_revenue(self):
        yearly_revenue = []
        current_year = datetime.now().year
        for month in range(1, 13):
            total_revenue = (
                Payment.objects.filter(
                    created_at__year=current_year, created_at__month=month
                ).aggregate(total_revenue=Sum("amount"))["total_revenue"]
                or 0
            )
            yearly_revenue.append(int(total_revenue))  # Ubah ke bilangan bulat (int)
        return yearly_revenue

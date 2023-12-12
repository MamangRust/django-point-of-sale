from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import PaymentForm
from decimal import Decimal
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.user.models import User
from .models import Payment


# Create your views here.
class PaymentListView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def get(self, request):
        payment = Payment.objects.all()

        return render(
            request=request,
            template_name="admin/payment/index.html",
            context={"payments": payment},
        )


class PaymentCreateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def post(self, request):
        form = PaymentForm(request.POST)

        if form.is_valid():
            user_id = form.cleaned_data["user"]
            user = get_object_or_404(User, pk=user_id)

            amount = form.cleaned_data["amount"]

            payment = Payment.objects.create(
                cartNumber=form.cleaned_data["cartNumber"],
                paymentMethod=form.cleaned_data["paymentMethod"],
                expirationDate=form.cleaned_data["expirationDate"],
                cvv=form.cleaned_data["cvv"],
                user=user,
                amount=Decimal(amount),
            )

            return JsonResponse(
                {"message": "Payment created successfully", "id": payment.id}
            )
        else:
            errors = form.errors.as_json()
            print(errors)
            return JsonResponse({"error": errors}, status=400)


class PaymentUpdateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def post(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = PaymentForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data["user"]
            user = get_object_or_404(User, pk=user_id)
            payment.cartNumber = form.cleaned_data["cartNumber"]
            payment.expirationDate = form.cleaned_data["expirationDate"]
            payment.cvv = form.cleaned_data["cvv"]
            payment.user = user
            payment.amount = form.cleaned_data["amount"]
            payment.save()
            return JsonResponse({"message": "Payment updated successfully"})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"error": errors}, status=400)


class PaymentDeleteView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def post(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()

        return JsonResponse({"message": "Payment delete successfully"})

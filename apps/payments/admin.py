from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "paymentMethod",
        "amount",
        "cartNumber",
        "expirationDate",
        "cvv",
    )  # Menampilkan bidang yang ingin ditampilkan di admin


admin.site.register(Payment, PaymentAdmin)

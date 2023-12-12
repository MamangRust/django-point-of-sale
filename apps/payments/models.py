from django.db import models
from apps.user.models import User
from apps.shared.models import TimeStampedModel


# Create your models here.
class Payment(TimeStampedModel):
    MASTERCARD = "mastercard"
    VISA = "visa"
    AMEX = "amex"

    PAYMENT_METHOD_CHOICES = [
        (MASTERCARD, "Mastercard"),
        (VISA, "Visa"),
        (AMEX, "American Express"),
    ]

    cartNumber = models.CharField(null=True, max_length=16)
    expirationDate = models.CharField(null=True, max_length=5)
    cvv = models.CharField(null=True, max_length=3)
    paymentMethod = models.CharField(
        null=True,
        max_length=17,
        choices=PAYMENT_METHOD_CHOICES,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

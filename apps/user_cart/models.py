from django.db import models
from apps.shared.models import TimeStampedModel
from apps.user.models import User
from apps.product.models import Product


# Create your models here.
class UserCart(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

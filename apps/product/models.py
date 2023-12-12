from django.db import models
from apps.shared.models import TimeStampedModel


# Create your models here.
class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    quantity = models.IntegerField(default=10)

    def __str__(self):
        return self.name

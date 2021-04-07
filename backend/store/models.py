from django.conf import settings
from django.db import models


class Product(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    price = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )
    quantity = models.IntegerField()


# Create your models here.

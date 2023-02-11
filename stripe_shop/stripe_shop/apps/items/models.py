from django.db import models
from django.core import validators

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=254, )
    description = models.CharField(max_length=500, )
    price = models.FloatField(validators=[validators.MinValueValidator(4.99),
                                          validators.MaxValueValidator(1000000)]
                              )  # price in $s

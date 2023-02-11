from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.


class Payment(models.Model):
    CURRENCY_CHOICES = (
        ('usd', 'USD'),
        ('aed', 'AED'),
    )

    stripe_id = models.CharField(max_length=128, db_index=True, blank=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='usd')  # e. g., in cents
    # order_id =
    created = models.DateTimeField(auto_now_add=True)

from django.db import models
from WhiteMarket.apps.user.models import User
from datetime import datetime

class ProductCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    created = models.DateTimeField(default=datetime.now, editable=False)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=250, blank=False)
    img = models.CharField(max_length=250, default='https://duckduckgo.com/assets/logo_header.v107.lg.svg')
    price = models.DecimalField(max_digits=30, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(
        ProductCategory,
        related_name='products',
        on_delete='models.CASCADE',
    )
    owner = models.ForeignKey(
        User,
        related_name='products',
        on_delete='models.CASCADE',
    )

    class Meta: 
        ordering = ('-created',)

    def __str__(self):
        return self.title


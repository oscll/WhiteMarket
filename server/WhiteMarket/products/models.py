from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=250, blank=False)
    img = models.CharField(max_length=250, default='https://duckduckgo.com/assets/logo_header.v107.lg.svg')
    price = models.DecimalField(max_digits=30, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    '''owner = models.ForeignKey(
        'auth.User',
        related_name='products',
        on_delete='models.CASCADE'
    )'''

    class Meta: 
        ordering = ['-created',]



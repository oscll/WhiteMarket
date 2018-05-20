from django.db import models
from WhiteMarket.apps.user.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class ProductCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    created = models.DateTimeField(default=datetime.now, editable=False)
    title = models.CharField(db_index=True, max_length=50, blank=False)
    price = models.DecimalField(db_index=True, max_digits=30, decimal_places=2)
    stock = models.PositiveIntegerField(db_index=True, default=1)
    description = models.CharField(db_index=True, max_length=10000, blank=False)
    state = models.PositiveSmallIntegerField(db_index=True, default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])
    img0 = models.CharField(db_index=True, max_length=250, blank=False)
    img1 = models.CharField(db_index=True, max_length=250, blank=True)
    img2 = models.CharField(db_index=True, max_length=250, blank=True)
    img3 = models.CharField(db_index=True, max_length=250, blank=True)
    img4 = models.CharField(db_index=True, max_length=250, blank=True)
    img5 = models.CharField(db_index=True, max_length=250, blank=True)
    img6 = models.CharField(db_index=True, max_length=250, blank=True)
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
    users_like = models.ManyToManyField(
        User,
        related_name='products_like',
        blank=True
    )
    total_likes = models.PositiveIntegerField(db_index=True, default=0)
    total_views = models.PositiveIntegerField(db_index=True, default=0, editable=False)

    class Meta:
        ordering = ('-created',)



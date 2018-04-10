# Generated by Django 2.0.4 on 2018-04-10 18:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20180316_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete='models.CASCADE', related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='productCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete='models.CASCADE', related_name='products', to='products.ProductCategory'),
        ),
    ]

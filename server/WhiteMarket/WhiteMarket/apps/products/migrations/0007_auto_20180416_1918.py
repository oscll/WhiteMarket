# Generated by Django 2.0.4 on 2018-04-16 19:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180411_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete='models.CASCADE', related_name='products', to='products.ProductCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete='models.CASCADE', related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]

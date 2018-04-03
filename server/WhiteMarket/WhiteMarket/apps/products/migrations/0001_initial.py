# Generated by Django 2.0.3 on 2018-03-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('img', models.CharField(default='https://duckduckgo.com/assets/logo_header.v107.lg.svg', max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
    ]

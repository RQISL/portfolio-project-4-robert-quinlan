# Generated by Django 3.2.20 on 2023-08-12 21:43

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ManyToManyField(related_name='item', to='order_foods.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('county', models.CharField(blank=True, max_length=15)),
                ('eirecode', models.CharField(blank=True, max_length=8)),
                ('items', models.ManyToManyField(blank=True, related_name='order', to='order_foods.MenuItem')),
            ],
        ),
    ]

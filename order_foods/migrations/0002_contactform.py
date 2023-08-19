# Generated by Django 3.2.20 on 2023-08-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
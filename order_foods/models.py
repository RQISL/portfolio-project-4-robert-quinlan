from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=15, blank=True)
    eirecode = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'


class ProfileView(models.Model):
    user = models.CharField(max_length=100, null=False, blank=False)
    bio = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.user

   
class ContactView(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.first_name
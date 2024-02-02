from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField


"""
This is Menu display in the page. The administer
can fill up detail the page with image, description of the
foods and prices.

The category will have option Starter, Main, Dessert
and Drink as follows below 'category class'

"""


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


"""
This is category in the database. The administer
can fill up the follow category as such e.g, Starter, Main, Dessert
and Drink. The administer can decide the word as they wish.

"""


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


"""
This is Order food menu display in the page.
When the order foods is selected and send
the page will have detail menu and prices
to confirmation if the user is happy with it.

"""


class OrderModel(models.Model):
    class Meta:
        verbose_name_plural = "Order Items"

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
        return f'Order Items: {self.created_on.strftime("%b %d %I: %M %p")}'


"""
This is profile record list of the users in the database.
The administer can modified but it is only for user modifty
in their own profile, which it is included CRUD in the profile
page.


"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    bio = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} Profile'


"""
In this article we will discuss How to fix 'ObjectDoesNotExist', Django, a
powerful web framework for Python, simplifies the process of building web
applications. However, developers often encounter the 'ObjectDoesNotExist'
exception, which arises when a query, executed through the get() method, fails
to find any matching records. In this article, we will delve into the details
of this exception and explore strategies to effectively handle it in Django
applications.

As above follow link iformation:
https://www.geeksforgeeks.org/objectdoesnotexist-error-in-django/

"""


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


"""
This is contact record list of the users in the database.
The administer can review their user address detail and foods.


"""


class ContactView(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.first_name

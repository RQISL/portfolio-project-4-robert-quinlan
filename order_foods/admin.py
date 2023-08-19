from .models import ProfileView
from django.contrib import admin
from .models import MenuItem, Category, OrderModel, ProfileView, ContactView
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(ProfileView)
admin.site.register(ContactView)

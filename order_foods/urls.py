"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from order_foods.views import (Home, About, Contact, Order,
                               OrderPayConfirmation, Thank_You
                               )

from order_foods import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('aboutus/', About.as_view(), name='aboutus'),
    path('contact/', Contact.as_view(), name='contact'),
    path('order_foods/', Order.as_view(), name='order_foods'),
    path('order-confirmation/<int:pk>', OrderPayConfirmation.as_view(),
         name='order-confirmation'),
    path('profile/<int:id>', views.profile_view, name='profile'),
    path('profile_add/', views.profile_create, name='profile_add'),
    path('update/<item_id>',
         views.profile_update, name='profile_update'),
    path('delete/',
         views.profile_delete, name='profile_delete'),
    path('thank_you/', Thank_You.as_view(), name='thank_you'),
]

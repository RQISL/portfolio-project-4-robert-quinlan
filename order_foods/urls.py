from django.contrib import admin
from django.urls import path, include
from order_foods.views import Home, About, Order, OrderConfirmation, OrderPayConfirmation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name='home'),
    path('aboutus/', About.as_view(), name='aboutus'),
    path('order_foods/', Order.as_view(), name='order_foods'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(),
         name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(),
         name='payment-confirmation'),
    # path('order_foods/', Order_Foods.as_view(), name='order_foods'),
]

"""codestar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from order_foods.views import Home, About, Login, Contact, ProfileView
from order_foods.views import Sign_up, Order, OrderPayConfirmation, DeleteFood

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name='home'),
    path('aboutus/', About.as_view(), name='aboutus'),
    path('contact/', Contact.as_view(), name='contact'),
    path('order_foods/', Order.as_view(), name='order_foods'),
    path('order-confirmation/<int:pk>', OrderPayConfirmation.as_view(),
         name='order-confirmation'),
    path('<pk>/delete/', DeleteFood.as_view(), name='delete_foods'),
    path('acoounts/login/', Login.as_view(), name='login'),
    path('accounts/signup/', Sign_up.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

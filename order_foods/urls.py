from . import views
from django.urls import path
from order_foods.views import OrderFoods

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('order_foods/', OrderFoods.as_view(), name='order_foods'),
    path('account/login/', views.sign_in, name='login'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='contact_and_feedback'),
]

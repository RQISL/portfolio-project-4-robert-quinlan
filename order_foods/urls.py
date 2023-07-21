from . import views
from django.urls import path
from order_foods.views import Overlay

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("overlay/", Overlay.as_view(), name="overlay"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='contact_and_feedback'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.posts, name="posts"),
    path('<slug:slug>', views.myposts, name="myposts"),
]
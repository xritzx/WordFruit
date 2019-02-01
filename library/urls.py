"""Urls patterns of the library App"""
from . import views
from django.urls import path

app_name = 'library'

urlpatterns = [
    path('', views.book, name='homepage'),
    path('<str:category>/', views.book, name='book'),
    path('like/<int:id>/', views.add_likes, name="like"), #hardcoded urlpattern implemented html id
    path("like/<int:id>/check/", views.has_liked, name="check_like") #exclusively for ajax check of user liked books
]
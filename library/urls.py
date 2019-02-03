"""Urls patterns of the library App"""
from . import views
from django.urls import path

app_name = 'library'

urlpatterns = [
    path('', views.book, name='homepage'),
    path('search/book/', views.search, name='search'),
    path('suggest/book/', views.suggest, name='suggestions'),
    path('<str:genre>/', views.book, name='book'),
    path('add/book/', views.add_book, name='addbook'),
    path('like/<int:id>/', views.add_likes, name="like"), #hardcoded urlpattern implemented html id
    path("like/<int:id>/check/", views.has_liked, name="check_like"), #exclusively for ajax check of user liked books
    path('read/<int:id>/', views.add_read, name="read"), #hardcoded urlpattern implemented html id
    path("read/<int:id>/check/", views.has_read, name="check_read"), #exclusively for ajax check of user read books
]
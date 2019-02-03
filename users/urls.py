from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

app_name = "users"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', login_required(views.profile), name='profile')
]

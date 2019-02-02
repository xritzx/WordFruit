from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

app_name = "users"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile')
]

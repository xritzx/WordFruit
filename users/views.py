from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

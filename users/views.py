from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.views.generic import CreateView


class SignUp(CreateView):
    
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    
def profile(req):
    user = req.user
    books = user.books_liked.all()
    return render(req, 'registration/profile.html', context={'books':books})
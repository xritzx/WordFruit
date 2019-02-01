"""A basic view for the Library App"""
from django.db.models import Count
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Book, Genre
from .forms import BookAddForm

def book(req, genre=None):

    if(genre != None):
        tag = Genre.objects.filter(name=genre)
        books = Book.objects.annotate(like_count=Count('likes')).order_by('-like_count').filter(tag__in=tag)[:20]
    else:
        books = Book.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:20]

    context = {
            'books': books,
            'genre': genre,
            }
    return render(req, 'library/homepage.html', context=context)
  

@login_required
def create_image(request):
    if request.method == 'POST':
        form = BookAddForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.contributor = request.user
            instance.save()
            return redirect('library:homepage')
    else:
        form = BookAddForm()
        return render(request, 'library/bookadd.html', {'form': form})

@login_required
def add_likes(request, id):
    
    user = request.user
    image = Book.objects.get(id=id)
    if user.pic_liked.filter(id=image.id).exists():
        image.likes.remove(user)
        image.save()
        return HttpResponse("Unliked")
    else:
        image.likes.add(user)
        image.save()
        return HttpResponse("Liked")

@login_required
def has_liked(request, id):

    user = request.user
    image = Book.objects.get(id=id)
    if user.pic_liked.filter(id=image.id).exists():
        return HttpResponse("True")
    else:
        return HttpResponse("False")

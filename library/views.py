"""A basic view for the Library App"""
from django.db.models import Count
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from users.models import CustomUser
from .models import Book, Genre
from .forms import BookAddForm

def book(req, genre=None):

    if(genre != None):
        tag = Genre.objects.filter(name=genre)
        books = Book.objects.annotate(like_count=Count('likes')).order_by('-like_count').filter(genre__in=tag)[:20]
    else:
        books = Book.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:20]

    context = {
            'books': books,
            'genre': genre,
            }
    return render(req, 'library/homepage.html', context=context)

def suggest(req):
    user = req.user
    books = user.books_liked.all()
    category={}
    
    for book in books:
        try:
            category[book.genre.name] += 1
        except:
            category[book.genre.name] = 1
    category = sorted([(v, k) for k, v in category.items()], reverse=True)
    if len(category) > 2:
        gen=Genre.objects.filter(name__in=[category[0][1],category[1][1]])
        suggestions = Book.objects.filter(genre__in=gen)
    elif 0 < len(category) < 2:
        suggestions = Book.objects.filter(genre=Genre.objects.get(name=category[0][1]))
    else:
        suggestions = None
    return render(req, 'library/suggestions.html', context={'books':suggestions})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookAddForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.contributor = request.user
            instance.save()
            return redirect('library:homepage')
        else:
            return render(request, 'library/addbook.html', {'form': form})
    else:
        form = BookAddForm()
        return render(request, 'library/addbook.html', {'form': form})

@login_required
def add_likes(request, id):
    
    user = request.user
    book = Book.objects.get(id=id)
    if user.books_liked.filter(id=book.id).exists():
        book.likes.remove(user)
        book.save()
        return HttpResponse("Unliked")
    else:
        book.likes.add(user)
        book.save()
        return HttpResponse("Liked")

@login_required
def has_liked(request, id):
    user = request.user
    book = Book.objects.get(id=id)
    if user.books_liked.filter(id=book.id).exists():
        return HttpResponse("True")
    else:
        return HttpResponse("False")

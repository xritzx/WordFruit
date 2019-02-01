from django.contrib import admin
from .models import Genre, Book

class LibraryAdmin(admin.ModelAdmin):

    list_display = ('book', 'date', 'genre')
    list_filter = ('date', 'genre')

admin.site.register(Book, LibraryAdmin)
admin.site.register(Genre)

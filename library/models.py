from django.contrib.auth import get_user_model
from datetime import datetime
from django.db import models
from stdimage import StdImageField
from django.conf import settings

User = get_user_model()

class Genre(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    
    book = models.CharField(max_length=100)
    ISBN = models.IntegerField()
    genre = models.ForeignKey(Genre, default=0, on_delete=models.CASCADE)
    image = StdImageField(upload_to='bookCover/', blank=True, variations={'thumbnail': (600, 800, True)})
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    ebook = models.FileField(upload_to='ebooks/', help_text="Upload the ebook if present", blank=True)
    date = models.DateField(auto_now=True, help_text="Date of Publication")
    read = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='has_read')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='books_liked')

    class Meta:

        verbose_name = "Book"
        verbose_name_plural = "Library"

    def __str__(self):
        return str(self.book)

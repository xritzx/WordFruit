from django.forms import ModelForm
from .models import Book

class  BookAddForm(ModelForm):

    class Meta:
        model = Book
        exclude = ['contributor', ]

from django import forms
from .models import Book

# ExampleForm that uses the Book model
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title"]  # include fields you want the form to handle

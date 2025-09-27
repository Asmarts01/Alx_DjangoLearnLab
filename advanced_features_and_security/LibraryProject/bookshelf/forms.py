# bookshelf/forms.py
from django import forms

# Required by ALX
class ExampleForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"})
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )

# Used in your project
class BookSearchForm(forms.Form):
    q = forms.CharField(
        label="Search Books",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter book title"})
    )

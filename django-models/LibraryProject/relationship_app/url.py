from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/text/', views.list_books_text, name='list_books_text'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path
from . import views
from .views import list_books, list_books_text, LibraryDetailView


urlpatterns = [
    # Book Views
    path('books/', views.list_books, name='list_books'),
    path('books/text/', views.list_books_text, name='list_books_text'),

    # Library View
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication Views
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
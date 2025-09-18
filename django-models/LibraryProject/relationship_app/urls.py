from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, list_books_text, LibraryDetailView, librarian_view, LibraryDetailView


urlpatterns = [
    # Book Views
    path('books/', views.list_books, name='list_books'),
    path('books/text/', views.list_books_text, name='list_books_text'),

    # Library View
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('librarian/', views.librarian_view, name='librarian_view'),

    # Authentication Views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    
    path('add_book/', views.add_book, name='add_book')
    path('books/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]

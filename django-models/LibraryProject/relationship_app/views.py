from django.shortcuts import render

# Create a function based view that list all books stored in the database
# This view should render a simple text list of book titles and their authors.

def list_books(request):
    from relationship_app.models import Book
    books = Book.objects.all()
    book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return render(request, 'list_books.html', {'book_list': book_list})

from django.http import HttpResponse
def list_books_text(request):
    from relationship_app.models import Book
    books = Book.objects.all()
    book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(book_list, content_type="text/plain")




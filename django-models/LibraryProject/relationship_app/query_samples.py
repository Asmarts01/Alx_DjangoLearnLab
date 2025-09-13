import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books= author.books.through.object.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []
    
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = Library.book.through.objects.filter(library=library)
        return [entry.book for entry in books]
    except Library.DoedNotExist:
        return []
    
def Librarian_of_library(library_name):
    try:
        Library = Library.objects.get(name=library_name)
        return Library.librarian
    except Library.DoesNotExist:
        return[]
    
if __name__ == "__main__":
    author_name = "J.K. Rowling"
    print(f"Books by {author_name}")
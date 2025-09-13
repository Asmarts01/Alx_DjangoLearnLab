>>> from bookshelf.models import Book
>>> try:
...     book = Book.objects.get(title__iexact="1984")
...     print(f"ID: {book.id}")
...     print(f"Title: {book.title}")
...     print(f"Author: {book.author}")
...     print(f"Publication Year: {book.publication_year}")  
... except ObjectDoesNotExist:
...     print("No book with that title exists.")
...                                                           
ID: 2
Title: 1984
Author: George Orwell
Publication Year: 1949
>>> from bookshelf.models import Book 
>>> book = Book.objects.create(title="1948", author="George Orwell", publication_year=1949)
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>, <Book: 1948 by George Orwell (1949)>]>
>>> book
<Book: 1948 by George Orwell (1949)>
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title__iexact="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>, <Book: Nineteen Eighty-Four by George Orwell (1949)>]>
>>>
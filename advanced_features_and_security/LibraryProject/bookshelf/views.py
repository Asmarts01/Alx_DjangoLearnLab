from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book


# View that requires the "can_view" permission
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


# View that requires the "can_create" permission
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Book.objects.create(title=title)
            return redirect("book_list")
    return render(request, "bookshelf/book_form.html")


# View that requires the "can_edit" permission
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            book.title = title
            book.save()
            return redirect("book_list")
    return render(request, "bookshelf/book_form.html", {"book": book})


# View that requires the "can_delete" permission
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("book_list")

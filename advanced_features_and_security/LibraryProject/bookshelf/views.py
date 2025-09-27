from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookSearchForm
from .forms import ExampleForm 


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

# View for searching books
def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = []
    if form.is_valid():
        query = form.cleaned_data.get("q")
        if query:
            books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_search.html", {"form": form, "books": books})

# ALX Required ExampleForm usage

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            # Render success page with submitted data
            return render(request, "bookshelf/example_success.html", {"name": name, "email": email})
    else:
        form = ExampleForm()
    return render(request, "bookshelf/example_form.html", {"form": form})

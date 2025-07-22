from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'libraryapp/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            isbn=request.POST['isbn'],
            publication_year=request.POST['publication_year']
        )
        return redirect('book_list')
    return render(request, 'libraryapp/book_form.html')

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.publication_year = request.POST['publication_year']
        book.save()
        return redirect('book_list')
    return render(request, 'libraryapp/book_form.html', {'book': book})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')

from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

def list_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_details(request):
    library = Library.objects.all()
    return render(request, 'relationship_app/library_detail.html', library)
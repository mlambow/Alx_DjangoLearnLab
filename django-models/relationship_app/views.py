from django.shortcuts import render
from .models import Book

def list_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_book.html', {'booka': books})

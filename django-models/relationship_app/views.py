from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

def list_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class libraryDetailsView(DetailView):
    model = Library
    library = Library.objects.all()
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
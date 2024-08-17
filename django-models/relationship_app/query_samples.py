from .models import Book, Librarian, Library

def books_by_author(author_name):
    author = Book.objects.get(name=author_name)
    books = 

def books_in_library(library_name):
     library_books = Library.objects.get(name=library_name) 
     books = books.all()
     return books

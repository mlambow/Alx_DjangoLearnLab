from .views import list_books, LibraryDetailView
from django.urls import path
from . import views
urlpatterns = [
    path('books/', list_books, name='list_book'),
    path('library/<int:pk>/', LibraryDetailView, name='library_detail')
]

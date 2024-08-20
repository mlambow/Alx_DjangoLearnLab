from .views import list_books, libraryDetailView
from django.urls import path
from . import views
urlpatterns = [
    path('books/', list_books, name='list_book'),
    path('library/<int:pk>/', libraryDetailView.as_views(), name='library_detail')
]

from django.urls import path
from .views import ListView, DeleteView, DetailView, CreateView, UpdateView

urlpatterns = [
    path('books', ListView.as_view(), name='book_list'),
    path('books/delete', DeleteView.as_view(), name='book_delete'),
    path('books/create', CreateView.as_view(), name='book_create'),
    path('books/detail/<int:pk>/', DetailView.as_view(), name='book_detail'),
    path('books/update', UpdateView.as_view(), name='book_update')
]

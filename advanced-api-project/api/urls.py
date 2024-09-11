from django.urls import path
from .views import ListView, DeleteView, DetailView, CreateView, UpdateView

urlpatterns = [
    path('book/', ListView.as_view(), name='book_list'),
    path('book/delete/<int:pk>/', DeleteView.as_view(), name='book_delete'),
    path('book/create/', CreateView.as_view(), name='book_create'),
    path('book/detail/<int:pk>/', DetailView.as_view(), name='book_detail'),
    path('book/update/<int:pk>/', UpdateView.as_view(), name='book_update')
]

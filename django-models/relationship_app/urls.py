from .views import list_books, LibraryDetailView
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_book'),
    path('library/<int:pk>/', LibraryDetailView, name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book/'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book/'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book/')
]

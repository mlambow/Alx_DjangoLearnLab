from views import list_book, libraryDetailsView
from django.urls import path
from . import views
urlpatterns = [
    path('books/', list_book, name='list_book'),
    path('library/<int:pk>/', libraryDetailsView.as_views(), name='library_detail')
]

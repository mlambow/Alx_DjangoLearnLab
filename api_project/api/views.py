from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from .models import Book

class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
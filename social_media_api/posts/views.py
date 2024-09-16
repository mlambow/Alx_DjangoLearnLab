from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer

class SetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter]
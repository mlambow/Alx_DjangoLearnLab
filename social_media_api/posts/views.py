from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from rest_framework import permissions
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer

class SetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter]

class PostFeedView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = SetPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_query(self):
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author_in=followed_users).order_by('-created_at')
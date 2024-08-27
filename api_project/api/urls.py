from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter

api = DefaultRouter()
api.register(r'book', BookList)

urlpatterns = [
    path('api/', include(api.urls))
]

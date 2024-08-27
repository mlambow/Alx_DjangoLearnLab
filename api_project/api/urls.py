from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookList)

urlpatterns = [
    path('api/', include(router.urls))
]

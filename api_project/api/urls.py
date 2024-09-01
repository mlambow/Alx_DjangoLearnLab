from django.urls import path, include
from .views import BookViewSet, BookList
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'book', BookViewSet)
#router.register(r'book', BookList)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token/', views.obtain_auth_token)
]

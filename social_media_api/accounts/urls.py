from django.urls import path
from rest_framework.authtoken import views
from .views import RegistrationView, LoginView, TokenRetrieveView, ProfileView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/', TokenRetrieveView.as_view(), name='token')
]

from django.urls import path
from rest_framework.authtoken import views
from .views import registration, login, profile

urlpatterns = [
    path('register/', registration, name='registration'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('api-token-auth', views.obtain_auth_token)
]

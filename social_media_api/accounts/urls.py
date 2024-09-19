from django.urls import path
from rest_framework.authtoken import views
from .views import RegistrationView, LoginView, TokenRetrieveView, ProfileView, FollowerListView, FollowingListView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/', TokenRetrieveView.as_view(), name='token'),

    #follow and unfollow
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow'),
]

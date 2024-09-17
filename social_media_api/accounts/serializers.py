from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['bio', 'profile_picture', 'followers']

class RegistrationSerializer(serializers.ModelSerializer):
    model = get_user_model()
    fields = ('id', 'username', 'email', 'password')

    def create_auth_token(created=False):
        user = get_user_model().objects.create_user()
        if created:
            Token.objects.create(user=user)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    passwork = serializers.CharField()
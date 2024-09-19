from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture', 'followers', 'following']

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_data']:
            raise serializers.ValidationError({'confirm_password': 'Password do not match'})
        return data
    
    def create(self, validated_data):
        del validated_data['confirm_password']
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        user = CustomUser.objects.get(username = data['username'])
        if not user.check_password(data['password']):
            raise serializers.ValidationError({'password': 'Invalid password'})
        self.validated_data['user'] = user
        return data
    
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'following']
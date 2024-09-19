from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import RegistrationSerializer, TokenSerializer, LoginSerializer, ProfileSerializer

class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user = user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create( user = user)
            return Response({'token': 'token.key'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class TokenRetrieveView(generics.GenericAPIView):
    permission_classes = permissions.IsAuthenticated
    serializer_class = TokenSerializer

    def get(self, request):
        token = Token.objects.get(user = request.user)
        serializer = self.get_serializer(token)
        return Response(serializer.data)
    
class ProfileView(generics.GenericAPIView):
    serializer_class = ProfileSerializer

    def patch(self, request):
        user = request.user
        serializer = self.get_serializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
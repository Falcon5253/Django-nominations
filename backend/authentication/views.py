from sqlite3 import connect

from django.contrib.auth import login, logout
from rest_framework.decorators import action
from rest_framework.exceptions import (AuthenticationFailed, NotFound,
                                       ValidationError)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

from authentication.models import User
from authentication.serializers import RegisterUserSerializer

from rest_framework.permissions import IsAuthenticated




# @action(methods=['POST'], detail=False, url_path='register')
@api_view(["POST"])
def register(request):
    serializer = RegisterUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message': 'success'})
    
@action(methods=['POST'], detail=False, url_path='login')
def login(self, request):
    if 'email' not in request.data:
        raise ValidationError({'error': 'email is empty'})
    
    if 'password' not in request.data:
        raise ValidationError({'error': 'password is empty'})
    
    email = request.data['email']
    password = request.data['password']
    try:
        user = User.objects.get(email=email)
        
    except User.DoesNotExist:
        raise NotFound({'error': 'user with this email was not found'})
    
    if not user.check_password(password):
        raise AuthenticationFailed({'error': 'incorrect password'})
    
    login(request=request, user=user)
    data = { "success":  "true" }
    return Response(data)


@action(methods=['GET'], detail=False, url_path='profile')
def get_user(self, request):
    data = { 'error':'Не авторизованный пользователь' }
    try:
        user = User.objects.get(id=request.user.id)
        data = self.serializer_class(user).data
    except:
        pass
    return Response(data)


@action(methods=['POST'], detail=False, url_path='logout')
def logout(self, request):
    logout(request)
    data = { 'success':'true' }
    return Response(data)
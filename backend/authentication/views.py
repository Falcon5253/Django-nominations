from sqlite3 import connect
from urllib import response
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from mysql import connector
import environ
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / '.env')
con = connector.connect(user=env('USER'),
    host=env('HOST'),
    database=env('NAME'),
    password=env('PASSWORD'))




class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        user = User.objects.get(email=request.data['email'])
        token = Token.objects.create(user=user)   

        return Response({'message': 'success'})
    
    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'error': 'email is empty'})
        if 'password' not in request.data:
            raise ValidationError({'error': 'password is empty'})
        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise NotFound({'error': 'user with this email was not found'})

        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'incorrect password'})

        cursor = con.cursor()
        query = ('SELECT * FROM `authtoken_token` WHERE `user_id`='+str(user.id))
        cursor.execute(query)
        for j in cursor:
            key = j[0]

        response = Response()
        response.set_cookie('token', key)
        return response


    @action(methods=['GET'], detail=False, url_path='me')
    def get_user(self, request):
        data = {}
        if request.COOKIES.get('token'):
            cursor = con.cursor()
            query = ('SELECT * FROM `authtoken_token` WHERE `key`="'+str(request.COOKIES.get('token'))+'"')
            cursor.execute(query)
            for j in cursor:
                user_id = j[2]
            user = User.objects.get(id=user_id)
            # user = User.objects.get(id=)
            data = self.serializer_class(user).data
        
        return Response(data)


    @action(methods=['POST'], detail=False, url_path='logout')
    def logout(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {'logout':'success'}
        return response
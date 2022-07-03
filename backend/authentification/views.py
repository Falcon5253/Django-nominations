from rest_framework.viewsets import ModelViewSet
from authentification.models import User
from authentification.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
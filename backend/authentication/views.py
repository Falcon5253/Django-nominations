from sqlite3 import connect

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.utils import formatting
from authentication.models import User
from rest_framework.views import APIView
from authentication.serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(GenericViewSet, APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_view_name(self):
        """
        Given a view instance, return a textual name to represent the view.
        This name is used in the browsable API, and in OPTIONS responses.

        This function is the default for the `VIEW_NAME_FUNCTION` setting.
        """
        # Name may be set by some Views, such as a ViewSet.
        name = getattr(self, 'name', None)
        if name is not None:
            return name

        name = self.__class__.__name__
        name = formatting.remove_trailing_string(name, 'View')
        name = formatting.remove_trailing_string(name, 'ViewSet')
        name = formatting.camelcase_to_spaces(name)

        return name
    
    def list(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_anonymous:
            serializer = self.get_serializer(user, many=False)
            return Response(serializer.data)
        data = { 'Warning':'You are not authorized' }
        return Response(data)
    
    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'success'})
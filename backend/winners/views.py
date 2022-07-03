from rest_framework.viewsets import ModelViewSet
from winners.serializers import WinnerSerialzer
from winners.models import Winners

class WinnerViewSet(ModelViewSet):
    queryset = Winners.objects.all()
    serializer_class = WinnerSerialzer
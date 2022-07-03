from rest_framework.viewsets import ModelViewSet
from organizer.serializers import OrganizerSerializer
from organizer.models import Organizer

class OrganizerViewSet(ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
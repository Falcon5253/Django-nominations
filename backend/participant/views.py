from rest_framework.viewsets import ModelViewSet
from participant.serializers import ParticipantSerializer
from participant.models import Participant

class ParticipantViewSet(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
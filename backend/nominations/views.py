from rest_framework.viewsets import ModelViewSet
from nominations.serializers import NominationSerializer
from nominations.models import Nomination

class NominationViewSet(ModelViewSet):
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
from rest_framework.viewsets import ModelViewSet
from nomination.serializers import NominationSerializer
from nomination.models import Nomination

class NominationViewSet(ModelViewSet):
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
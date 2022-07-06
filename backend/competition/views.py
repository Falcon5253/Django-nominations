from rest_framework.viewsets import ModelViewSet
from competition.serializers import CompetitionSerializer
from competition.models import Competition

class CompetitionViewSet(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
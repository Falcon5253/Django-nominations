import imp
from rest_framework.viewsets import ModelViewSet
from vote.models import Vote
from vote.serializers import VoteSerializer

class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
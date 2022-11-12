from rest_framework.viewsets import ModelViewSet
from participant.serializers import ParticipantSerializer
from participant.models import Participant
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from authentication.models import User
import json

class ParticipantViewSet(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


    @action(methods=['POST'], detail=False, url_path='participants')
    def get_participants(self, request):
        participants = Participant.objects.filter(competition_id= request.data['id'])
        users = []
        for participant in json.loads(serializers.serialize('json', participants)):
            users.append(User.objects.get(id = participant['fields']['user_id']))
        data = {}
        for user in json.loads(serializers.serialize('json', users)):
            data[user['pk']] = {'first_name': user['fields']['first_name'], 'last_name': user['fields']['last_name'], 'photo': user['fields']['photo']}
        return Response(data)
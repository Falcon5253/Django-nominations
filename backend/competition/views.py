from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Participant
from .serializers import CompetitionSerializer, WinnerSerialzer, NominationSerializer, ParticipantSerializer, VoteSerializer
from .models import Competition, Winner, Nomination, Vote
from authentication.models import User
from django.core import serializers
import json

class CompetitionViewSet(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class WinnerViewSet(ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerialzer

    @action(methods=['GET'], detail=False, url_path='winners')
    def get_winners(self, request):
        winners = serializers.serialize('json', Winner.objects.all())
        winners = json.loads(winners)
        data = {}
        participants_competitions = []
        for winner in winners:
            participants_competitions.append( {
                'participant': Participant.objects.get(id = winner['fields']['participant_id']), 
                'competition': Competition.objects.get(id = winner['fields']['competititon_id'])
                })
 
        for participant_competition in participants_competitions:
            user = User.objects.get(id = json.loads(serializers.serialize('json', [participant_competition['participant']]))[0]['fields']['user_id'])
            nomination = Nomination.objects.get(id = json.loads(serializers.serialize('json', [participant_competition['competition']]))[0]['fields']['nomination_id'])
            first_name =  json.loads(serializers.serialize('json', [user]))[0]['fields']['first_name']
            last_name =  json.loads(serializers.serialize('json', [user]))[0]['fields']['last_name']
            photo =  json.loads(serializers.serialize('json', [user]))[0]['fields']['photo']
            nomination_title = json.loads(serializers.serialize('json', [nomination]))[0]['fields']['title']
            year = json.loads(serializers.serialize('json', [participant_competition['competition']]))[0]['fields']['year']

            data[json.loads(serializers.serialize('json', [user]))[0]['pk']] = {'first_name': first_name, 'last_name': last_name, 'nomination_title':  nomination_title, 'year': year, 'photo': photo}
            
        return Response(data)


class NominationViewSet(ModelViewSet):
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer


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


class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
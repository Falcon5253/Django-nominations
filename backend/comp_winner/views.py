from rest_framework.viewsets import ModelViewSet
from nomination.models import Nomination
from comp_winner.serializers import CompWinnerSerialzer
from comp_winner.models import CompWinner
from competition.models import Competition
from rest_framework.decorators import action
from django.core import serializers
from authentication.models import User
from participant.models import Participant
from rest_framework.response import Response
import json

class CompWinnerViewSet(ModelViewSet):
    queryset = CompWinner.objects.all()
    serializer_class = CompWinnerSerialzer

    @action(methods=['GET'], detail=False, url_path='winners')
    def get_winners(self, request):
        winners = serializers.serialize('json', CompWinner.objects.all())
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
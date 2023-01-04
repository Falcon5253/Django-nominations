from rest_framework import serializers
from .models import Competition, Winner, Nomination, Participant, Vote

class CompetitionSerializer(serializers.ModelSerializer):
    nomination = serializers.CharField(source='nomination.title')
    class Meta:
        model = Competition
        fields = '__all__'


class WinnerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = '__all__'


class NominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomination
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
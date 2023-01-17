from rest_framework import serializers
from .models import Competition, Winner, Nomination, Participant, Vote
from rest_framework.fields import empty

class CompetitionSerializer(serializers.ModelSerializer):
    nomination = serializers.CharField(source='nomination.title')
    
    def __init__(self, instance=None, data=empty, **kwargs):
        self.Meta.fields = ['nomination', 'description', 'concluded_at']
        super(CompetitionSerializer, self).__init__(instance=None, data=data, **kwargs)
    
    def create(self, validated_data):
        nomination = validated_data['nomination']
        title = nomination['title']
        validated_data["nomination"] = Nomination.objects.get(title=title)
        return super(CompetitionSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        nomination = validated_data['nomination']
        title = nomination['title']
        validated_data["nomination"] = Nomination.objects.get(title=title)
        return super(CompetitionSerializer, self).create(validated_data)
    
    
    class Meta:
        model = Competition
        fields = ['nomination', 'description', 'concluded_at']
        


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
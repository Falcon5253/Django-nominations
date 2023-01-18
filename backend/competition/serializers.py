from rest_framework import serializers
from .models import Competition, Winner, Nomination, Participant, Vote
from rest_framework.fields import empty
from django.utils import timezone



class CompetitionSerializer(serializers.ModelSerializer):
    nomination_title = serializers.CharField(source='nomination.title', read_only=True)

    def __init__(self, instance=None, data=empty, **kwargs):
        super(CompetitionSerializer, self).__init__(instance=instance, data=data, **kwargs)
    
    
    class Meta:
        model = Competition
        fields = ['nomination_title', 'nomination', 'description', 'concluded_at', 'cover', 'organizer']


class CompetitionAdminSerializer(CompetitionSerializer):
    organizer = serializers.EmailField(default=None)
    
    class Meta:
        model = Competition
        fields = '__all__'


# TODO: Добавить ссылку на детальную страницу
class CompetitionOrganizerSerializer(CompetitionSerializer):
    organizer_email = serializers.EmailField(read_only=True, source='organizer.email')
    
    def update(self, instance, validated_data):
        validated_data['created_at'] = timezone.now().date()
        return super().update(instance, validated_data)
    
    class Meta:
        model = Competition
        fields = ['nomination', 'nomination_title', 'concluded_at', 'description', 'cover' , 'organizer', 'organizer_email']




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
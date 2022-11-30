from rest_framework import serializers
from competition.models import Competition

class CompetitionSerializer(serializers.ModelSerializer):
    nomination = serializers.CharField(source='nomination_title.title')
    class Meta:
        model = Competition
        fields = '__all__'
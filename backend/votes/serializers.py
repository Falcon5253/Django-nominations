import imp
from rest_framework import serializers
from votes.models import Votes

class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes
        fields = '__all__'
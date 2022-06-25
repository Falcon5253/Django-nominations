from dataclasses import field
from rest_framework import serializers
from nominations.models import Nomination

class NominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomination
        fields = '__all__'
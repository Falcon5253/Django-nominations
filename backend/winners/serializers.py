from rest_framework import serializers
from winners.models import Winners

class WinnerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Winners
        fields = '__all__'
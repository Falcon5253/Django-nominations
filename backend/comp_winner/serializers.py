from rest_framework import serializers
from comp_winner.models import CompWinner

class CompWinnerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CompWinner
        fields = '__all__'
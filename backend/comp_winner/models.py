from django.db import models
from participant.models import Participant

class CompWinner(models.Model):
    participant_id = models.OneToOneField(to=Participant, on_delete=models.CASCADE, verbose_name='participant')

    def __str__(self):
        return str(self.competititon_id)
    
    class Meta:
        verbose_name = 'Победитель'
        verbose_name_plural = 'Победители'

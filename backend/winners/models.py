from statistics import mode
from django.db import models
from competition.models import Competition
from participant.models import Participant

class Winners(models.Model):
    competititon_id = models.OneToOneField(to=Competition, on_delete=models.CASCADE, verbose_name='competition')
    participant_id = models.OneToOneField(to=Participant, on_delete=models.CASCADE, verbose_name='participant')

    def __str__(self):
        return str(self.competititon_id)
    
    class Meta:
        verbose_name = 'Победитель'
        verbose_name_plural = 'Победители'

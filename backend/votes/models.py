from django.db import models
from competition.models import Competition
from authentification.models import User
from participant.models import Participant

class Votes(models.Model):
    competition_id = models.OneToOneField(to=Competition, verbose_name='competition', on_delete=models.CASCADE)
    user_id = models.OneToOneField(to=User, verbose_name='user', on_delete=models.CASCADE)
    voted_for = models.OneToOneField(to=Participant, verbose_name='voted_for', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.competition_id)
    
    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'
from django.db import models
from authentication.models import User
from competition.models import Competition

class Participant(models.Model):
    competition_id = models.ForeignKey(verbose_name='competition', to=Competition, on_delete=models.CASCADE)
    user_id = models.ForeignKey(verbose_name='user', to=User, on_delete=models.CASCADE)
    participations_number = models.IntegerField(verbose_name='число участий')

    def __str__(self):
        return str(self.user_id)
    
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
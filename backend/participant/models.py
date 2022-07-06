from django.db import models
from authentication.models import User
from competition.models import Competition

class Participant(models.Model):
    competition_id = models.ManyToManyField(verbose_name='competition', to=Competition)
    user_id = models.OneToOneField(verbose_name='user', to=User, on_delete=models.CASCADE)
    participations_number = models.IntegerField(verbose_name='число участий')

    def __str__(self):
        return str(self.user_id)
    
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
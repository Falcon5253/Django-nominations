from django.db import models
import django
from authentication.models import User


class Nomination(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, unique=True)
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Номинация'
        verbose_name_plural = 'Номинации'



class Competition(models.Model):
    nomination = models.ForeignKey(to=Nomination, verbose_name='nomination', related_name='competition', on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name='Дата создания', default=django.utils.timezone.now)
    concluded_at = models.DateField(verbose_name='Дата завершения', null=True, default=None)
    description = models.TextField(verbose_name='Описание', null=True, default=None) # При создании экземпляра, если null, то должно приравниваться к описанию номинации
    organizer_id = models.ForeignKey(to=User, verbose_name='organizer', related_name='competition', on_delete=models.CASCADE)
    cover = models.ImageField(verbose_name='Обложка', upload_to='competition/cover')

    def __str__(self):
        return str(self.nomination.title) + ' (' + str(self.created_at) + ')'

    def save(self, *args, **kwargs):
        if self.description == "":
            self.description = self.nomination.description
        
        super(Competition, self).save(*args, **kwargs)
        
    
    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'



class Participant(models.Model):
    competition_id = models.ForeignKey(verbose_name='competition', to=Competition, on_delete=models.CASCADE)
    user_id = models.ForeignKey(verbose_name='user', to=User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)
    
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'




class Winner(models.Model):
    participant_id = models.OneToOneField(to=Participant, on_delete=models.CASCADE, verbose_name='participant')

    def __str__(self):
        return str(self.participant_id)
    
    class Meta:
        verbose_name = 'Победитель'
        verbose_name_plural = 'Победители'


class Vote(models.Model):
    user = models.ForeignKey(to=User, verbose_name='user', on_delete=models.CASCADE)
    voted_for = models.ForeignKey(to=Participant, verbose_name='voted_for', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " за " + str(self.voted_for)
    
    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'
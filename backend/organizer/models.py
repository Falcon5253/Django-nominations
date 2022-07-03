from tabnanny import verbose
from django.db import models
from authentication.models import User

class Organizer(models.Model):
    user_id = models.OneToOneField(verbose_name='Пользователь', to=User, related_name='organizer', on_delete=models.CASCADE)
    competitions_number = models.IntegerField(verbose_name='Число соревнований', default=0)

    def __str__(self):
        return str(self.user_id)
    
    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'
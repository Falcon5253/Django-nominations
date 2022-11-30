from django.db import models
from nomination.models import Nomination
from authentication.models import User
from datetime import date


class Competition(models.Model):
    nomination = models.ForeignKey(to=Nomination, verbose_name='nomination', related_name='competition', on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="Дата создания", default=date.today())
    concluded_at = models.DateField(verbose_name="Дата создания", null=True, default=None)
    organizer_id = models.ForeignKey(to=User, verbose_name='organizer', related_name='competition', on_delete=models.CASCADE)
    cover = models.ImageField(verbose_name='Обложка', upload_to='competition/cover')

    def __str__(self):
        return str(self.nomination.title) + ' (' + str(self.created_at) + ')'

    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'
from django.db import models
from nominations.models import Nomination
from organizer.models import Organizer


class Competition(models.Model):
    nomination_id = models.ForeignKey(to=Nomination, verbose_name='nomination', related_name='competition', on_delete=models.CASCADE)
    year = models.DateField(verbose_name='Дата')
    organizer_id = models.ForeignKey(to=Organizer, verbose_name='organizer', related_name='competition', on_delete=models.CASCADE)
    cover = models.ImageField(verbose_name='Обложка', upload_to='competition/cover')

    def __str__(self):
        return str(self.nomination_id)

    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'
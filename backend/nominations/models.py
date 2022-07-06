from django.db import models

class Nomination(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Номинация'
        verbose_name_plural = 'Номинации'
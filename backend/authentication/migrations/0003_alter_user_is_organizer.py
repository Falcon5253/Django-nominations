# Generated by Django 4.0.5 on 2023-01-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_organizer',
            field=models.BooleanField(default=False, verbose_name='организатор'),
        ),
    ]

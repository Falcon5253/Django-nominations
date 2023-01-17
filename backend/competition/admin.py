from django import forms
from django.contrib import admin
from core.admin import my_admin_site

from competition.models import Competition, Winner, Nomination, Participant, Vote
from authentication.models import User


my_admin_site.register(Winner)
my_admin_site.register(Nomination)
my_admin_site.register(Participant)
my_admin_site.register(Vote)


class CompetitionForm(forms.ModelForm):
    nomination = forms.ModelChoiceField(label='Номинация', queryset=Nomination.objects.all())
    created_at = forms.DateField(label='Дата создания', widget=forms.SelectDateWidget)
    concluded_at = forms.DateField(label='Дата завершения', widget=forms.SelectDateWidget)
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'placeholder': 'Оставьте пустым, чтобы использовать стандартное описание номинации', 'style':'resize: none'}),
        required=False
    )
                                  
    organizer_id = forms.ModelChoiceField(label='Организатор', queryset=User.objects.filter(is_organizer=True))
    cover = forms.ImageField(label='Обложка')


@admin.register(Competition, site=my_admin_site)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'concluded_at')
    form = CompetitionForm

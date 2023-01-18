from django import forms
from django.contrib import admin
from core.admin import my_admin_site
from django.core.exceptions import PermissionDenied
from competition.models import Competition, Winner, Nomination, Participant, Vote
from authentication.models import User
from import_export.admin import ExportActionMixin
import tablib

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


class CustomExportMixin(ExportActionMixin):
    
    def get_export_data(self, file_format, queryset, *args, **kwargs):
        request = kwargs.pop("request")
        if not self.has_export_permission(request):
            raise PermissionDenied

        data = self.get_data_for_export(request, queryset, *args, **kwargs)
        data2 = tablib.Dataset()
        data2.headers = data.headers
        for x in range(0, data.height):
            id, nomination_id, created_at, concluded_at, description, organizer_id, cover = data.lpop()
            nomination = Nomination.objects.get(id=nomination_id)
            organizer = User.objects.get(id=organizer_id)
            
            nomination = nomination.title + " (" + concluded_at + ")"
            organizer = organizer.email
            data2.append((id, nomination, created_at, concluded_at, description, organizer, cover))

        data = data2
        export_data = file_format.export_data(data)
        encoding = kwargs.get("encoding")
        if not file_format.is_binary() and encoding:
            export_data = export_data.encode(encoding)
        return export_data

@admin.register(Competition, site=my_admin_site)
class CompetitionAdmin(CustomExportMixin, admin.ModelAdmin):
    list_display = ('id', '__str__', 'description', 'concluded_at')
    form = CompetitionForm

from django.contrib import admin
from competition.models import Competition, Winner, Nomination, Participant, Vote


admin.site.register(Competition)
admin.site.register(Winner)
admin.site.register(Nomination)
admin.site.register(Participant)
admin.site.register(Vote)
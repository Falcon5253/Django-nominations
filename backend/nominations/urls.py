from django.urls import path
from nominations.views import nominations_list

urlpatterns = [
    path('nominations', nominations_list)
]

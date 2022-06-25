from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
from nominations.models import Nomination
from nominations.serializers import NominationSerializer


@api_view()
def nominations_list(request):
    nominations = Nomination.objects.all()
    data = NominationSerializer(instance=nominations, many=True).data
    return Response(data={'data':data})
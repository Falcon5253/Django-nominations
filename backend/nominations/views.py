from django.http import JsonResponse, HttpResponse

def nominations_list(request):
    return JsonResponse(data={'status':'ok'})
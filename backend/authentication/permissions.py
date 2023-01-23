from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from competition.models import Competition
from authentication.models import User


class IsOrganizer(BasePermission):
    message = 'Не организатор'
    def has_permission(self, request, view):
        return bool(request.user.is_organizer)

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.organizer.id
    

class IsNotAuthenticated(BasePermission):
    message = 'Вы уже авторизованы'
    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)

class IsAdminUser(BasePermission):
    message = 'Не админ'
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_superuser)
    
try:
    content_type = ContentType.objects.get_for_model(Competition)
    comp_permission = Permission.objects.filter(content_type=content_type)

    organizers = User.objects.filter(is_organizer=True)

    for perm in comp_permission:
        for user in organizers:
            user.user_permissions.add(perm)
except:
    pass
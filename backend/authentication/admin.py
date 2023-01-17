from django.contrib import admin
from core.admin import my_admin_site
from authentication.models import User

@admin.register(User, site=my_admin_site)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nickname', 'description')
    list_display_links = ('id', 'email')

from django.contrib import admin
from core.admin import my_admin_site
from authentication.models import User
from import_export.admin import ExportActionMixin

@admin.register(User, site=my_admin_site)
class UserAdmin(admin.ModelAdmin, ExportActionMixin):
    list_display = ('id', 'email', 'nickname', 'description')
    list_display_links = ('id', 'email')

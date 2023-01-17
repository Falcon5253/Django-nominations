from django.contrib import admin
from django.contrib.admin.forms import AdminAuthenticationForm
from django.core.exceptions import ValidationError

class UserForm(AdminAuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )


class CustomAdminSite(admin.AdminSite):
    login_form = UserForm
    
    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser
    
my_admin_site = CustomAdminSite()
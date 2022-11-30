from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname
        )

        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email = self.normalize_email(email),
            nickname = nickname,
            password = password,
        )

        user.is_active = True
        user.is_staff = True
        user.is_organizer = True
        user.is_superuser = True
        user.save()
        
        return user
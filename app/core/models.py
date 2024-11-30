from django.db import models # naqo

from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)


class UserManager(BaseUserManager):
    """Manager for Users."""

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    email = models.EmailField(max_length = 255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

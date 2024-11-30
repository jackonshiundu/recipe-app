from django.db import models  # naqo

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    """Manager for Users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a user with an email and password."""
        user = self.model(email=email, **extra_fields)  # Fixed: Removed extra spaces around '='
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)  # Fixed: Removed extra spaces around '='
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # Fixed: Removed extra spaces around '='
    is_staff = models.BooleanField(default=True)  # Fixed: Changed 'is_stuff' to 'is_staff'

    objects = UserManager()

    USERNAME_FIELD = 'email'

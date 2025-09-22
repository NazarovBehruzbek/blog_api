from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin

# Create your models here.
class User(AbstractUser,PermissionsMixin):
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields here
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

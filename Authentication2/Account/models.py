from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length=12,unique=True)
    USERNAME_FIELD = 'user_id'
    # REQUIRED_FIELDS='email'
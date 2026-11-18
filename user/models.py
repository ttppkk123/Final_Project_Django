from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    phone_number = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
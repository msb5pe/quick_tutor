""" 
V1: Login with Google works 
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login = models.DateTimeField('date created', default=timezone.now)
    # classes = models.ListCharField(models.CharField)

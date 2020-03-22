""" 
V1: Login with Google works 
"""


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField('date account created', default=None)

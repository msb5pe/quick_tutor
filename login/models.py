""" V1: Login with Google works """


from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    token = models.CharField(max_length=200, primary_key=True, default='0000000')
    last_signin = models.DateTimeField('Last sign-in', default=timezone.now)

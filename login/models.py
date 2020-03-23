""" 
V1: Login with Google works 
V1.2: Adjusted Profile model to include a boolean field for determining if someone has been helped
    and one for if he/she is a tutor
"""


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

<<<<<<< HEAD
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField('date account created', default=None)
=======


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User)    
    classes = ArrayField(models.CharField(max_length=5),default=list)
    helped = models.BooleanField(default=False)
    tutor = models.BooleanField(default=False)
>>>>>>> arvindbranch

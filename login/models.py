""" 
V1: Login with Google works 
V1.2: Adjusted Profile model to include a boolean field for determining if someone has been helped
    and one for if he/she is a tutor
"""


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User)    
    classes = ArrayField(models.CharField(max_length=5),default=list)
    helped = models.BooleanField(default=False)
    tutor = models.BooleanField(default=False)

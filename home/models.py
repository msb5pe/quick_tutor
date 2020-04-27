from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TutorRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=31, blank=False)
    classes = models.CharField(max_length=400, default="None")
    location = models.CharField(max_length=200, null=True, blank=True)
    helped = models.BooleanField(default=False)
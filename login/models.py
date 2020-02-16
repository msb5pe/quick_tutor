from django.db import models

# Create your models here.
#- alex

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

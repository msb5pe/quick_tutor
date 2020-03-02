""" V1.1: configured login admin """
from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.register(Profile)
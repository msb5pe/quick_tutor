""" V1.1: configured login admin """
from django.contrib import admin
from .models import TutorRequest

# Register your models here.
admin.site.register(TutorRequest)
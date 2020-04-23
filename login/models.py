""" 
V1: Login with Google works 
V1.2: Adjusted Profile model to include a boolean field for determining if someone has been helped
    and one for if he/she is a tutor
"""


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User


class Location(models.Model):
    placeName = models.CharField(max_length=100)

    def __str(self):
        return self.placeName

    def getPlaceName(self):
        return self.placeName


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField('date account created', default=timezone.now)
    picture = models.URLField(max_length=500, default="https://source.unsplash.com/random/200×200/?fruit")
    # image = models.ImageField(upload_to='profile_image', blank=True)
    classes = models.CharField(max_length=400, default="None")
    helped = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
    # location = models.ForeignKey("Location", null=True, blank=True, on_delete=models.CASCADE)
    # location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    first_time_user = models.BooleanField(default=True)
    phone = models.CharField(max_length=31, blank=False)


    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

def get_username(self):
    return self.username
User.add_to_class("__str__", get_username)

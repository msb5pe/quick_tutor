from .models import UserProfile
from django.utils import timezone
import datetime
from django.db import models

def save_profile(backend, user, response,  *args, **kwargs):
    if UserProfile.objects.filter(user_id=user.id).count()==0 :
        userProfile = UserProfile.objects.create(
            user=user,
            first_name=response['given_name'],
            last_name=response['family_name'],
            email=response['email'],
            date_created=timezone.now(),
            picture=response['picture'])
        userProfile.save()


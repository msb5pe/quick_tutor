from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse
from django.apps import apps
from django.views import generic

UserProfile = apps.get_model('login', 'UserProfile')

def find_user(u):
    return UserProfile.objects.filter(user=u)[0]


def index(request):
    user_profile = find_user(request.user)
    if(user_profile.is_tutor):
        #online_profiles = get_current_profiles(request.user)
        same_location = get_students_only(get_same_location(request.user.userprofile.location, UserProfile.objects.all()))
        payload = {'userprofile':user_profile, 'same_location':same_location, 'classes':user_profile.classes.split(',')}
        return render(request, 'home/dashboard.html', payload)
    else:
        #Notif page
        return HttpResponse("Waiting for tutor....")


# Gets online users
def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)
    #return UserProfile.objects.filter(id__in=user_id_list)

def get_current_profiles(user):
    onlineUsers = get_current_users()
    onlineProfiles = []
    for online in onlineUsers:
        onlineProfiles.append(online.userprofile)
    return onlineProfiles

def get_same_location(location, profiles):
    for profile in profiles:
        if location != profile.location:
            profiles.remove(profile)
    return profiles

def get_students_only(users):
    ret_ary = []
    for u in users:
        if(not u.is_tutor):
            ret_ary.append(u)
    return ret_ary
        


# onlineProfiles = get_current_profiles(request.user)
# onlineSameLocation = get_same_location(request.user.userprofile.location, onlineProfiles)

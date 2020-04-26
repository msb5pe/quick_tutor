from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse
from django.apps import apps
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import TutorRequest

UserProfile = apps.get_model('login', 'UserProfile')

def find_user(u):
    return UserProfile.objects.filter(user=u)[0]

@login_required()
def index(request):
    user_profile = find_user(request.user)
    if(user_profile.is_tutor):
        #online_profiles = get_current_profiles(request.user)
        # same_location = get_students_only(get_same_location(request.user.userprofile.location, UserProfile.objects.all()))
        same_location = get_requests(request.user.userprofile.location)
        payload = {'userprofile':user_profile, 'same_location':same_location, 'classes':user_profile.classes.split(',')}
        return render(request, 'home/dashboard.html', payload)
    else:
        #Notif page
        payload = {'userprofile':user_profile, 'classes':user_profile.classes.split(',')}
        return render(request, 'home/loadingpage.html', payload)


def create_request(request):
    user_profile = find_user(request.user)
    classes = request.POST.getlist('classes')
    loc = request.POST.get('location')
    cls_str = classes[0]
    for c in classes[1:]:
        if (c != ""):
            cls_str = cls_str + "," + c
    if not request.user.userprofile.is_tutor:
        new_request = TutorRequest(user=request.user, phone=request.user.userprofile.phone,
                                    classes=cls_str, location=loc)
        new_request.save()
    user_profile.classes = cls_str
    user_profile.location = loc
    user_profile.save()
    return redirect('home:index')

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

# returns profiles at same location as parameter location
def get_same_location(location, profiles):
    locs = []
    for profile in profiles:
        if location == profile.location:
            locs.append(profile)
    return locs

# takes in and returns profiles?
def get_students_only(profiles):
    students = []
    for u in profiles:
        if(not u.is_tutor):
            students.append(u)
    return students

# returns all requests in the same location
def get_requests(location):
    locs = []
    tutor_requests = TutorRequest.objects.all()
    for profile in tutor_requests:
        if location == profile.location:
            locs.append(profile)
    return locs


# Delete request object
def delete_request(request):
    request.POST.get('location')
    return redirect('home:index')




# onlineProfiles = get_current_profiles(request.user)
# onlineSameLocation = get_same_location(request.user.userprofile.location, onlineProfiles)

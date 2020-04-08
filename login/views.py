""" V1: Login with Google works """

from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .models import UserProfile
from .forms import DeptForm
from .models import UserProfile, Location
import requests

def find_user(u):
    return UserProfile.objects.filter(user=u)[0]

def logout_success(request):
    logout(request)
    return redirect('login:index')

class IndexView(generic.TemplateView):
    template_name = 'login/index.html'
    context_object_name = 'UserProfile'
    def get_queryset(self, request):
        return find_user(request.user)

def class_select_isTutor(request):
    user_profile = find_user(request.user)
    user_profile.is_tutor = True
    user_profile.save()
    return render(request,'login/dept.html')

def class_select_isTutee(request):
    return render(request, 'login/dept.html')

def class_selector(request):
    user_profile = find_user(request.user)
    r = requests.get("http://stardock.cs.virginia.edu/louslist/courses/view/" + request.POST['department'] + "?JSON")
    ret_ary = []
    for line in r.text.split("\n"):
        s = line.split(';')
        try:
            ret_ary.append(s[0] + " " + s[1])
        except:
            pass
    ret_ary = list(set(ret_ary))
    if r.status_code == 200:
        payload = {'classes': ret_ary}
        return render(request,'login/classes.html', payload)
    return render(request, 'login/dept.html')

def select_location(request):
    locations_list = Location.objects.order_by('placeName')
    template = loader.get_template('login/locations.html')
    context = {'locations_list': locations_list, }
    return render(request, 'login/locations.html', context)

# Test function to show the selected location
# Used with location_test.html
def select_location2(request):
    user_profile = find_user(request.user)
    try:
        loc = request.POST.get('location')
        user_profile.location = loc
        user_profile.save()
    except Exception as e:
        print(e)
        return render(request, 'login/locations.html', {
            'error_message': "Empty text fields",
        })
    else:
        return HttpResponse(loc)
    # Set location and then redirect!!!


def class_select_isTutee(request):
    return render(request, 'login/dept.html')

def class_selector(request):
    user_profile = find_user(request.user)
    r = requests.get("http://stardock.cs.virginia.edu/louslist/courses/view/" + request.POST['department'] + "?JSON")
    ret_ary = []
    for line in r.text.split("\n"):
        s = line.split(';')
        try:
            ret_ary.append(s[0] + " " + s[1])
        except:
            pass
    ret_ary = list(set(ret_ary))
    if r.status_code == 200:
        payload = {'classes': ret_ary}
        return render(request,'login/classes.html', payload)
    return render(request, 'login/dept.html')

def authflowhandler(request):
    return render(request, 'login/is_tutor.html')    

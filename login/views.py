""" V1: Login with Google works """

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout
from .models import UserProfile, Location
from .forms import set_location_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm




def logout_success(request):
    logout(request)
    return redirect('login:index')

class IndexView(generic.TemplateView):
    template_name = 'login/index.html'
    context_object_name = 'UserProfile'

    def get_queryset(self, request):
        """Return the last five published questions."""
        return UserProfile.objects.filter(user=request.user)

def class_select_isTutor(request):
    user_profile = UserProfile.objects.filter(user=request.user)[0]
    user_profile.is_tutor = True
    user_profile.save()
    # --- Probably should go somewhere else, this is just to write the code out ------
    locations_list = Location.objects.order_by('placeName')
    template = loader.get_template('login/locations.html')
    context = {'locations_list': locations_list,}
    return render(request, 'login/locations.html', context)
    # -------------------------------------------------------------------------
    # return render(request, 'login/classes.html')


def select_location(request):
    user_profile = UserProfile.objects.filter(user=request.user)[0]
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


def class_select_isTutee(request):
    return render(request, 'login/classes.html')


def authflowhandler(request):
    return render(request, 'login/is_tutor.html')    

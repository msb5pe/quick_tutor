""" V1: Login with Google works """

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout
from .models import UserProfile
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

def logout_success(request):
    logout(request)
    return redirect('login:index')

def index(request):
    #If the user is authenticated, then save user details and logins
    return render(request, 'login/index.html')

def create_user(request):
    return render(request, 'login/create_user.html')
    # return HttpResponse("This is where you would create your profile if your email doesn't exist on the server")

def is_tutor(request):
    return render(request, 'login/is_tutor.html')


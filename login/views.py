""" V1: Login with Google works """

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .models import UserProfile
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required


def login_success(request):
    #If user exists, then display details; otherwise, prompt to create new user
    try:
        user = request.user
        user = user.social_auth.get(provider='google')
        return render(request, 'login/existing_user.html')
    except:
        pass    
    return HttpResponseRedirect(reverse('login:create_user'), args=(request.user))

def logout_success(request):
    logout(request)
    return redirect('index')

def index(request):
    #If the user is authenticated, then save user details and redirect to success; otherwise, render login
    user = request.user
    if(user.is_authenticated()):
        print(user.email)
        print(user.name)
        redirect('success', request)
    return render(request, 'login/index.html')

def create_user(request):
    return render(request, 'login/create_user.html')
    # return HttpResponse("This is where you would create your profile if your email doesn't exist on the server")

def profile(request):
    return HttpResponse("This is your profile page")

@login_required
def edit_profile(request):
    print('here1')
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.userprofile, files=request.FILES) #??????????????????????????????? user.profile or user.userprofile
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        print('here2')
        return render(request, 'login/edit_profile.html', context) #???????????????????????????????????????

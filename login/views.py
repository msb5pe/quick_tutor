""" V1: Login with Google works """

from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .models import UserProfile, Location
import class_handler
from django.contrib.auth.forms import UserChangeForm
from .forms import EditProfileForm, EditUserForm

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
    context = {'is_tutor' : True}
    return render(request, 'login/dept.html', context)

def class_select_isTutee(request):
    user_profile = find_user(request.user)
    user_profile.is_tutor = False
    user_profile.save()
    context = {'is_tutor' : False}
    return render(request, 'login/dept.html', context)

def class_selector(request):
    locations_list = Location.objects.order_by('placeName')
    class_list = class_handler.call(request.POST.getlist('departments'))
    payload = {'classes': class_list, 'locations_list': locations_list, }
    return render(request,'login/classes.html', payload)


def home_redirect(request):
    user_profile = find_user(request.user)
    classes = request.POST.getlist('classes')
    location = request.POST.get('location') # original
    # location = Location.get(pk=request.POST['location'])
    cls_str = classes[0]
    for c in classes[1:]:
        cls_str = cls_str + "," + c
    user_profile.classes = cls_str
    user_profile.location = location
    user_profile.save()
    return redirect('home:index')

def authflowhandler(request):
    return render(request, 'login/is_tutor.html')
    # user_profile = find_user(request.user)
    # if user_profile.first_time_user:
    #     user_profile.first_time_user = False
    #     user_profile.save()
    #     return render(request, 'login/edit_profile.html')
    # else:
    #     return render(request, 'login/is_tutor.html')

# Not implemented
def authErrorHandler(request):
    return HttpResponse('Must be an @virginia.edu email')

def edit_profile(request):
    locations_list = Location.objects.order_by('placeName')
    if request.method == 'POST':
        user_form = EditUserForm(data=request.POST, instance=request.user)
        profile_form = EditProfileForm(data=request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/login/authflow/')

    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.userprofile)
        args = {'user_form': user_form, 'profile_form': profile_form, 'locations_list': locations_list,}
        return render(request, 'login/edit_profile.html', args)

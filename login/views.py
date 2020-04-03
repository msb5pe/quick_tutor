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

class IndexView(generic.TemplateView):
    template_name = 'login/index.html'
    context_object_name = 'UserProfile'

    def get_queryset(self, request):
        """Return the last five published questions."""
        print(request)
        return UserProfile.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]


def midflowhandler(request):
    return render(request, 'login/midflow.html')    

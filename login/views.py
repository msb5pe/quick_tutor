""" V1: Login with Google works """

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render


def login_success(request):
    return HttpResponse("You have successfully logged in")

def logout(request):
    return HttpResponse("You have successfully logged out")

def index(request):
    return render(request, 'login/index.html')

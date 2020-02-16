""" V1: Login with Google works """

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'login/index.html')

def login_success(request):
    return HttpResponse("You have successfully logged in")

def logout(request):
    return HttpResponse("You have successfully logged out")


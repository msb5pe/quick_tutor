from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'login/index.html')

def login_success(request):
    return HttpResponse("You have successfully logged in")
""" V1: Login with Google works """

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.login_success, name='login_success'),
    path('logout/', views.logout, name='logout')
]
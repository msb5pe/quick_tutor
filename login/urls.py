""" 
V1: Login with Google works 
V1.1: Refactored login to be server side. Made paths for social_django api.
    ** Logout doesn't work yet.
"""

from django.urls import path
from django.conf import settings

from . import views
from django.conf.urls import include
from django.contrib.auth import logout


urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('', views.index, name='index'),
    path('success/', views.logout_success, name='success'),
    path('logout/', views.logout_success, name='logout'),
    path('create_user/', views.create_user, name='create_user'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
]
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
    path('logout/', logout, {'': settings.LOGOUT_REDIRECT_URL},
    name='logout'),
    path('logout-success/', views.logout_success, name='logout-success')
]
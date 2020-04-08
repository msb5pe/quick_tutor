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

app_name = 'login'

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('', views.IndexView.as_view(), name='index'),
    path('logout/', views.logout_success, name='logout'),
    path('authflow/', views.authflowhandler, name='authflow'),
    path('tutor/', views.class_select_isTutor, name='tutor'),
    path('tutee/', views.class_select_isTutee, name='tutee'),
    path('selector/', views.class_selector, name='selector'),
    path('hrdirect', views.home_redirect, name='hrdirect'),
]
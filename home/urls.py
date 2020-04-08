from django.urls import path, include

from . import views

app_name = 'home'


urlpatterns = [
    # path('', include('social_django.urls', namespace='social')),
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
]
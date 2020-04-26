from django.urls import path, include

from . import views

app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('create_request/', views.create_request, name='create_request'),
    path('delete_request/', views.delete_request, name='delete_request')
]
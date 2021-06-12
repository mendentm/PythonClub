from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='view'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('newresource/', views.newResource, name='newresource'),
    path('newevent/', views.newEvent, name='newevent'),
]

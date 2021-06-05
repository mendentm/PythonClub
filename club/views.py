from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resources_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resources_list' : resources_list})

def meetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings_list' : meetings_list})

def meetingdetails(request, id):    
    meeting_details_view=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetails.html', {'meeting_details_view': meeting_details_view})
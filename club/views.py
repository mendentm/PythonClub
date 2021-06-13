from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, EventForm, ResourceForm
from django.contrib.auth.decorators import login_required
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

#forms 
@login_required
def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

@login_required
def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

@login_required
def newEvent(request):
    form=EventForm

    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'club/newevent.html', {'form': form})


# login view

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

# logout view

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')
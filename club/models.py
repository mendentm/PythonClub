from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    MeetingTitle=models.CharField(max_length=255)
    MeetingDate=models.DateField()
    MeetingTime=models.TimeField()
    MeetingLocation=models.CharField(max_length=255)
    MeetingAgenda=models.CharField(max_length=255)

    def __str__(self):
        return self.MeetingTitle

    class Meta:
        db_table='Meeting'

class MeetingMinutes(models.Model):
    MeetingId=models.ForeignKey(User, on_delete=models.CASCADE)
    MinutesText=models.TextField()
    Attendance=models.ManyToManyField(Meeting)

    def __str__(self):
        return self.MeetingId

    class Meta:
        db_table="Meeting Minutes"

class Resource(models.Model):
    ResourceName=models.CharField(max_length=255)
    ResourceType=models.CharField(max_length=255)
    UserId=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    DateEntered=models.DateField()
    ResourceUrl=models.URLField()
    Description=models.TextField()

    def __str__(self):
        return self.ResourceName

    class Meta:
        db_table='Resource'

class Event(models.Model):
    EventTitle=models.CharField(max_length=255)
    UserId=models.ForeignKey(User, on_delete=models.CASCADE)
    EventLocation=models.CharField(max_length=255)
    EventDate=models.DateField()
    EventTime=models.TimeField()
    EventDescription=models.CharField(max_length=255)

    def __str__(self):
        return self.EventTitle

    class Meta:
        db_table='Event'    

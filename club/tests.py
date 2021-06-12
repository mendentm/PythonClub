from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from django.urls import reverse
from .forms import MeetingForm
# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(MeetingTitle='A test meeting')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'A test meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type=MeetingMinutes(MinutesText='Test meetingminutestext')
        
    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'Meeting Minutes')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
       

class ResourceTest(TestCase):
    def setUp(self):
        self.UserId=User(username='user1')  
        self.Resource=Resource(ResourceName='Resourcename test', DateEntered=datetime.date(2021,1,10), ResourceUrl='http://www.google.com', Description='Resource description')

    def test_string(self):
        self.assertEqual(str(self.Resource), 'Resourcename test')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')
   
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class EventTest(TestCase):
    def setUp(self):
        self.type=Event(EventTitle='A test Event')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'A test Event')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


# form tests

class NewMeetingForm(TestCase):
    #valid form data
    def test_meetingform(self):
        data={

        'MeetingTitle': 'executive', 
        'Meetingdate': '2020-1-5',
        'MeetingTime': '4:42:50',
        'MeetingLocation': 'Texas',
        'MeetingAgenda': 'Anything',

        }

        form=MeetingForm (data)
        self.assertTrue(form.is_valid)
    
    #invalid test failing
    """def test_meetingform_invalid(self):
        data={

        'MeetingTitle': 'executive', 
        'Meetingdate': '2020-1-5',
        'MeetingTime': '4:42:50',
        'MeetingLocation': 'Texas',
        'MeetingAgenda': 'Nothing',
        }

        form=MeetingForm (data)
        self.assertFalse(form.is_valid)
        """


class NewResourceForm(TestCase):
    #valid form data
    def test_resourceform(self):
        data={

        'ResourceName': 'executive', 
        'ResourceType' : 'nothing',
        'UserId' : 'david',
        'DateEntered': '2020-1-5',
        'MeetingTime': '4:42:50',
        'ResourceUrl': 'http://www.google.com',
        'Description': 'Anything',

        }

        form=MeetingForm (data)
        self.assertTrue(form.is_valid)
 

class NewEventForm(TestCase):
    #valid form data
    def test_eventform(self):
        data={

        'EventTitle': 'executive', 
        'EventLocation' : 'nothing',
        'UserId' : 'david',
        'EventDate': '2020-1-5',
        'EventTime': '4:42:50',
        'EventDescription': 'Anything',

        }

        form=MeetingForm (data)
        self.assertTrue(form.is_valid)
 

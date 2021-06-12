from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from django.urls import reverse
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



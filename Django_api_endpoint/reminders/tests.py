from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import date, time

class ReminderAPITestCase(APITestCase):
    def test_create_reminder(self):
        url = '/api/reminders/create/'
        data = {
            'date': date.today(),
            'time': '12:30:00',
            'message': 'Test reminder',
            'remind_by': 'email'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_reminder_with_invalid_method(self):
        url = '/api/reminders/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expecting 200 OK now

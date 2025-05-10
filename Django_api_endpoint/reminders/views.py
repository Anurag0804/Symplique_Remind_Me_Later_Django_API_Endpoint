from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

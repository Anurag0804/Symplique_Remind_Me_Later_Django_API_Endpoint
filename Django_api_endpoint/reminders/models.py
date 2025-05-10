from django.db import models
from django.utils import timezone

class Reminder(models.Model):
    REMINDER_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    # Use timezone.now() to get the current date and time as default
    date = models.DateField(default=timezone.now)  # Ensures it's today's date or future date
    time = models.TimeField(default=timezone.now)
    message = models.TextField()
    remind_by = models.CharField(max_length=10, choices=REMINDER_CHOICES,null=True)

    def __str__(self):
        return f"{self.message} at {self.date} {self.time} via {self.remind_by}"

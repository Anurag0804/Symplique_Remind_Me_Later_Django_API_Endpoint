from django.urls import path
from .views import ReminderCreateView

urlpatterns = [
    path('create/', ReminderCreateView.as_view(), name='reminder-create'),
]

# tasks/views.py

from rest_framework import generics
from .serializer import MotivationalQuoteSerializer, ReminderSerializer
from .models import MotivationalQuote, Reminder

class ListMotivationalQuotes(generics.ListAPIView):
    queryset = MotivationalQuote.objects.all()
    serializer_class = MotivationalQuoteSerializer

class ListReminders(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

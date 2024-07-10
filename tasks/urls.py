from django.urls import path
from .views import *

urlpatterns = [
    path('quotes/', ListMotivationalQuotes.as_view()),
    path('reminders/', ListReminders.as_view()),
]

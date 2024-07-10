from rest_framework import serializers
from .models import MotivationalQuote, Reminder

class MotivationalQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivationalQuote
        fields = ('id', 'quote_text', 'author')

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'text')

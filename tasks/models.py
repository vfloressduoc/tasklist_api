from django.db import models

class MotivationalQuote(models.Model):
    quote_text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.quote_text

class Reminder(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

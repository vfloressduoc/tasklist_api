from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()


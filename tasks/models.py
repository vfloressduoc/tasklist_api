from django.db import models

# class Task(models.Model):
#     name = models.CharField(max_length=100, blank=False)
#     description = models.CharField(max_length=100)
#     is_completed = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     deadline = models.DateTimeField()

class ToDo(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(blank=False)
    is_completed = models.BooleanField(default=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # deadline = models.DateTimeField()

    def __str__(self):
        return self.name
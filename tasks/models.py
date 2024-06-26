from django.db import models

class ToDo(models.Model):
    itemName = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    itemDate = models.DateField(blank=False)
    itemPriority = models.CharField(max_length=50, blank=False)  # nuevo campo
    itemCategory = models.CharField(max_length=50, blank=False)  # nuevo campo
    completed = models.BooleanField(default=False)  # cambiar is_completed a completed

    def __str__(self):
        return self.itemName

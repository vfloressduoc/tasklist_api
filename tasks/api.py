from tasks.serializer import TaskSerializer
from .models import Task
from rest_framework import viewsets, permissions

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TaskSerializer
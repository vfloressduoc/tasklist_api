# from rest_framework import serializers
# from .models import Task

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'

from rest_framework import serializers
from .models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'name', 'description', 'date', 'is_completed')
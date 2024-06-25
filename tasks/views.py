from django.shortcuts import render
from rest_framework import generics
from .serializer import *
from .models import *

# Create your views here.
#CRUD


class ListTodo(generics.ListAPIView):       #leer/ver lista
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DetailTodo(generics.RetrieveUpdateAPIView):       #update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):       #crear
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):      #borrar
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer   


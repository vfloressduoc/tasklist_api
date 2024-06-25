# from django.contrib import admin
# from .models import Task

# admin.site.register(Task)
# class taskAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'is_completed', 'created_at', 'deadline')
#     list_filter = ('is_completed', 'created_at', 'deadline')
#     search_fields = ('name', 'description')

from django.contrib import admin
from .models import *

admin.site.register(ToDo)
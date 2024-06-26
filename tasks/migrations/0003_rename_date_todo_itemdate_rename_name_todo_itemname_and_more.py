# Generated by Django 5.0.6 on 2024-06-26 03:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_todo_delete_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date',
            new_name='itemDate',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='itemName',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='is_completed',
        ),
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='itemCategory',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='itemPriority',
            field=models.CharField(default='normal', max_length=50),
            preserve_default=False,
        ),
    ]
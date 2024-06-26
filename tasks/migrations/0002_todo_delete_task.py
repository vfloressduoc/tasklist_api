# Generated by Django 5.0.6 on 2024-06-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('is_completed', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]

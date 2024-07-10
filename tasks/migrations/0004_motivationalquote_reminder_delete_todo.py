# Generated by Django 5.0.6 on 2024-07-10 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_date_todo_itemdate_rename_name_todo_itemname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivationalQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', models.TextField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ToDo',
        ),
    ]
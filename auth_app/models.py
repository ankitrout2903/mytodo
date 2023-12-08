from django.db import models

# Create your models here.

# todo_app/models.py
from django.db import models

class Todo(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ('OPEN', 'Open'),
            ('WORKING', 'Working'),
            ('DONE', 'Done'),
            ('OVERDUE', 'Overdue'),
        ],
        default='OPEN',
    )

class Tag(models.Model):
    value = models.CharField(max_length=100, unique=True)

from django.db import models

# Create your models here.
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

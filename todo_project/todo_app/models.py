# Create your models here.
from django.db import models
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.title

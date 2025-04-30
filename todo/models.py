from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.task_name
    userID = models.IntegerField()
    task_name = models.CharField(max_length = 200)
    priority = models.IntegerField(default = 0)
    dueDate = models.DateField("Due date")
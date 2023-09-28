from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    due_date = models.DateTimeField(blank=True)
    assignee = models.CharField(max_length=1024)
    created_by = models.CharField(max_length=1024)
    creation_time = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=128)
    creation_time = models.DateTimeField(auto_now_add=True)
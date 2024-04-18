from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskStage(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Label(models.Model):
    label = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.label
    
    

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cover = models.URLField(max_length=200, null=True)
    labels = models.ManyToManyField(Label, related_name='labels')
    due_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        help_text="Enter a due date in the future.",
        null=True,
    )
    task_stage = models.ForeignKey(TaskStage, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True, null = True)
    assigned_to = models.ManyToManyField(User, related_name='assigned_to')
    assigned_by = models.ForeignKey(User, related_name = 'assigned_by', default='None', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    


    


class Attachment(models.Model):
    name = models.CharField(max_length=50)
    src = models.URLField(max_length=200)
    size = models.CharField(max_length=50)
    task = models.ForeignKey(Task, related_name='attachment', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    name = models.CharField(max_length=50)
    src = models.URLField(max_length=200)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    task = models.ForeignKey(Task, related_name='comment', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

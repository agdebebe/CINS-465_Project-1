from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=20)
    entry = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

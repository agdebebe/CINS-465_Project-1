from django.db import models
from django import forms

# Create your models here.



class Task(models.Model):
    description = models.CharField(max_length=20)
    CATAGORY_CHOICES = (
    ('A', 'Home'),
    ('B', 'School'),
    ('C', 'Work'),
    ('D', 'Self-Improvment'),
    ('E', 'Other'),
    )

    TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
    )

    catagory = models.CharField(max_length=8, choices=CATAGORY_CHOICES)
    completed = models.CharField(max_length=8, choices = TRUE_FALSE_CHOICES, default='No')

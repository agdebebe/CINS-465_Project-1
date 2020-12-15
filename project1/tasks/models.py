from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # tasks_view_hide_completed = models.BooleanField(blank = False, label = 'tasks_view_hide_completed', widget=forms.CheckboxInput(attrs={'onclick': 'this.form.submit()'}))
      # external = forms.BooleanField(label=_('External link'), required=False)
    description = models.CharField(max_length=20)
    CATAGORY_CHOICES = (
    ('A', 'Home'),
    ('B', 'School'),
    ('C', 'Work'),
    ('D', 'Self-Improvment'),
    ('E', 'Other'),
    )

    TRUE_FALSE_CHOICES = (
    ('True', 'Yes'),
    ('False', 'No')
    )

    catagory = models.CharField(max_length=8, choices=CATAGORY_CHOICES)
    completed = models.CharField(max_length=8, choices = TRUE_FALSE_CHOICES, default='No')

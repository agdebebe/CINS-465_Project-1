from django import forms
from tasks.models import Task
from django.forms import ModelForm



class ADD_TASKFORM(ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'catagory')

class EDIT_TASKFORM(ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'catagory')

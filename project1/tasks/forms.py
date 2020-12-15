from django import forms
from tasks.models import Task
from django.forms import ModelForm
from core.models import UserProfile



class ADD_TASKFORM(ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'catagory')

class EDIT_TASKFORM(ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'catagory')

class SHOW_HIDE(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('tasks_view_hide_completed',)

from django import forms
from budget.models import Budget
from django.forms import ModelForm



class ADD_BUDGETFORM(ModelForm):
    class Meta:
        model = Budget
        fields = ('description', 'catagory', 'projected', 'actual')

class EDIT_BUDGETFORM(ModelForm):
    class Meta:
        model = Budget
        fields = ('description', 'catagory', 'projected', 'actual')

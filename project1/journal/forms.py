from django import forms
from journal.models import Journal
from django.forms import ModelForm



class ADD_JOURNALFORM(ModelForm):
    class Meta:
        model = Journal
        fields = ('description', 'entry')


class EDIT_JOURNALFORM(ModelForm):
    class Meta:
        model = Journal
        fields = ('description', 'entry')

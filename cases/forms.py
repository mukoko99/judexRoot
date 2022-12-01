from dataclasses import fields
import email
from pyexpat import model
import re
from django import forms 
from django.forms import ModelForm
from .models import Case, Defendant, Judge
options = (
    ('1', 'OPEN'),
    ('2', 'INACTIVE'),
    ('3', 'CLOSED'),
    ('4', 'REOPENED',)
)
class CaseForm(ModelForm):
    status = forms.MultipleChoiceField(choices=options, widget=forms.Select)
    class Meta:
        model = Case
        fields = ['defendant', 'judge', 'charge']

class DefendantForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=32, required=False)
    lastName = forms.CharField(label='Last Name', required=True, max_length=32)
    age = forms.IntegerField(label='Age', required=False)
    gender = forms.CharField(label='Gender', max_length=1)
    race = forms.CharField(label='Race', required=False)
    #class Meta:
        #model = Defendant
        #fields = '__all__'

class JudgeForm(ModelForm):
    class Meta:
        model = Judge
        fields = ['lastName', 'firstName', 'gender']
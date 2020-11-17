from django import forms
from django.forms import ModelForm
from .models import *

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'
        
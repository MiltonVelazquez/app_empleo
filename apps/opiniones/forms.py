from django import forms
from .models import *

class OpinionForm(forms.ModelForm):
    
    class Meta:
        model = Opinion
        fields = ['texto']
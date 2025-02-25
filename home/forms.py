# home/forms.py
from django import forms
from .models import contactus



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = contactus  # Make sure this matches the model name
        fields = ['name', 'email', 'number', 'project', 'query_description', 'datetime']

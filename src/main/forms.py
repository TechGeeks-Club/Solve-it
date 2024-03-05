from django import forms
from . import models
from django.contrib.auth.models import User
import re
from .validation import validateName

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if not username or not password:
            raise forms.ValidationError('Username and password are required')
    
        if not validateName(username):
            raise forms.ValidationError('Invalid username')
        
        return cleaned_data
    
class Participant(forms.ModelForm):
    class Meta:
        model = models.Participant
        fields = ['user', 'team']


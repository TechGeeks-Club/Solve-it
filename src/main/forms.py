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

class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = ['name', 'Pid', 'pin']
    
    
class QuetionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ["question_title",'question_text', 'points', 'template', 'level']

class QuestionLevelForm(forms.ModelForm):
    class Meta:
        model = models.QuestionLevel
        fields = ['level']
        
class TestFrom(forms.ModelForm):
    class Meta:
        model = models.Test
        fields = ['input', 'output', 'question']
    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['question', 'team', 'answer']
class AnswerResaultForm(forms.ModelForm):
    class Meta:
        model = models.AnswerResault
        fields = ['answer', 'success', 'points']


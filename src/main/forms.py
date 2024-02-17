from django import forms
from . import models



class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = ['name', 'Pid', 'pin']
    
    
class QuetionsForm(forms.ModelForm):
    class Meta:
        model = models.Quetions
        fields = ['question', 'pointes', 'template', 'level']


class LevelsForm(forms.ModelForm):
    class Meta:
        model = models.Levels
        fields = ['name']
        
class TestsFrom(forms.ModelForm):
    class Meta:
        model = models.Tests
        fields = ['inp', 'exp_res', 'Qid']
    
class ResponsesForm(forms.ModelForm):
    class Meta:
        model = models.Responses
        fields = ['Qid', 'Tid', 'file_path']


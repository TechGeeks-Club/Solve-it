from django import forms
from . import models

class Participant(forms.ModelForm):
    class Meta:
        model = models.Participant
        fields = ['user', 'Tid']

class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = ['name', 'Pid', 'pin']
    
    
class QuetionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['question', 'pointes', 'template', 'level']

class QuestionLevelForm(forms.ModelForm):
    class Meta:
        model = models.QuestionLevel
        fields = ['level']
        
class TestFrom(forms.ModelForm):
    class Meta:
        model = models.Test
        fields = ['inp', 'exp_res', 'Qid']
    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['question', 'team', 'answer']
class AnswerResaultForm(forms.ModelForm):
    class Meta:
        model = models.Responses
        fields = ['Qid', 'Tid', 'file_path']


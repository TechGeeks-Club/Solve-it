from django import forms
from main.models import Answer
# from .models import ExerciseFile

# class CustomExerciseFileForm(forms.ModelForm):
#     class Meta:
#         model = ExerciseFile
#         fields = ['title', 'level', 'file', 'text']

#     def clean_file(self):
#         file = self.cleaned_data.get('file')

#         # Perform validations on the content of the file
#         if file:
#             content = file.read().decode('utf-8')

#             # Add your custom validations here
#             if "invalid_pattern" in content:
#                 raise forms.ValidationError("The file contains invalid content.")

#         return file

class AnswerFileForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        
        
        
        
'''
# answers/forms.py
from django import forms
from .models import Answer

class AnswerFileForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']

# answers/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnswerFileForm
from .models import Answer, Question, Participant

def upload_answer(request, question_id, participant_id):
    question = get_object_or_404(Question, pk=question_id)
    participant = get_object_or_404(Participant, pk=participant_id)

    if request.method == 'POST':
        form = AnswerFileForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.participant = participant
            answer.save()
            return redirect('success_page')  # Redirect to success page or any other view
    else:
        form = AnswerFileForm()

    return render(request, 'answers/upload_answer.html', {'form': form})
'''
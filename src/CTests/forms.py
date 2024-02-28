from django import forms
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
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import UserForm

def first_page(request):
    return HttpResponse("<h1>first page </h1>")

# def submit_form(request):
#     if request.method == 'POST':
#         # If the form is submitted via POST request, process the form data
#         form = UserForm(request.POST)
#         if form.is_valid():
#             # If the form data is valid, perform any necessary actions
#             # For example, you might save the data to the database
#             form.save()
#             # After processing the form, you can redirect the user to a different page
#             return redirect('success_page')  # Redirect to a success page
#     else:
#         # If the form is not submitted via POST request, create a new instance of the form
#         form = UserForm()
#     # Render the form template with the form instance
#     return render(request, 'form_template.html', {'form': form})
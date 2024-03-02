from django.shortcuts import render

from .forms import AnswerFileForm
def index(request):
    return render(request, "test.html")

def upload(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
        form = AnswerFileForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.participant = user.participant
            
            
            answer.save()
            return render(request, "success.html")
        
    else:
        form = AnswerFileForm()
        return render(request, "test.html", {'form': form})
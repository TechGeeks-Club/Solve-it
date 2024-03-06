from django.shortcuts import render
from django.http import JsonResponse

from .forms import AnswerFileForm
from main.models import Question
# def index(request):
#     return render(request, "test.html")

def index(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
        form = AnswerFileForm(request.POST, request.FILES)
        question = Question.objects.filter(id=request.POST["questionId"])
        
        if not question.exists():
            return JsonResponse({"error":"Question not found"},status=400)
        question = question.first()
        
        if form.is_valid():
            answer = form.save(commit=False)
            answer.participant = user.participant
            answer.question = question
            answer.save()
            
            
            
            answer.save()
            return render(request, "success.html")
        
    elif request.method == "GET":
        # load the questions with the status
        form = AnswerFileForm()
        questions = Question.objects.filter(is_active=True)
        return render(request, "test.html", context={'form': form,"questions":questions})
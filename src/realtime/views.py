from django.shortcuts import render

from main.models import Question
from main.forms import AnswerFileForm

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    print("room_name", room_name)
    # return render(request, "chat/room.html", {"room_name": room_name})
    qustions = Question.objects.filter(is_active=True)
    form = AnswerFileForm()
    return render(request, "test.html", {"from":form,"room_name": room_name,"questions":qustions})

# l
def leaderboard(request):
    return render(request, "chat/lb.html")
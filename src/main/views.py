from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .forms import UserForm

from .validation import validateName,validatePin
from .models import Team,Participant

import random

def team_members_num(team_id):
    # team = Team.objects.get(name=request.POST['name'])
    num  = int(Participant.objects.filter(team_id=team_id).count())
    print(num)
    return num

def first_page(request):
    return HttpResponse("<h1>first page </h1>")


def login_view(request):
    if request.method == 'GET':
        return render(request, 'singup.html')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse("<h1>Login success</h1>",status=200)
        
        return HttpResponse("<h1>login error</h1>",status=401)
    
    raise  Http404()


def singup_view(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'singup.html', {'form': form})
        
    if request.method == 'POST':
        # form = UserForm(request.POST)
        unv = validateName(request.POST['username'])
        if not unv :
            if validatePin(request.POST['password']):
                newUser = User(username=request.POST['username'])
                newUser.set_password(raw_password=request.POST['password'])
                newUser.save()
                Participant(user=newUser).save()

                return HttpResponse("<h1>singup success</h1>",status=201)
            else:
                return HttpResponse("<h1>invalid password</h1>",status=400)
        
        elif unv == 1:
            return HttpResponse("<h1>invalid username</h1>",status=400)    
        elif unv == 2:
            return HttpResponse("<h1>username already exists</h1>",status=400)  
    raise  Http404()

@login_required
def create_team(request):
    if request.method == 'GET':
        
        if Team.objects.filter(participant__user_id=request.user.id).exists():
            return HttpResponse("<h1>you are already in a team</h1>",status=400)

        return render(request, 'singup.html')
        
    if request.method == 'POST':
            
        if not validateName(request.POST['name']):
            return HttpResponse("<h1>invalid name</h1>",status=400)
        
        if Team.objects.filter(name=request.POST['name']).exists(): 
            return HttpResponse("<h1>pin already exist</h1>",status=400)
        
        
        pin = random.randint(100000,999999)
        team = Team.objects.create(name=request.POST['name'],pin=str(pin))
        
        participant = Participant.objects.get(user_id=request.user.id)
        participant.team = team
        participant.save()
        return HttpResponse(f"<h1>team created | your pin is {pin}</h1>",status=201)

    raise  Http404()    

@login_required
def join_team(request):
    if request.method == 'GET':      
        if Team.objects.filter(participant__user_id=request.user.id).exists():
            return HttpResponse("<h1>you are already in a team</h1>",status=400)
        
        return render(request, 'singup.html')

    
    if request.method == 'POST':
        try:
            team = Team.objects.get(name=request.POST['name'])
        except:
            return HttpResponse("<h1>team not found</h1>",status=404)
        
        if team.pin == request.POST['password']:    
            if team_members_num(team.id) < 3:
                user = request.user.id
                participent = Participant.objects.get(user_id=user)
                participent.team = team 
                participent.save()
                return HttpResponse("<h1>team joined</h1>",status=200)
            else:
                return HttpResponse("<h1>team is full<h1>")
        else:
            return HttpResponse("<h1>a wrong password</h1>",status=400)
    
        
    raise Http404()

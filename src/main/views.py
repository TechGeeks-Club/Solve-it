from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .forms import UserForm

from .validation import validateName
from .models import Team,Participant

import random
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
        form = UserForm(request.POST)
        if form.is_valid():
            newUser = User(username=form.data["username"])
            newUser.set_password(raw_password=form.data["password"])
            newUser.save()
            Participant(user=newUser).save()
            
            return HttpResponse("<h1>singup success</h1>",status=201)
        
        return HttpResponse("<h1>singup error</h1>",status=400)
    
    raise  Http404()

@login_required
def create_team(request):
    if request.method == 'GET':
        try:
            part = Participant.objects.get(user_id=request.user.id)
            if part.team:
                return HttpResponse("<h1>you are already in a team</h1>",status=400)
        except:
            pass
        return render(request, 'singup.html')
        
    if request.method == 'POST':
        
            
        if validateName(request.POST['name']):
            try:
                team = Team.objects.get(name=request.POST['name'])
                return HttpResponse("<h1>team already exist</h1>",status=400)
            except:
                pass
            pin = random.randint(1000,999999)
            team = Team.objects.create(name=request.POST['name'],pin=int(pin))
            print(f"============={team}======{team.id}==============")
            user_id = request.user.id
            print(f"============={user_id}==============")
            participant = Participant.objects.get(user_id=user_id)
            print(f"============={participant}==============")
            participant.team = team
            participant.save()
        return HttpResponse(f"<h1>team created | your pin is {pin}</h1>",status=201)
    raise  Http404()    

@login_required
def join_team(request):
    if request.method == 'GET':
        try:
            part = Participant.objects.get(user_id=request.user.id)
            if part.team:
                return HttpResponse("<h1>you are already in a team</h1>",status=400)
        except:
            pass
        return render(request, 'singup.html')
    
    if request.method == 'POST':
        try:
            team = Team.objects.get(name=request.POST['name'])
            user = request.user.id
            participent = Participant.objects.get(user_id=user)
            participent.team = team 
            participent.save()
            return HttpResponse("<h1>team joined</h1>",status=200)
        except:
            return HttpResponse("<h1>team not found</h1>",status=404)
    raise  Http404()
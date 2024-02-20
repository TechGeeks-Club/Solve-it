from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import Http404
from .forms import UserForm

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
            
            return HttpResponse("<h1>singup success</h1>",status=201)
        
        return HttpResponse("<h1>singup error</h1>",status=400)
    
    raise  Http404()
    

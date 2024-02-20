from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.base_user import make_password
from django.contrib.auth import authenticate,login

from .forms import UserForm
from . import validation

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
        else:
            return HttpResponse("<h1>login error</h1>",status=400)
    else:
        pass


def singup_view(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'singup.html', {'form': form})
        
    if request.method == 'POST':
        form = UserForm(request.POST)
        # print(str(form.data["password"]))
        
        if validation.check_username(form.data["username"])  and validation.check_outher(form) :
            # frm = form.save()
            pss = make_password(form.data["password"])
            print(pss,print(form.data["password"]))
            user = User.objects.create_user(username=form.data["username"],password=pss)
            # uUser = User.objects.get(username=form.data["username"]).set_password(raw_password=form.data["password"])
            #print green text
            
            # return redirect('success_page.html')
            return HttpResponse("<h1>singup success</h1>",status=201)
        else:
            return HttpResponse("<h1>singup error</h1>",status=400)
    else:
        pass
    

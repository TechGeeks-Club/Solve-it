#this file contains auth,sighnup,login,logout,etc

from .models import  Team
from django.contrib.auth.models import User
import re



def check_username(username):

    ptt = "^[a-zA-Z]([a-zA-Z0-9._-]+){2,20}$" #allow only a-z,A-Z,0-9,.,_,-
    user = User.objects.filter(username=username)
    
    if re.search(ptt,username) and not user.exists():
        return 1
    return 0

def check_pin(pin):
    ptt = "^[0-9]{4,6}$" 
    if re.search(ptt,pin):
        return 1
    return 0

def check_team_name(team):
    ptt = "^[a-zA-Z]([a-zA-Z0-9._-]+){2,20}$" #allow only a-z,A-Z,0-9,.,_,- 
    team = Team.objects.filter(name=team)
    if re.search(ptt,team) and not team.exists():
        return 1
    return 0 

def check_outher(form):
    try:
        if  form.data["email"]:
            ptt = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$" 
            if not re.search(ptt,form.data["email"]):
                return 0
    except:
        pass
    try:
        if form.data["first_name"]:
            ptt = "^[a-zA-Z]{2,20}$"
            if not re.search(ptt,form.data["first_name"]):
                return 0
    except:
        pass
    try:    
        if form.data["last_name"]: 
            ptt = "^[a-zA-Z]{2,20}$"
            if not re.search(ptt,form.data["last_name"]):
                return 0
    except:
        pass
    
    return 1
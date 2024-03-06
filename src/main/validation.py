#this file contains auth,sighnup,login,logout,etc

from .models import Participant
from django.contrib.auth.models import User
import re

def validateName(name) -> bool:
    namePattern = "^[a-zA-Z]([a-zA-Z0-9._-]+){2,20}$"
    if isinstance(name, str) and re.match(namePattern, name) is not None:
        return True
    return False

def validateUserName(name) -> bool : #is a reverse function treu == 0 false == 1
    namePattern = "^[a-zA-Z]([a-zA-Z0-9._-]+){2,20}$"
    if not User.objects.filter(username=name).exists():
        if re.match(namePattern, name) :
            return 0
        else:
            return 1 #invalid name
    else:
        return 2 #user already exists

def validatePin(pin): 
    ptt = "^[0-9]{4,6}$" 
    if re.match(ptt,pin):
        return 1
    return 0

def team_members_num(team_id):
    num  = int(Participant.objects.filter(team_id=team_id).count())
    return num

# ! not used
# def check_outher(form):
#     try:
#         if  form.data["email"]:
#             ptt = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$" 
#             if not re.search(ptt,form.data["email"]):
#                 return 0
#     except:
#         pass
#     try:
#         if form.data["first_name"]:
#             ptt = "^[a-zA-Z]{2,20}$"
#             if not re.search(ptt,form.data["first_name"]):
#                 return 0
#     except:
#         pass
#     try:    
#         if form.data["last_name"]: 
#             ptt = "^[a-zA-Z]{2,20}$"
#             if not re.search(ptt,form.data["last_name"]):
#                 return 0
#     except:
#         pass
    
#     return 1
from django.contrib import admin
from django.urls import path,include
from .views import first_page,singup_view,login_view,create_team,join_team

urlpatterns = [
    path('', first_page),
    path('login/', login_view),
    path('signup/', singup_view),
    path('team/create', create_team),
    path('team/join', join_team),
]

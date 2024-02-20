from django.contrib import admin
from django.urls import path,include
from .views import singup_view,login_view

urlpatterns = [
    path('login/', login_view),
    path('singup/', singup_view),
]

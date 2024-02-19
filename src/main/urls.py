from django.contrib import admin
from django.urls import path,include
from .views import first_page

urlpatterns = [
    # path('singup/', submit_form),
    path('', first_page),
]

from django.urls import path

from . import views


urlpatterns = [
    path("team/", views.index, name="index"),
    path("team/<str:room_name>/", views.room, name="room"),
    path("lb/", views.leaderboard, name="leaderboard"),
]
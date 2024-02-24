# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.TeamConsumer.as_asgi()),
    re_path(r"ws/competition/$", consumers.CompetitionConsumer.as_asgi()),
]
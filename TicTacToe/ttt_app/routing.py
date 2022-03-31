from django.urls import path, re_path
from .consumer import GameRoom


ws_urlpatterns = [
    #re_path("ws/game/<room_code>", GameRoom.as_asgi()),
     path('ws/game/<room_code>' , GameRoom.as_asgi())

]
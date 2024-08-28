from django.urls import path

from chess_app import consumers

websocket_urlpatterns = [
    path('ws/game/<int:game_id>/', consumers.GameConsumer.as_asgi())
]

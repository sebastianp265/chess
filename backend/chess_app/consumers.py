import json

from channels.generic.websocket import WebsocketConsumer
from django.contrib.gis.geometry import json_regex


class ChessGameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        move = text_data_json['move']

        self.send(text_data=json_regex.dumps({'move': move}))

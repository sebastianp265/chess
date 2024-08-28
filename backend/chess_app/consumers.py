import json

from channels.generic.websocket import AsyncWebsocketConsumer


class GameConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.game_id = None
        self.game_group_id = None

    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_group_id = f'game_{self.game_id}'

        await self.channel_layer.group_add(self.game_group_id, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.game_group_id, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        move = text_data_json['move']

        await self.channel_layer.group_send(
            self.game_group_id,
            {'type': 'receive.move', 'move': move}
        )

    async def receive_move(self, event):
        move = event['move']

        await self.send(text_data=json.dumps({'move': move}))

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EmissionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.space = self.scope['url_route']['kwargs']['space']
        self.group_space = f'group_{self.space}'

        await self.channel_layer.group_add(
            self.group_space,
            self.channel_name
        )

        await self.accept()
        
        await self.channel_layer.group_send(
            self.group_space,
            {'type': 'connection_established', 'message': 'WS connection established!'}
        )


    async def connection_established(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({'message': message}))


    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.group_space,
            self.channel_name
        )

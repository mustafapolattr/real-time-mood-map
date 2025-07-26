import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MoodConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "mood_updates"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # Mesajı doğrudan yayın yapıyoruz. Buraya istersen filtre/validate ekleyebilirsin.
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "broadcast_message",
                "message": text_data,
            }
        )

    async def broadcast_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            "message": message
        }))

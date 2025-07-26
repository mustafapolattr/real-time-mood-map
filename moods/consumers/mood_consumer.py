import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MoodConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "moods"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get("message", "")
            await self.send(text_data=json.dumps({
                "message": message
            }))
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                "error": "Geçersiz veri formatı."
            }))

    # Receive message from room group
    async def send_mood(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))

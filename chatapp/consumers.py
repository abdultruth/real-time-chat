import json


from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


from django.contrib.auth import get_user_model


from .models import Chat, Room



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        #join room group
        await self.channel_layer.group_add (self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        #leave room group
        await self.channel_layer.group_discard (self.room_group_name, self.channel_name)
        #await self.disconnect(close_code)

    # Receive message from Websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        request_user = text_data_json['request_user']
        sender = await self.get_user(request_user)
        room = await self.get_room(self.room_name)


        await self.save_chat(message=message, sender=sender, room=room)

        # Sending message to room group
        await self.channel_layer.group_send (self.room_group_name,                     
                        {
                            "type": "chat.message", 
                            "message": message, 
                            "request-user": request_user
                        }
                        
        )

        

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        request_user = event["request-user"]


        # Sending message to WebSocket
        await self.send(text_data=json.dumps(
            {
                "message": message,
                "request_user": request_user
            }
          )
        )

    @database_sync_to_async
    def get_user(self, username):
        return get_user_model().objects.filter(username=username).first()
    
    @database_sync_to_async
    def get_room(self, room_name):
        return Room.objects.filter(name=room_name).first()

    
    @database_sync_to_async
    def save_chat(self, message, sender, room):
        Chat.objects.create(user=sender, message=message, room=room)
        

    
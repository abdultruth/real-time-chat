import json


from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"

#         #join room group
#         async_to_sync(self.channel_layer.group_add) (
#             self.room_group_name, self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         #leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )

#     # Receive message from Websocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Sending message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event["message"]

#         # Sending message to WebSocket
#         self.send(text_data=json.dumps({"message": message}))



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

    # Receive message from Websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Sending message to room group
        await self.channel_layer.group_send (self.room_group_name, {"type": "chat.message", "message": message})

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Sending message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
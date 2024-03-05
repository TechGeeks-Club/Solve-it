# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from src.settings import C9N_L8D_ROOM,C9N_TEAM_B7T


# only one room for start/end the game and deisplay the leaderboad
class CompetitionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # if not self.scope["user"].is_staff:
        #     await self.close()
        #     return
        
        print("connected to room: ", C9N_L8D_ROOM)
        # Join room group
        await self.channel_layer.group_add(
            C9N_L8D_ROOM, self.channel_name
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            C9N_L8D_ROOM, self.channel_name
        )
        await self.close()
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("recive handler: ", message)
        
        await self.channel_layer.group_send(
            C9N_L8D_ROOM, {"type": "start_game", "message": message}
        )
    
        
    async def start_game(self, event):
        message = event["start_game"]
        # TODO: some logic
        
        await self.send(text_data=json.dumps({"message": "start_game"}))
        await self.channel_layer.group_send(
            C9N_TEAM_B7T,  # Send to the broadcast group
            {"type": "start_game", "message": "Game started!"}
        )
        
    async def end_game(self, event):
        message = event["end_game"]
        # TODO: some logic
        await self.send(text_data=json.dumps({"message": "end_game"}))

        
    

class TeamConsumer(AsyncWebsocketConsumer):
    # every user in any room will be in the broadcast group
    groups = [C9N_TEAM_B7T] 
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        
        
        print("connected to room: ", self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )
        # await self.close()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("recive handler: ")
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )
       
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        print("chat_message handler: ")
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
        
    async def start_game(self, event):
        message = event["message"]
        print("start_game handler: ")
        await self.send(text_data=json.dumps({"message": message}))
        
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from .utils import get_cookies

connected_users={}

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.lobby_name=self.scope["url_route"]["kwargs"]["lobby_id"]
        self.lobby_group_name=f"lobby_{self.lobby_name}"


        await self.accept()
        await self.channel_layer.group_add(self.lobby_group_name,self.channel_name)

        cookies=get_cookies(self.scope)
        self.chat_guestname=cookies.get("chat_guestname", "Anonymous")
        self.client_ip=self.scope['client'][0]
        connected_users.setdefault(self.lobby_name, set()).add((self.chat_guestname, self.client_ip))
        print(connected_users)
        await self.send(text_data=json.dumps({
            "type":"users_update",
            **{lobby:list(users)for lobby, users in connected_users.items()}
            }))        
            


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.lobby_group_name,{
            "type":"chat_message",
            "message": message
            })



    async def chat_message(self,event):
        message=event["message"]
        await self.send(text_data=json.dumps({"message": message}))



    async def disconnect(self,close_code):
        if self.lobby_name in connected_users:
            connected_users[self.lobby_name].discard((self.chat_guestname, self.client_ip))
            if not connected_users[self.lobby_name]:
                del connected_users[self.lobby_name]

        await self.chann

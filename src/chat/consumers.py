import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        chat_mate = self.scope["url_route"]["kwargs"]["username"]
        me = self.scope["user"]
        print(chat_mate, me)
        # await asyncio.sleep(5)
        # await self.send({
        #     "type": "websocket.close"
        # })

    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
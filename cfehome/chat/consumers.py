# c.f. views ("somewhere where a websocket communicates with channels")

import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({  # send response to websocket (wait for it to finish)
            "type": "websocket.accept"
        })

        # await asyncio.sleep(10)
        await self.send({
            "type": "websocket.send",
            "text": "Hello from Server"
        })

    async def websocket_recieve(self, event):
        # when a message is recieved from the websocket
        print("recieve", event)

    async def websocket_disconnect(self, event):
        # when the socket connects
        print("disconnected", event)

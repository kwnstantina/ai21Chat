from fastapi import APIRouter, WebSocket
from ai21 import AsyncAI21Client
import os
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()
token = os.environ.get("api-token")
client = AsyncAI21Client(api_key=token)

@router.websocket("/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        response = await process_message(message)
        await websocket.send_text(response)
        
async def process_message(message):
    response = await client.chat.completions.create(
        messages=message,
        model="jamba-1.5-large"
    )
    return response
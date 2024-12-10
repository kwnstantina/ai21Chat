# from pydantic import BaseModel
# from typing import List
# from fastapi import FastAPI, WebSocket
# from fastapi.responses import JSONResponse
# import os
# from ai21 import AsyncAI21Client
# from ai21.models.chat import ChatMessage, ResponseFormat, DocumentSchema, FunctionToolDefinition, ToolDefinition, ToolParameters
# from dotenv import load_dotenv

# load_dotenv()


# token = os.environ.get("api-token")

# class Message(BaseModel):
#     participant: str
#     message: str

# class ChatPayload(BaseModel):
#     participants: List[str]
#     messages: List[Message]
    
    
# class ChatMessage(BaseModel):
#     role: str
#     content: str

# class ToolParameters(BaseModel):
#     type: str
#     properties: dict
#     required: List[str]

# class FunctionToolDefinition(BaseModel):
#     name: str
#     description: str
#     parameters: ToolParameters

# class ToolDefinition(BaseModel):
#     type: str
#     function: FunctionToolDefinition
# app = FastAPI(
#     title="AI21 Chat API",
#     description="A simple API to interact with the AI21 Chat API",
#     version="0.1",
#     swagger_ui_parameters={"defaultModelsExpandDepth": -1} 
# )

# client = AsyncAI21Client(api_key=token)

# @app.get("/get-message")
# async def read_root():  
#     system = "You're a general , who help  users with their problems and conflicts in their releshionships, based on th interest-based relational approach threory"
#     messages = [
#      ChatMessage(content=system, role="system"),
#      ChatMessage(content="Hello, my boss friend says that I am silly and I feel sad, what could I do to feel better", role="user"),]
    
#     response = await client.chat.completions.create(
# 		model="jamba-1.5-large",
# 		messages=messages,
# 		documents=[],
# 		tools=[],
# 		n=1,
# 		max_tokens=2048,
# 		temperature=0.4,
# 		top_p=1,
# 		stop=[],
# 		response_format=ResponseFormat(type="text"),)
    
#     data={
#         "id": response.id,
# 		"message": response.choices[0].message.content,
# 		"role": response.choices[0].message.role,
# 	}


#     return data;


# @app.websocket("/chat")
# async def chat_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         message = await websocket.receive_text()
#         response = await process_message(message)
#         await websocket.send_text(response)
        
        
# async def process_message(message):
#     response = await client.chat.completions.create(
#         messages=message,
#         model="jamba-1.5-large",
#     )

#     return response



# @app.post("/chat")
# async def chat_endpoint(payload: ChatPayload):
#     participants = payload.participants
#     messages = payload.messages
#     data = []
    
#     system = "You are an expert in sports psychology, helping users resolve conflicts related to sports."
#     assistant = "Hello, I am here to help you resolve your conflict about sports. How can I assist you today?"
    
#     chatMessages = [
#         ChatMessage(role="system", content=system),
#         ChatMessage(role="assistant", content=assistant),
#     ]
    
#     for message in messages:
#         chatMessages.append(ChatMessage(role="user", content=message.message))
    
#     response = await client.chat.completions.create(
#         model="jamba-1.5-large",
#         messages=chatMessages,
#         stream=True,
#         max_tokens=150,
#         temperature=0.8,
#         top_p=1,
#         tools=[
#             ToolDefinition(
#                 type="function",
#                 function=FunctionToolDefinition(
#                     name="web_search",
#                     description="Perform a web search and return relevant results",
#                     parameters=ToolParameters(
#                         type="object",
#                         properties={
#                             "query": {"type": "string", "description": "The search query"},
#                             "num_results": {"type": "integer", "description": "The number of search results to return", "default": 5}
#                         },
#                         required=["query"]
#                     )
#                 )
#             )
#         ],
#         n=1,
#         stop=["\n"]
#     )
    
#     async for chunk in response:
#         data.append(chunk.choices[0].delta.content)
    
#     return JSONResponse(content={"participants": participants, "messages": messages, "data": data}, status_code=200)


from routes import chat, websocket,message
from typing import List
from fastapi import FastAPI
import os


app = FastAPI(
    title="AI21 Chat API",
    description="A simple API to interact with the AI21 Chat API",
    version="0.1",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1} 
)

app.include_router(chat.router)
app.include_router(websocket.router)
app.include_router(message.router)

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.chat import ChatPayload
from models.tool import ToolDefinition, FunctionToolDefinition, ToolParameters
from ai21 import AsyncAI21Client
import os
from dotenv import load_dotenv
from ai21.models.chat import ChatMessage, ResponseFormat, DocumentSchema, FunctionToolDefinition, ToolDefinition, ToolParameters


router = APIRouter()

@router.post("/chat")
async def chat_endpoint(payload: ChatPayload):
    load_dotenv()
    token = os.environ.get("api-token")
    client = AsyncAI21Client(api_key=token)
    
    participants = payload.participants
    messages = payload.messages
    data = []
    
    system = "You are an expert in sports psychology, helping users resolve conflicts related to sports."
    assistant = "Hello, I am here to help you resolve your conflict about sports. How can I assist you today?"
    
    chatMessages = [
        ChatMessage(role="system", content=system),
        ChatMessage(role="assistant", content=assistant),
    ]
    
    for message in messages:
        chatMessages.append(ChatMessage(role="user", content=message.message))
    
    response = await client.chat.completions.create(
        model="jamba-1.5-large",
        messages=chatMessages,
        stream=True,
        max_tokens=150,
        temperature=0.8,
        top_p=1,
        tools=[
            ToolDefinition(
                type="function",
                function=FunctionToolDefinition(
                    name="web_search",
                    description="Perform a web search and return relevant results",
                    parameters=ToolParameters(
                        type="object",
                        properties={
                            "query": {"type": "string", "description": "The search query"},
                            "num_results": {"type": "integer", "description": "The number of search results to return", "default": 5}
                        },
                        required=["query"]
                    )
                )
            )
        ],
        n=1,
        stop=["\n"]
    )
    
    async for chunk in response:
        data.append(chunk.choices[0].delta.content)
    
    return JSONResponse(content={"participants": participants, "messages": messages, "data": data}, status_code=200)
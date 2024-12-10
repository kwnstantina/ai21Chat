from fastapi import APIRouter, HTTPException
from ai21 import AsyncAI21Client
from ai21.models.chat import ChatMessage, ResponseFormat, DocumentSchema, FunctionToolDefinition, ToolDefinition, ToolParameters

import os
from dotenv import load_dotenv


router = APIRouter()



@router.get("/get-message")
async def read_root():  
 try:
    load_dotenv()
    token = os.environ.get("api-token")
    client = AsyncAI21Client(api_key=token)
    system = "You're a general, who helps users with their problems and conflicts in their relationships, based on the interest-based relational approach theory"
    messages = [
        ChatMessage(content=system, role="system"),
        ChatMessage(content="Hello, my boss friend says that I am silly and I feel sad, what could I do to feel better", role="user"),
    ]
    
    response = await client.chat.completions.create(
        model="jamba-1.5-large",
        messages=messages,
        documents=[],
        tools=[],
        n=1,
        max_tokens=2048,
        temperature=0.4,
        top_p=1,
        stop=[],
        response_format=ResponseFormat(type="text"),
    )
    
    data = {
        "id": response.id,
        "message": response.choices[0].message.content,
        "role": response.choices[0].message.role,
    }

    return data
 except Exception as e:
        # Log the error
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
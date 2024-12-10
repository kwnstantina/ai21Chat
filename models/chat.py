from dataclasses import dataclass
from pydantic import BaseModel
from typing import List


@dataclass
class Message(BaseModel):
    participant: str
    message: str
    
@dataclass
class ChatPayload(BaseModel):
    participants: List[str]
    messages: List[Message]

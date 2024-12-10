from pydantic import BaseModel
from typing import List
from dataclasses import dataclass

@dataclass
class ToolParameters(BaseModel):
    type: str
    properties: dict
    required: List[str]
    
@dataclass
class FunctionToolDefinition(BaseModel):
    name: str
    description: str
    parameters: ToolParameters

@dataclass
class ToolDefinition(BaseModel):
    type: str
    function: FunctionToolDefinition
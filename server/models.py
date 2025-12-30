"""
Pydantic models used for request validation.

These schemas intentionally remain minimal:
- no nested validation
- no enums
- no strict constraints

This keeps the API flexible while relying on server-side checks.
"""



from pydantic import BaseModel, Field
from typing import Dict

class AgentRegistration(BaseModel):
    agent_id: str



class AgentHeartbeat(BaseModel):
    agent_id: str


class TaskCreate(BaseModel):
    task_type: str
    payload: Dict = Field(default_factory=dict) # Creates new dict per request, is safe and industry standard


class ReportSubmit(BaseModel):
    agent_id: str
    task_id: str
    status: str
    result: Dict = Field(default_factory=dict) 
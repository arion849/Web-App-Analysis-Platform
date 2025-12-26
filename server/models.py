# Requests/response schemas
from pydantic import BaseModel
from typing import Dict

class AgentRegistration(BaseModel):
    agent_id: str



class AgentHeartbeat(BaseModel):
    agent_id: str


class TaskCreate(BaseModel):
    agent_id: str
    task_type: str
    payload: Dict = {}


class ReportSubmit(BaseModel):
    agent_id: str
    task_id: str
    status: str
    result: Dict = {}
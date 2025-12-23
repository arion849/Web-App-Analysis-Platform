# Requests/response schemas
from pydantic import BaseModel
from typing import List
from datetime import datetime


class AgentRegistration(BaseModel):
    agent_id: str
    host: str
    capabilities: List[str]


class Heartbeat(BaseModel):
    agent_id: str
    timestap: datetime


class AanlysisReport(BaseModel):
    agent_id: str
    target_url: str
    status_code: int
    response_time_ms: float
    timestamp: datetime

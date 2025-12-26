# Requests/response schemas
from pydantic import BaseModel


class AgentRegistration(BaseModel):
    agent_id: str



class AgentHeartbeat(BaseModel):
    agent_id: str

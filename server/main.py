# API routes

from fastapi import FastAPI, HTTPException
from models import AgentRegistration, AgentHeartbeat
from state import heartbeat, register_agent

app = FastAPI()

@app.post("/agents/register")
def register(req: AgentRegistration ):
    try:
        register_agent(req.agent_id)
    except(ValueError):
        raise HTTPException(status_code=409, detail= "Agent already registered")
    
    return{"status": "register"}

@app.post("/agents/heartbeat")
def agent_heartbeat(req: AgentHeartbeat):
    try:
        heartbeat(req.agent_id)
    except(KeyError):
        raise HTTPException(status_code=404, detail="Unknown agent")
    
    return {"status":"ok"}
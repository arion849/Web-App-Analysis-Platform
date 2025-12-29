# API routes

import time
from fastapi import FastAPI, HTTPException
from models import AgentRegistration, AgentHeartbeat, TaskCreate, ReportSubmit
from state import heartbeat, register_agent, create_task, submit_report

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

@app.post("/tasks")
def create_task_endpoint(task: TaskCreate):
    task_id = create_task(None, task.payload, task.task_type ) # No agent assigned upon task creation, the assign_task_to_agent deals with that.
    return {"task_id": task_id, "status" : "pending"}

@app.post("/tasks/assign")
def assign_task_to_agent(task_id:str, agent_id:str):
    from state import agents, tasks

    if agent_id not in agents:
        raise HTTPException(status_code=404, detail="Agent not registered")
    if agents[agent_id]["status"] != "online":
        raise HTTPException(status_code=400, detail="Agent offline")
    if tasks[task_id]["status"] != "pending":
        raise HTTPException(status_code=400, detail="Task not pending")

    tasks[task_id]["assigned_agent_id"] = agent_id
    tasks[task_id]["status"] = "running"
    tasks[task_id]["updated_at"] = time.time()

    return {"task_id": task_id, "agent_id" : agent_id, "status": "running"}
    

@app.post("/reports")
def report_task(report: ReportSubmit):
    from state import agents, tasks, reports

    if report.agent_id not in agents:
        raise HTTPException(status_code=404, detail="Unknown agent")
    
    if report.task_id not in tasks:
        raise HTTPException(status_code=404, detail="Unknown task")
    
    task = tasks[report.task_id]

    if task.get("assigned_agent_id") != report.agent_id:
        raise HTTPException(status_code=400, detail="Agent not assigned to this task")
    if task["status"] != "running":
        raise HTTPException(status_code=400, detail="Task not running")
    if report.status not in ("completed", "failed"):
        raise HTTPException(status_code=400, detail="Invalid report status")


    submit_report(report.agent_id, report.task_id, report.status, report.result)
    
    return {"status":"ok"}
# API routes

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
def assign_task(task: TaskCreate):
    from state import agents

    if task.agent_id not in agents:
        raise HTTPException(status_code=404, detail="Agent not registered")
    task_id = create_task(task.agent_id, task.payload, task.task_type )

    return {"task_id": task_id, "status" : "pending"}


@app.post("/reports")
def report_task(report: ReportSubmit):
    from state import agents, tasks, reports

    if report.agent_id not in agents:
        raise HTTPException(status_code=404, detail="Unknown agent")
    
    if report.task_id not in tasks:
        raise HTTPException(status_code=404, detail="Unknown task")
    
    submit_report(report.agent_id, report.task_id, report.status, report.result)
    
    return {"status":"ok"}
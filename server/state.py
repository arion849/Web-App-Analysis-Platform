# in memory state

from typing import Dict, TypedDict, List
import time
import uuid

class AgentState(TypedDict):

    registered_at: float
    last_heartbeat: float
    status: str     # offline/online


agents: Dict[str, AgentState] = {}
reports: list[dict] = []


def register_agent(agent_id: str) -> None:
    if agent_id in agents:
        raise ValueError("Agent already registered.")
    
    now = time.time()
    
    agents[agent_id] = AgentState(
        registered_at = now,
        last_heartbeat = now,
        status= "online",
        
    )


def heartbeat(agent_id:str) -> None:
    if agent_id not in agents:
        raise KeyError("Unknown agent")
    
    now = time.time()
    agents[agent_id]["last_heartbeat"] = now
    agents[agent_id]["status"] = "online"




class TaskStorage(TypedDict):

    task_id: str
    assigned_agent_id: str | None
    task_type: str
    payload: dict
    status: str     # pending/running/completed/failed
    created_at: float
    updated_at: float


tasks: Dict[str, TaskStorage] = {}

def create_task( task_type:str = "default", payload: dict = {} ) -> str:
    task_id = str(uuid.uuid4())

    # Extra check to be sure that task_id is not in tasks.
    while task_id in tasks:
        task_id = str(uuid.uuid4())


    tasks[task_id] = TaskStorage(
        task_id = task_id,
        assigned_agent_id = None,
        task_type = task_type,
        payload = payload,
        status = "pending",
        created_at= time.time(),
        updated_at= time.time()
    )

    return task_id

class ReportStorage(TypedDict):
    agent_id: str
    task_id: str
    status: str
    result: dict
    timestamp: float


reports: List[ReportStorage] = []


def submit_report(agent_id:str, task_id: str, status:str, result:dict = {}) -> None:

    if agent_id not in agents:
        raise KeyError("Unknown agent")
    if task_id not in tasks:
        raise KeyError("Unknown task")
    

    reports.append(ReportStorage(
        agent_id = agent_id, 
        task_id = task_id, 
        status = status, 
        result = result, 
        timestamp = time.time(),
    ))

    tasks[task_id]["status"] = status
    tasks["updated_at"]= time.time()


def timeout_heartbeat() -> None:
    now: float = time.time()
    timeout: float = 15

    for agent_id, agent in agents.items():
        if agent["status"] == "online" and now - agent["last_heartbeat"] > timeout:
            agent["status"] = "offline"

    
# in memory state

from typing import Dict, TypedDict, List
import time
import uuid

class AgentState(TypedDict):

    registered_at: float
    last_heartbeat: float


agents: Dict[str, AgentState] = {}
reports: list[dict] = []


def register_agent(agent_id: str) -> None:
    if agent_id in agents:
        raise ValueError("Agent already registered.")
    
    now = time.time()
    
    agents[agent_id] = AgentState(
        registered_at = now,
        last_heartbeat = now,
    )


def heartbeat(agent_id:str) -> None:
    if agent_id not in agents:
        raise KeyError("Unknown agent")
    agents[agent_id]["heartbeat"] = time.time()





class TaskStorage(TypedDict):

    task_id: str
    agent_id: str
    task_type: str
    payload: dict
    status: str


tasks: Dict[str, TaskStorage] = {}

def create_task(agent_id: str, task_type:str = "default", payload: dict = {} ) -> str:
    task_id = str(uuid.uuid4())

    # Extra check to bee sure that task_id is not if tasks.
    while task_id in tasks:
        task_id = str(uuid.uuid4())

    tasks[task_id] = TaskStorage(
        task_id = task_id,
        agent_id = agent_id,
        task_type = task_type,
        payload = payload,
        status = "pending"
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
                   timestamp = time.time()
    ))

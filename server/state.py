# in memory state

from typing import Dict, Any, TypedDict
import time

class AgentState(TypedDict):

    registered_at: float
    last_heartbeat: float


agents: Dict[str, Any] = {}
reports: list[dict] = []


def register_agent(agent_id: str) -> None:
    if agent_id in agents:
        raise ValueError("Agent already registered.")
    now = time.time()
    agents[agent_id] = {
        "registered_at" : now,
        "last_heartbeat": now,
    }


def heartbeat(agent_id:str) -> None:
    if agent_id not in agents:
        raise KeyError("Unknown agent")
    agents[agent_id]["heartbeat"] = time.time()

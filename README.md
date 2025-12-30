# Distributed Web Application Analysis Platform (MVP)

This project is a minimal distributed analysis platform built as part of a technical internship assignment.  
It implements a central orchestration server that manages agents, tasks, and reports, focusing on backend robustness and scope control.

The system is intentionally simple and demonstrates core distributed-system concepts such as agent registration, liveness tracking, task assignment, and result reporting.

---

## How the system works (high level)

- Agents register with the server using a unique `agent_id`
- Agents periodically send heartbeats to indicate they are alive
- Tasks can be created and assigned to online agents
- Agents submit reports when tasks complete or fail
- If an agent stops sending heartbeats, it is marked offline after a timeout

All state is stored in memory and reset when the server restarts.

---

## Running the server

### Using Docker (recommended)

From the repository root:

```bash
docker-compose up --build
```
#### IMPORTANT NOTE

When accessing the API, after opening the server in browser you must manually add /docs to the URL like so:

http://localhost:8000/docs 

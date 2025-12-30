## 1. What I implemented

I implemented a minimal distributed orchestration server using FastAPI.  
The server supports:

- Agent registration with unique identifiers
- Agent liveness tracking using periodic heartbeats
- Online/offline agent status based on heartbeat timeouts
- Task creation and explicit assignment to agents
- Report submission for completed or failed tasks
- In-memory storage for agents, tasks, and reports

The focus of the implementation is backend robustness and clarity rather than feature completeness.

---

## 2. What I intentionally did not implement

I deliberately did not implement:

- Persistent storage (databases or caches)
- Authentication or authorization
- Automatic task scheduling
- Agent-side execution logic as a separate service
- Retry mechanisms or fault recovery
- Background workers or async schedulers

These omissions were intentional to keep the scope aligned with the assignment and to avoid shallow or incomplete implementations.

---

## 3. Why I made those choices

The main goal was to deliver a clear and defensible MVP.

By keeping all state in memory and interactions explicit, the system remains easy to reason about and test.  
This allowed me to focus on:

- Correct API design
- Defensive validation
- Failure handling through heartbeat timeouts
- Clear separation of responsibilities

More advanced features would require additional infrastructure and would reduce the clarity of the core design within the given time constraints.

---

## 4. What I would work on in the first 30–90 days of the internship

In the first 30 days, I would:
- Add persistent storage for agents, tasks, and reports
- Introduce structured logging and metrics
- Improve test coverage, especially for failure scenarios

In the next 60–90 days, I would:
- Implement authentication and authorization
- Add background processing for heartbeat checks and scheduling
- Introduce proper agent services instead of simulated agents
- Improve scalability by decoupling components

---

## 5. What I found difficult or unclear

The most challenging part was deciding what *not* to implement.

Distributed systems offer many possible extensions, and the difficulty was resisting overengineering while still delivering something meaningful.  
Clarifying the expected depth for an MVP required careful interpretation of the assignment.

---

## 6. Areas where I feel strong and areas I want to improve

I feel strongest in:
- Backend API design
- Scope management
- Defensive programming
- Reasoning about system trade-offs

I want to improve further in:
- Production-grade distributed systems
- Fault tolerance patterns
- Observability and monitoring
- Long-running background processing
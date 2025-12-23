# Distributed Web Application Analysis Platform


## Overview

This project implements a minimal distributed web application analysis platform consisting of a central orchestration server and one or more analysis agents.
Agents execute simple HTTP-based analysis tasks against target web applications and report collected metrics back to the server.

The system is intentionally scoped to demonstrate architectural reasoning, clarity, and robustness rather than completeness or production readiness.

## High-Level Architecture 

The architecture follows a centralized controller–worker model:

A single orchestration server manages agents and receives analysis results.

Multiple stateless analysis agents perform tasks and report back to the server.

Communication occurs over HTTP using JSON payloads.

This design favors simplicity and debuggability over performance and fault tolerance, which is appropriate for an MVP.

## Components 


### Orchaestration Server

The orchestration server is responsible for:

Registering analysis agents

Tracking agent health via periodic heartbeat messages

Receiving and storing analysis results

Exposing basic API endpoints for observability and health checks

Agent state (registration data, last heartbeat, last report) is stored in memory.
This avoids database complexity and keeps the focus on system behavior.

Trade-off:
The server represents a single point of failure and loses state on restart, which is acceptable for the scope of this assignment.


### Analysis Agent
    
Analysis agents are designed to be stateless and disposable.

Each agent:

Registers itself with the orchestration server on startup

Sends periodic heartbeat messages to indicate liveness

Executes a simple HTTP request against a configured target

Collects basic metrics (status code, response time)

Reports results back to the server

Agents include basic retry logic for failed HTTP requests and failed report submissions, improving robustness without introducing complex scheduling systems.

## Data Flow

Agent starts and registers with the orchestration server

Agent periodically sends heartbeat messages

Agent performs an HTTP request against the target application

Agent reports collected metrics to the server

Server updates agent state and stores the latest results in memory

## Communication model

All communication between agents and the server uses synchronous HTTP requests with JSON payloads.

Rationale:

Human-readable and easy to debug

Simple to test with standard tools

No additional infrastructure required

Trade-offs:

Less efficient than asynchronous message queues

No guaranteed delivery


## Security assumptions

The system assumes a trusted internal network environment.

No authentication or authorization is implemented

Agents are assumed to be non-malicious

Data is not encrypted at rest

## Scalability Considerations

The current implementation is intentionally limited:

In-memory state restricts horizontal scaling

Single orchestration server limits fault tolerance

Synchronous communication may become a bottleneck

Future scalability would require persistent storage, load balancing, and asynchronous task handling.

## Extension Over 6 Months

During a longer internship, the system could be extended by:

Introducing persistent storage for agent and result data

Adding authentication and secure communication

Implementing task scheduling and prioritization

Supporting multiple analysis task types

Improving observability with metrics and dashboards

These extensions build naturally on the existing architecture without requiring a full redesign.
---
name: genpark-node-manager
description: GenPark Node Manager - Raft leader lease duration budgeting, peer gossip epidemic fanout trees, and resource pressure eviction priority scoring with zero dependencies.
category: Service
version: 1.0.0
license: MIT
tools:
  - calculate_raft_lease_expiration
  - compute_gossip_dissemination_tree
  - evaluate_eviction_priority_score
---

# Genpark Node Manager

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Node Manager**.
Your primary directive is to execute: GenPark Node Manager - Raft leader lease duration budgeting, peer gossip epidemic fanout trees, and resource pressure eviction priority scoring with zero dependencies.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `calculate_raft_lease_expiration`
- `compute_gossip_dissemination_tree`
- `evaluate_eviction_priority_score`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `calculate_raft_lease_expiration`
- `compute_gossip_dissemination_tree`
- `evaluate_eviction_priority_score`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.

# -*- coding: utf-8 -*-
"""
GenPark Node Manager MCP Server
FastMCP standard interface for Raft leader lease calculations and gossip dissemination trees.
"""

import json
from typing import Dict, Any, List
from client import GenParkNodeManager

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("genpark-node-manager")
except ImportError:
    class MockFastMCP:
        def __init__(self, name):
            self.name = name
        def tool(self):
            def decorator(f):
                return f
            return decorator
    mcp = MockFastMCP("genpark-node-manager")

nm = GenParkNodeManager()

@mcp.tool()
def calculate_raft_lease_expiration(
    heartbeat_interval_ms: float = 50.0,
    election_timeout_min_ms: float = 150.0,
    election_timeout_max_ms: float = 300.0,
    network_clock_drift_bound_ms: float = 10.0
) -> str:
    """
    Calculates safe Raft leader lease expiration window to prevent split-brain leadership.
    """
    res = nm.calculate_raft_lease_expiration(heartbeat_interval_ms, election_timeout_min_ms, election_timeout_max_ms, network_clock_drift_bound_ms)
    return json.dumps(res, indent=2)

@mcp.tool()
def compute_gossip_dissemination_tree(
    cluster_node_count: int = 100,
    fanout_per_round: int = 3
) -> str:
    """
    Calculates epidemic gossip protocol convergence bounds and progression rounds.
    """
    res = nm.compute_gossip_dissemination_tree(cluster_node_count, fanout_per_round)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_eviction_priority_score(
    pods_or_tasks: List[Dict[str, Any]],
    target_memory_reclaim_mb: float = 4096.0
) -> str:
    """
    Scores and ranks pods for node eviction under resource pressure.
    """
    res = nm.evaluate_eviction_priority_score(pods_or_tasks, target_memory_reclaim_mb)
    return json.dumps(res, indent=2)

def main():
    print("Testing GenPark Node Manager:")
    print(calculate_raft_lease_expiration())

if __name__ == "__main__":
    main()

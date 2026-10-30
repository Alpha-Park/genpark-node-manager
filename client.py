# -*- coding: utf-8 -*-
"""
GenPark Node Manager Client
Pure Python Standard Library (Zero External Dependencies)
Implements Raft leader lease duration budgeting, peer gossip epidemic fanout trees,
and resource pressure eviction priority scoring.
"""

import math
import random
from typing import Dict, Any, List, Optional

class GenParkNodeManager:
    """
    Decentralized agent node coordination and cluster lifecycle management engine.
    """

    def __init__(self):
        pass

    def calculate_raft_lease_expiration(
        self,
        heartbeat_interval_ms: float = 50.0,
        election_timeout_min_ms: float = 150.0,
        election_timeout_max_ms: float = 300.0,
        network_clock_drift_bound_ms: float = 10.0,
        current_time_epoch_ms: float = 1730000000000.0
    ) -> Dict[str, Any]:
        """
        Calculates safe Raft leader lease expiration window to prevent split-brain leadership:
          SafeLeaseDuration = ElectionTimeoutMin - HeartbeatInterval - (2 * ClockDrift)
          LeaseExpirationTimestamp = CurrentTime + SafeLeaseDuration
        """
        safe_lease_ms = election_timeout_min_ms - heartbeat_interval_ms - (2.0 * network_clock_drift_bound_ms)
        safe_lease_ms = max(5.0, safe_lease_ms)
        lease_expiration_ms = current_time_epoch_ms + safe_lease_ms

        valid = safe_lease_ms > heartbeat_interval_ms

        return {
            "current_time_epoch_ms": current_time_epoch_ms,
            "safe_lease_duration_ms": round(safe_lease_ms, 2),
            "lease_expiration_timestamp_ms": round(lease_expiration_ms, 2),
            "election_timeout_window_ms": [election_timeout_min_ms, election_timeout_max_ms],
            "lease_safety_valid": valid,
            "split_brain_protection_posture": "LEADER_LEASE_SECURE" if valid else "CLOCK_DRIFT_HAZARD"
        }

    def compute_gossip_dissemination_tree(
        self,
        cluster_node_count: int = 100,
        fanout_per_round: int = 3
    ) -> Dict[str, Any]:
        """
        Calculates epidemic gossip protocol convergence bounds:
          Rounds = ceil( ln(N) / ln(fanout) )
          MessageExchanges = Rounds * N * fanout
        """
        n = max(2, cluster_node_count)
        k = max(2, fanout_per_round)

        rounds = math.ceil(math.log(n) / math.log(k))
        total_exchanges = rounds * n * k

        # Infection progression per round
        progression = []
        infected = 1
        for r in range(1, rounds + 1):
            infected = min(n, infected * (k + 1))
            progression.append({
                "round": r,
                "reachable_nodes_count": infected,
                "coverage_percentage": round((infected / n) * 100.0, 1)
            })

        return {
            "total_cluster_nodes": n,
            "fanout_factor": k,
            "theoretical_rounds_to_consensus": rounds,
            "total_protocol_message_exchanges": total_exchanges,
            "dissemination_timeline": progression
        }

    def evaluate_eviction_priority_score(
        self,
        pods_or_tasks: List[Dict[str, Any]],
        target_memory_reclaim_mb: float = 4096.0
    ) -> Dict[str, Any]:
        """
        Scores and ranks pods for node eviction under resource pressure:
          EvictionScore = (1000 - PriorityClass) * 2.0 + (MemoryUsageMB * 0.5) + (IdleHours * 10.0)
        Higher score = evicted first.
        """
        scored = []
        for pod in pods_or_tasks:
            pod_id = pod.get("id", "pod")
            priority_class = float(pod.get("priority_class", 500.0))
            mem_mb = float(pod.get("memory_mb", 512.0))
            idle_hrs = float(pod.get("idle_hours", 1.0))

            eviction_score = ((1000.0 - priority_class) * 2.0) + (mem_mb * 0.5) + (idle_hrs * 10.0)
            scored.append({
                "pod_id": pod_id,
                "priority_class": priority_class,
                "memory_mb": mem_mb,
                "idle_hours": idle_hrs,
                "eviction_score": round(eviction_score, 2)
            })

        # Rank descending
        sorted_evictions = sorted(scored, key=lambda p: p["eviction_score"], reverse=True)

        eviction_plan = []
        reclaimed_mb = 0.0
        for p in sorted_evictions:
            if reclaimed_mb >= target_memory_reclaim_mb:
                break
            eviction_plan.append(p)
            reclaimed_mb += p["memory_mb"]

        return {
            "target_memory_reclaim_mb": target_memory_reclaim_mb,
            "reclaimed_memory_mb": round(reclaimed_mb, 2),
            "reclaim_target_met": reclaimed_mb >= target_memory_reclaim_mb,
            "evicted_pods_count": len(eviction_plan),
            "eviction_candidates": eviction_plan
        }

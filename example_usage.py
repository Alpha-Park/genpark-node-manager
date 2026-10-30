# -*- coding: utf-8 -*-
from client import GenParkNodeManager

nm = GenParkNodeManager()

# 1. Raft Leader Lease
lease = nm.calculate_raft_lease_expiration(heartbeat_interval_ms=50.0, election_timeout_min_ms=180.0, network_clock_drift_bound_ms=15.0)
print(f"Raft Leader Lease: Duration={lease['safe_lease_duration_ms']}ms ({lease['split_brain_protection_posture']})")

# 2. Gossip Dissemination Tree
gossip = nm.compute_gossip_dissemination_tree(cluster_node_count=250, fanout_per_round=4)
print()
print(f"Epidemic Gossip: {gossip['total_cluster_nodes']} nodes, Fanout={gossip['fanout_factor']}")
print(f"  Rounds to Consensus: {gossip['theoretical_rounds_to_consensus']}, Total Messages: {gossip['total_protocol_message_exchanges']}")

# 3. Pod Eviction Scoring
pods = [
    {"id": "worker-batch-1", "priority_class": 100.0, "memory_mb": 2048.0, "idle_hours": 6.0},
    {"id": "api-gateway", "priority_class": 900.0, "memory_mb": 1024.0, "idle_hours": 0.1},
    {"id": "analytics-collector", "priority_class": 200.0, "memory_mb": 3072.0, "idle_hours": 4.0}
]
evict = nm.evaluate_eviction_priority_score(pods, target_memory_reclaim_mb=3500.0)
print()
print(f"Node Eviction: Reclaimed {evict['reclaimed_memory_mb']}/{evict['target_memory_reclaim_mb']}MB (Evicted {evict['evicted_pods_count']} pods)")
for p in evict['eviction_candidates']:
    print(f"  Evicted: {p['pod_id']} (Score={p['eviction_score']})")

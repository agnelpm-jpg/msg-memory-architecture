# MSG Architecture Specification

## Overview

MSG (Mnemonic State Graph) is a four-layer memory architecture for conversational AI systems. Its central thesis is that **cognition is distributed** between the model and the human — the model manages pointers, the human provides the memory.

## Design Principles

1. **Human as memory store**: The human remembers most of what was discussed; they need cues, not content
2. **Cue-gated retrieval**: Only cue when confidence is high enough to justify the interruption
3. **Update-in-place**: A cued node cannot be stale by construction
4. **Dependency-aware**: Changes to hub facts cascade to dependents
5. **Socratic confirmation**: Contradictions of high-centrality facts require human confirmation

## Four-Layer Stack

```
┌─────────────────────────────────────┐
│  Layer 1: LLM + Cue Engine          │
│  - Natural language interface       │
│  - Cue generation & acceptance      │
│  - Adaptive threshold tuning        │
├─────────────────────────────────────┤
│  Layer 2: VPC (Variable Persistence)│
│  - Dual-graph working memory        │
│  - Human-readable cues & summaries  │
│  - Machine-readable embeddings      │
├─────────────────────────────────────┤
│  Layer 3: Vector Store              │
│  - Immutable, content-addressed     │
│  - Full document chunks             │
│  - Fallback for deep retrieval      │
├─────────────────────────────────────┤
│  Layer 4: Session Store             │
│  - On-disk serialization            │
│  - Audit logging                    │
│  - Tombstoned deprecated nodes      │
└─────────────────────────────────────┘
```

## VPC Node Schema

Every salient concept becomes a VPC node:

```python
@dataclass
class VPCNode:
    # Human-facing
    cue: str              # 5-10 word recall prompt
    summary: str          # 1-2 sentence summary
    
    # Machine-facing
    entities: List[str]   # Structured entities
    embedding: np.ndarray # Semantic embedding
    
    # Graph topology
    dag_parents: List[int]
    dag_children: List[int]
    assoc_edges: Dict[int, float]  # neighbor -> weight
    
    # Cognitive state
    confidence: float     # C(t) = C_base * C_structural * C_recency
    centrality: float     # PageRank over DAG
    user_priority: float  # Domain importance (0-1)
    
    # Temporal state
    last_referenced: int  # Turn number
    last_cued: int        # Turn number
    missed_cues: int      # Count since last hit
    
    # Lifecycle
    status: str           # active | deprecated | archived
    version: int          # Monotonic counter
```

## Confidence Model

### Formula

```
C(t) = C_base × C_structural × C_recency
```

### Components

**Base Decay (missed-cue driven)**
```
C_base = C_0 · λ^(missed_cues)    where λ = 0.95
```
- Decays ONLY on ignored cues
- No penalty for dormant but never-cued facts
- Aligns with Tulving's cue-dependent forgetting

**Structural Importance**
```
C_structural = 0.4 × centrality + 0.4 × user_priority + 0.2
```
- Hub facts decay more slowly
- Critical decisions get persistent cueing

**Recency Boost**
```
C_recency = 1 + 0.5 × e^(-0.3 × Δt)
```
- Spikes to 1.5 on reference
- Relaxes to 1.0 over ~10 turns

**Archival Threshold**: C(t) < 0.25 for 50+ consecutive turns

## Dual Graph Topology

### Dependency DAG (Directed Acyclic Graph)

**Purpose**: Invalidation and centrality

**Mechanisms**:
1. **Cascade invalidation**: On update, children confidence ×= 0.9
2. **PageRank centrality**: Hub detection for persistence
3. **Safe deprecation**: >2 dependents requires confirmation

### Association Graph (Undirected, Weighted)

**Purpose**: Cueing and priming

**Mechanisms**:
1. **Co-occurrence tracking**: 5-turn sliding window
2. **Priming**: 1.2× boost to neighbors for 3 turns
3. **Spreading activation**: Based on Collins & Loftus (1975)

## Cue Engine

### Scoring

```
score(node) = cos(query_embedding, node_embedding) × C(t) × priming_multiplier
```

### Adaptive Threshold

```
τ = base_τ + 0.02 × (misses - hits_in_last_20)
```

### Cue Types

| Type | Trigger | Base Accept | Rationale |
|------|---------|-------------|-----------|
| Recognition | High sim, no conflict | 0.90 | Low pressure |
| Continuation | Re-entry, high centrality | 0.85 | Contextual |
| Branching | Moderate sim near node | 0.83 | Prevents conflation |
| Elaboration | Vague reference | 0.80 | Grounds ambiguity |
| Contrast | Contradiction detected | 0.78 | Signals disagreement |
| Correction | Low confidence | 0.62 | Admits fallibility |

## Progressive Hydration

Three-tier retrieval on successful cue:

1. **Summary** (~50 tokens): Cue + summary from Layer 2
2. **Expansion** (~400 tokens): + most relevant chunk from Layer 3
3. **Full** (~2,000 tokens): + top-3 chunks with provenance

Escalation triggered by explicit human request ("tell me more", "why?").

## Socratic Garbage Collection

When an update contradicts a node with >2 dependents:
1. Pause the update
2. Fire a Contrast cue to the human
3. Wait for explicit confirmation
4. Apply update + cascade if confirmed

Cost: 35 tokens for clarifying question.

## Safety Layer

### Tombstone Design
- Deprecated nodes are never deleted
- Full audit trail: [turn, tool_call, args, user_input, reason]

### Poisoning Defense
- High-centrality (>0.6) deprecation requires confirmation
- >2 dependent deprecation requires confirmation

### Gaslighting Prevention
- Cannot silently overwrite established facts
- Contradictions must route through Correction cue

## References

- Tulving, E. (1974). Cue-dependent forgetting. *American Scientist*, 62(1), 74-82.
- Collins, A. M. & Loftus, E. F. (1975). Spreading-activation theory. *Psychological Review*, 82(6), 407-428.
- Anderson, J. R. (1983). Spreading activation theory of memory. *JVLB*, 22(3), 261-295.
- Koriat, A. (1993). The accessibility model of feeling of knowing. *Psychological Review*, 100(4), 609-639.

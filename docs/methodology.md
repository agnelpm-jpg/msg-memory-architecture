# Experimental Methodology

## Design Rationale

The evaluation isolates three structural mechanisms testable without a live LLM or human subjects:

1. **Update-in-place deduplication**: Does versioning prevent stale retrieval?
2. **Cue-gated token economy**: Does confidence-gated cueing reduce tokens?
3. **DAG cascade invalidation**: Does dependency awareness propagate changes?

This is a **mechanism-level ablation**, not a system-level validation.

## World Generation

Each world instance draws randomly:

| Parameter | Range | Description |
|-----------|-------|-------------|
| Topic count | 15-40 | Number of distinct topics |
| Turn count | 250-600 | Conversation length |
| Embedding dim | 24-64 | Synthetic embedding dimension |
| DAG density | 0.25-0.55 | Dependency edge density |
| Update rate | 0.08-0.35 | Fraction of update turns |
| Query rate | 0.15-0.30 | Fraction of query turns |
| Distractor rate | 0.20-0.45 | Fraction of distractor turns |

### Heterogeneous Categories

| Category | Priority | Contradiction Mult. | Weight |
|----------|----------|-------------------|--------|
| background_fact | 0.10-0.30 | 0.4 | 0.30 |
| preference | 0.20-0.45 | 0.6 | 0.25 |
| critical_decision | 0.75-0.95 | 1.4 | 0.15 |
| deadline_dependency | 0.55-0.80 | 1.8 | 0.15 |
| contested_fact | 0.40-0.70 | 2.5 | 0.15 |

### Hub Guarantee

At least 1 hub node (≥3 dependents) guaranteed per world, ensuring cascade invalidation and Socratic GC are meaningfully exercised.

## Turn Types

- **create**: New topic introduced
- **update**: Existing topic modified (may be contradiction)
- **distractor**: Off-topic turn (no memory impact)
- **query**: Question about existing topic

## Token Cost Model

Three-component mixture per turn:

| Type | Range | Frequency |
|------|-------|-----------|
| Short chat | 15-90 tokens | 65% |
| Explanation | 150-450 tokens | 25% |
| Heavy paste | 700-3,200 tokens | 10% |

## Baselines

### Full Context (Oracle)
- Re-attends to entire history every turn
- Accuracy = 1.0 by construction
- Cost grows linearly

### Naive RAG
- Indexes every create/update chunk
- No versioning: old and new compete equally
- Top-3 retrieval by cosine similarity
- Hit only if top result is correct topic AND latest version

### MSG-lite
- Full confidence model with PageRank centrality
- All 6 cue types with differentiated acceptance
- Priming, archiving, Socratic GC implemented
- Acceptance probabilities are hand-set modeling assumptions

## Metrics

| Metric | Systems | Description |
|--------|---------|-------------|
| Recall accuracy | All | Fraction of queries with correct answer |
| Tokens/turn | All | Mean token consumption |
| Cue rate | MSG | Fraction of queries triggering cue |
| False-cue rate | MSG | Fraction of cues that are wrong |
| Cascade events | MSG | Confidence discounts triggered |
| Socratic events | MSG | Pause-and-confirm events |
| Archived count | MSG | Nodes archived |

## Reproducibility Protocol

- 11 independent runs
- 12 base instances per run (fully randomized)
- 6 sweep points per run (contradiction rate 0.05-0.40)
- 132 total base-condition world instances
- All parameters resampled per instance
- Master seeds reported for exact reproduction

## Randomization

```python
# Fresh master seed every invocation
master_seed = int.from_bytes(os.urandom(4), "big")

# Reproduce with:
python msg_simulation.py --seed <master_seed>
```

## Limitations of Synthetic Evaluation

1. Synthetic embeddings, not real sentence embeddings
2. Rule-based acceptance model, not human behavior
3. No standard benchmark (LongMemEval, LoCoMo)
4. No comparison against implemented baselines (Mem0, Zep, etc.)
5. Single combined implementation, no per-mechanism ablation
6. Hand-tuned thresholds
7. Unmeasured real-world contradiction rates

These limitations define the boundary of claims. Results establish structural feasibility under synthetic conditions.

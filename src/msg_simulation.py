"""
MSG v2 simulation harness — v2.

Controlled synthetic benchmark testing the structural claims of the MSG spec
against two baselines: full-context and naive RAG.

WHAT CHANGED FROM v1:
- No fixed seed. Every run is a genuinely different instance (different topic
  count, turn count, update rate, DAG shape, token-length distribution)
  unless you explicitly pass --seed for reproducibility.
- Heterogeneous "context categories" per topic (critical_decision,
  deadline_dependency, preference, background_fact, contested_fact) with
  different user_priority ranges and per-topic contradiction likelihoods —
  this is closer to what a real conversation's memory load actually looks
  like than one undifferentiated topic pool.
- Variable, occasionally heavy per-turn token costs (chat messages vs.
  pasted logs/code/specs) instead of a fixed token-per-turn constant —
  this is what "heavy token usage patterns" stress-tests.
- Confidence model matches the spec's actual formula:
      C_t = C_base * C_structural * C_recency
  with C_structural driven by real PageRank centrality (recomputed every 50
  turns, as specced) instead of a degree-fraction proxy, C_base decaying only
  on missed cues (lambda=0.95), and C_recency spiking on reference and
  decaying over ~10 turns.
- All 6 cue types implemented with differentiated acceptance psychology
  (Recognition/Contrast/Correction/Continuation/Branching/Elaboration don't
  get accepted at the same rate — Correction in particular should get
  rejected more often, since it's the LLM admitting fallibility).
- Priming: referencing a node temporarily boosts association-linked
  neighbors for 3 turns, as specced.
- Archive threshold implemented (confidence < 0.25 for 50+ turns -> archived,
  excluded from future cueing).
- Socratic GC: updates that contradict a node with >2 dependents pause and
  cost an extra clarifying-question turn instead of silently overwriting.
- Every run now also renders and saves a PNG chart automatically, plus a
  JSON manifest of exactly which random world parameters were used (so a
  weird result is reproducible: rerun with --seed <the printed seed>).

This remains a controlled ALGORITHMIC simulation with synthetic embeddings
and a probabilistic (not real-LLM) "user." It validates the structural/token
mechanics; it does not validate real human-cueing psychology. See
msg_llm_loop_sim.html for the real-LLM-judged pilot on that front.
"""
import argparse
import datetime
import json
import os
import random
import string
from dataclasses import dataclass, field
from typing import Optional

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# ---------------------------------------------------------------------------
# Context categories: heterogeneous topic types, each with its own
# priority/volatility profile. This is what makes the simulated conversation
# feel like a real mixed workload instead of one undifferentiated topic pool.
# ---------------------------------------------------------------------------

CATEGORIES = {
    "critical_decision":  dict(user_priority=(0.75, 0.95), contradiction_mult=1.4, weight=0.15),
    "deadline_dependency": dict(user_priority=(0.55, 0.80), contradiction_mult=1.8, weight=0.15),
    "preference":          dict(user_priority=(0.20, 0.45), contradiction_mult=0.6, weight=0.25),
    "background_fact":     dict(user_priority=(0.10, 0.30), contradiction_mult=0.4, weight=0.30),
    "contested_fact":      dict(user_priority=(0.40, 0.70), contradiction_mult=2.5, weight=0.15),
}

CUE_TYPES = ["Recognition", "Contrast", "Correction", "Continuation", "Branching", "Elaboration"]

# Differentiated acceptance psychology per cue type (base probability a
# simulated user "accepts" a cue that is in fact correct; incorrect cues use
# a much lower accept probability computed later). Correction is lowest
# because the LLM is explicitly admitting fallibility -- more likely to get
# second-guessed even when it's right.
CUE_ACCEPT_BASE = {
    "Recognition": 0.90,
    "Contrast": 0.78,
    "Correction": 0.62,
    "Continuation": 0.85,
    "Branching": 0.83,
    "Elaboration": 0.80,
}


def rand_seed():
    return int.from_bytes(os.urandom(4), "big")


def run_tag():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + "".join(
        random.choices(string.ascii_lowercase, k=4))


# ---------------------------------------------------------------------------
# Token-cost model: mixture of short chat turns, medium explanations, and
# occasional heavy dumps (pasted code/logs/specs). This replaces the old
# fixed-120-tokens-per-turn assumption.
# ---------------------------------------------------------------------------

def sample_turn_tokens(rng):
    r = rng.random()
    if r < 0.65:
        return int(rng.uniform(15, 90))          # short chat turn
    elif r < 0.90:
        return int(rng.uniform(150, 450))         # explanation / paragraph
    else:
        return int(rng.uniform(700, 3200))        # heavy dump: code, logs, pasted doc


# ---------------------------------------------------------------------------
# World: topics with ground-truth embeddings, categories, and a dependency DAG
# ---------------------------------------------------------------------------

def make_world(rng, n_topics, embed_dim, edge_density):
    centroids = rng.normal(size=(n_topics, embed_dim))
    centroids /= np.linalg.norm(centroids, axis=1, keepdims=True)

    cat_names = list(CATEGORIES.keys())
    cat_weights = [CATEGORIES[c]["weight"] for c in cat_names]
    categories = rng.choice(cat_names, size=n_topics, p=np.array(cat_weights) / sum(cat_weights))

    user_priority = np.zeros(n_topics)
    contradiction_mult = np.zeros(n_topics)
    for i, c in enumerate(categories):
        lo, hi = CATEGORIES[c]["user_priority"]
        user_priority[i] = rng.uniform(lo, hi)
        contradiction_mult[i] = CATEGORIES[c]["contradiction_mult"]

    dag = nx.DiGraph()
    dag.add_nodes_from(range(n_topics))
    n_edges = int(n_topics * edge_density)
    possible = [(i, j) for i in range(n_topics) for j in range(i + 1, n_topics)]
    rng.shuffle(possible)
    for (i, j) in possible[:n_edges]:
        dag.add_edge(int(i), int(j))

    # Guarantee a few genuine hub nodes (>=3 dependents) — a real conversation
    # usually has a handful of load-bearing decisions (e.g. "database choice")
    # that many later things depend on. Pure random-edge sampling at this
    # density almost never produces that, which would make cascade
    # invalidation and Socratic GC untestable.
    n_hubs = max(1, n_topics // 10)
    hub_candidates = list(range(0, max(1, n_topics // 2)))
    rng.shuffle(hub_candidates)
    for hub in hub_candidates[:n_hubs]:
        later = [j for j in range(hub + 1, n_topics)]
        if len(later) < 3:
            continue
        rng.shuffle(later)
        n_deps = int(rng.integers(3, min(6, len(later) + 1)))
        for dep in later[:n_deps]:
            dag.add_edge(hub, dep)

    return dict(centroids=centroids, categories=categories, user_priority=user_priority,
                contradiction_mult=contradiction_mult, dag=dag, n_topics=n_topics)


def noisy_embed(centroid, noise, rng):
    v = centroid + rng.normal(scale=noise, size=centroid.shape)
    return v / np.linalg.norm(v)


def cos(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))


# ---------------------------------------------------------------------------
# Turn generator
# ---------------------------------------------------------------------------

@dataclass
class Turn:
    kind: str            # 'create' | 'update' | 'distractor' | 'query'
    topic: Optional[int]
    embedding: Optional[np.ndarray]
    turn_no: int
    tokens: int
    is_contradiction: bool = False   # big semantic jump = real contradiction, not a soft update


def generate_conversation(rng, n_turns, world, update_rate, query_rate, distractor_rate):
    centroids = world["centroids"]
    contradiction_mult = world["contradiction_mult"]
    n_topics = world["n_topics"]

    turns = []
    seen_topics = []
    for t in range(n_turns):
        r = rng.random()
        tokens = sample_turn_tokens(rng)
        if r < distractor_rate:
            turns.append(Turn("distractor", None, None, t, tokens))
        elif seen_topics and r < distractor_rate + update_rate:
            topic = int(rng.choice(seen_topics))
            # per-topic contradiction likelihood scaled by category volatility
            is_contra = rng.random() < min(0.9, 0.18 * contradiction_mult[topic])
            noise = 0.32 if is_contra else 0.16
            emb = noisy_embed(centroids[topic], noise=noise, rng=rng)
            turns.append(Turn("update", topic, emb, t, tokens, is_contradiction=is_contra))
        elif seen_topics and r < distractor_rate + update_rate + query_rate:
            topic = int(rng.choice(seen_topics))
            turns.append(Turn("query", topic, None, t, max(10, tokens // 4)))
        else:
            topic = int(rng.integers(0, n_topics))
            emb = noisy_embed(centroids[topic], noise=0.10, rng=rng)
            turns.append(Turn("create", topic, emb, t, tokens))
            if topic not in seen_topics:
                seen_topics.append(topic)
    return turns


# ---------------------------------------------------------------------------
# System 1: Full context — always correct, cost grows with actual (variable)
# turn sizes, not a flat per-turn constant.
# ---------------------------------------------------------------------------

def run_full_context(turns):
    running_total = 0
    per_turn_tokens = []
    hits, queries = 0, 0
    for turn in turns:
        running_total += turn.tokens
        per_turn_tokens.append(running_total)  # must attend to the whole history each turn
        if turn.kind == "query":
            queries += 1
            hits += 1
    return dict(total_tokens=sum(per_turn_tokens), per_turn_tokens=per_turn_tokens,
                accuracy=hits / max(queries, 1), queries=queries)


# ---------------------------------------------------------------------------
# System 2: Naive RAG — indexes every chunk (create + every update) at its
# real token size, no versioning/decay/dedup: stale and fresh chunks compete
# on equal footing purely by embedding similarity.
# ---------------------------------------------------------------------------

RAG_TOPK = 3

def run_naive_rag(turns, world):
    centroids = world["centroids"]
    index = []  # (topic, embedding, turn_no, tokens)
    latest_turn = {}
    total_tokens = 0
    per_turn_tokens = []
    hits, queries = 0, 0

    for turn in turns:
        cost = 0
        if turn.kind in ("create", "update"):
            index.append((turn.topic, turn.embedding, turn.turn_no, turn.tokens))
            latest_turn[turn.topic] = turn.turn_no
            cost = 0  # indexing itself isn't a context-window cost
        elif turn.kind == "query":
            queries += 1
            q_emb = noisy_embed(centroids[turn.topic], noise=0.12, rng=np.random.default_rng(turn.turn_no))
            scored = sorted(index, key=lambda c: cos(c[1], q_emb), reverse=True)
            topk = scored[:RAG_TOPK]
            cost = sum(c[3] for c in topk)  # real token cost of retrieved chunks
            if topk and topk[0][0] == turn.topic and topk[0][2] == latest_turn.get(turn.topic):
                hits += 1
        per_turn_tokens.append(cost)
        total_tokens += cost

    return dict(total_tokens=total_tokens, per_turn_tokens=per_turn_tokens,
                accuracy=hits / max(queries, 1), queries=queries)


# ---------------------------------------------------------------------------
# System 3: MSG — full confidence model, PageRank centrality, cue-type
# psychology, priming, Socratic GC, archiving.
# ---------------------------------------------------------------------------

SUMMARY_TOKENS = 50
EXPANSION_TOKENS = 400
FULL_TOKENS = 2000
LAMBDA = 0.95
RECENCY_HALFLIFE_TURNS = 10  # ~ matches spec's e^{-0.3*dt}
SOCRATIC_ASK_COST = 35        # cost of the clarifying question when GC pauses


@dataclass
class MSGNode:
    topic: int
    embedding: np.ndarray
    category: str
    user_priority: float
    base_confidence: float = 1.0     # only decays on missed cues
    centrality: float = 0.1
    last_referenced: int = 0
    missed_cues: int = 0
    status: str = "active"
    inactive_since: int = 0
    version: int = 1


def structural_conf(centrality, user_priority):
    return 0.4 * centrality + 0.4 * user_priority + 0.2


def recency_conf(delta_t):
    return 1.0 + 0.5 * np.exp(-delta_t / RECENCY_HALFLIFE_TURNS)


def select_cue_type(node, sim, is_session_reentry, is_contradiction_context, is_vague):
    if is_contradiction_context:
        return "Contrast"
    if node.base_confidence * structural_conf(node.centrality, node.user_priority) < 0.35 and sim > 0.7:
        return "Correction"
    if is_session_reentry and node.centrality > 0.6:
        return "Continuation"
    if is_vague:
        return "Elaboration"
    if 0.4 < sim < 0.75:
        return "Branching"
    return "Recognition"


def run_msg(turns, world, base_tau, min_gap, rng_seed):
    rng = np.random.default_rng(rng_seed)
    centroids = world["centroids"]
    dag = world["dag"]
    categories = world["categories"]
    user_priority = world["user_priority"]

    nodes = {}
    assoc = {}  # (topic_a, topic_b) -> co-occurrence weight
    recent_topics = []  # sliding window for association updates
    primed_until = {}   # topic -> turn number priming expires

    total_tokens = 0
    per_turn_tokens = []
    hits, queries, cued_count, false_cue = 0, 0, 0, 0
    cascade_events, archived_count, socratic_events = 0, 0, 0
    hits_recent, misses_recent = [], []
    cue_type_stats = {c: {"fired": 0, "accepted": 0} for c in CUE_TYPES}
    last_query_turn = -999

    def update_association(topics_window):
        for i in range(len(topics_window)):
            for j in range(i + 1, len(topics_window)):
                a, b = sorted((topics_window[i], topics_window[j]))
                if a == b:
                    continue
                key = (a, b)
                assoc[key] = assoc.get(key, 0.0) * 0.9 + 0.1  # exponential co-occurrence update

    def recompute_centrality():
        if len(dag) == 0:
            return
        pr = nx.pagerank(dag, alpha=0.85)
        for topic, n in nodes.items():
            n.centrality = pr.get(topic, 0.05)

    for turn in turns:
        cost = 0

        if turn.topic is not None and turn.kind != "query":
            recent_topics.append(turn.topic)
            if len(recent_topics) > 5:
                recent_topics.pop(0)
            update_association(recent_topics)

        if turn.turn_no > 0 and turn.turn_no % 50 == 0:
            recompute_centrality()

        if turn.kind == "create":
            cat = categories[turn.topic]
            n = MSGNode(topic=turn.topic, embedding=turn.embedding, category=cat,
                        user_priority=user_priority[turn.topic], last_referenced=turn.turn_no)
            nodes[turn.topic] = n
            cost = 0

        elif turn.kind == "update":
            if turn.topic in nodes:
                n = nodes[turn.topic]
                n_children = list(dag.successors(turn.topic))
                if turn.is_contradiction and len(n_children) > 2:
                    # Socratic GC: pause, ask, then apply (extra cost, but no
                    # silent corruption of dependents)
                    cost += SOCRATIC_ASK_COST
                    socratic_events += 1
                n.embedding = turn.embedding
                n.version += 1
                n.status = "active"
                n.last_referenced = turn.turn_no
                for child in n_children:
                    if child in nodes:
                        nodes[child].base_confidence *= 0.9
                        cascade_events += 1
            else:
                cat = categories[turn.topic]
                n = MSGNode(topic=turn.topic, embedding=turn.embedding, category=cat,
                            user_priority=user_priority[turn.topic], last_referenced=turn.turn_no)
                nodes[turn.topic] = n

        elif turn.kind == "query":
            queries += 1
            is_session_reentry = (turn.turn_no - last_query_turn) > 25
            is_vague = rng.random() < 0.15
            last_query_turn = turn.turn_no

            q_emb = noisy_embed(centroids[turn.topic], noise=0.12, rng=rng)

            best_node, best_score, best_sim = None, -1.0, 0.0
            for topic, n in nodes.items():
                if n.status != "active":
                    continue
                sim = cos(n.embedding, q_emb)
                delta_t = turn.turn_no - n.last_referenced
                c_t = n.base_confidence * structural_conf(n.centrality, n.user_priority) * recency_conf(delta_t)
                score = sim * c_t
                if primed_until.get(topic, -1) >= turn.turn_no:
                    score *= 1.2
                if score > best_score:
                    best_score, best_node, best_sim = score, n, sim

            n_hits = sum(hits_recent[-20:])
            n_miss = sum(misses_recent[-20:])
            tau = min(base_tau * 1.5, max(base_tau * 0.55, base_tau + 0.02 * (n_miss - n_hits)))
            gap_ok = (turn.turn_no - (best_node.last_referenced if best_node else -999)) >= 0

            fires = best_node is not None and best_score > tau and (turn.turn_no - last_query_turn >= -min_gap)

            if fires:
                is_contradiction_context = False
                cue_type = select_cue_type(best_node, best_sim, is_session_reentry, is_contradiction_context, is_vague)
                cue_type_stats[cue_type]["fired"] += 1
                cued_count += 1

                correct = (best_node.topic == turn.topic)
                base_accept = CUE_ACCEPT_BASE[cue_type]
                # correct cues get accepted at ~base_accept; incorrect cues get
                # "accepted" (i.e. false-positive slips through) far less often
                accept_prob = base_accept if correct else (1 - base_accept) * 0.25
                accepted = rng.random() < accept_prob

                # hydration: user asks "why/how" some of the time on accepted cues
                hydrate_roll = rng.random()
                if accepted and hydrate_roll > 0.92:
                    cost += FULL_TOKENS
                elif accepted and hydrate_roll > 0.55:
                    cost += EXPANSION_TOKENS
                else:
                    cost += SUMMARY_TOKENS

                best_node.last_referenced = turn.turn_no
                # priming: boost associated neighbors for 3 turns
                for (a, b), w in assoc.items():
                    if w > 0.6:
                        neighbor = b if a == best_node.topic else (a if b == best_node.topic else None)
                        if neighbor is not None:
                            primed_until[neighbor] = turn.turn_no + 3

                if accepted and correct:
                    hits += 1
                    cue_type_stats[cue_type]["accepted"] += 1
                    hits_recent.append(1); misses_recent.append(0)
                    best_node.missed_cues = 0
                else:
                    false_cue += 1
                    hits_recent.append(0); misses_recent.append(1)
                    best_node.missed_cues += 1
                    best_node.base_confidence *= LAMBDA
            else:
                cost += 10  # fallback: cheap direct re-ask, no node cued
                hits_recent.append(0); misses_recent.append(0)

            # archive sweep: low confidence, long untouched
            for topic, n in nodes.items():
                if n.status == "active":
                    c_now = n.base_confidence * structural_conf(n.centrality, n.user_priority) * recency_conf(turn.turn_no - n.last_referenced)
                    if c_now < 0.25:
                        if n.inactive_since == 0:
                            n.inactive_since = turn.turn_no
                        elif turn.turn_no - n.inactive_since > 50:
                            n.status = "archived"
                            archived_count += 1
                    else:
                        n.inactive_since = 0

        per_turn_tokens.append(cost)
        total_tokens += cost

    return dict(
        total_tokens=total_tokens, per_turn_tokens=per_turn_tokens,
        accuracy=hits / max(queries, 1), queries=queries,
        cue_rate=cued_count / max(queries, 1),
        false_cue_rate=false_cue / max(cued_count, 1),
        cascade_events=cascade_events, socratic_events=socratic_events,
        archived_count=archived_count, cue_type_stats=cue_type_stats,
    )


# ---------------------------------------------------------------------------
# Experiment runner: fully randomized world + conversation per call, unless
# a seed is fixed for the sweep's internal repeats.
# ---------------------------------------------------------------------------

def run_one(master_rng, n_turns=None, update_rate=None, n_topics=None):
    seed = int(master_rng.integers(0, 2**31 - 1))
    rng = np.random.default_rng(seed)

    n_topics = n_topics or int(rng.integers(15, 41))
    n_turns = n_turns or int(rng.integers(250, 601))
    embed_dim = int(rng.integers(24, 65))
    edge_density = rng.uniform(0.25, 0.55)
    update_rate = update_rate if update_rate is not None else float(rng.uniform(0.08, 0.35))
    query_rate = float(rng.uniform(0.15, 0.30))
    distractor_rate = float(rng.uniform(0.20, 0.45))

    world = make_world(rng, n_topics, embed_dim, edge_density)
    turns = generate_conversation(rng, n_turns, world, update_rate, query_rate, distractor_rate)

    full = run_full_context(turns)
    rag = run_naive_rag(turns, world)
    msg = run_msg(turns, world, base_tau=0.30, min_gap=4, rng_seed=seed + 1)

    params = dict(seed=seed, n_topics=n_topics, n_turns=n_turns, embed_dim=embed_dim,
                  edge_density=round(edge_density, 3), update_rate=round(update_rate, 3),
                  query_rate=round(query_rate, 3), distractor_rate=round(distractor_rate, 3))
    return params, full, rag, msg


def summarize_runs(runs):
    def agg(key_fn, results):
        return float(np.mean([key_fn(r) for r in results]))

    out = {}
    for name, results in runs.items():
        n_turns_list = [r["_n_turns"] for r in results]
        out[name] = dict(
            avg_tokens_per_turn=round(agg(lambda r: r["total_tokens"] / r["_n_turns"], results), 1),
            avg_total_tokens=round(agg(lambda r: r["total_tokens"], results), 0),
            avg_accuracy=round(agg(lambda r: r["accuracy"], results), 4),
        )
        if name == "msg":
            out[name]["avg_cue_rate"] = round(agg(lambda r: r["cue_rate"], results), 4)
            out[name]["avg_false_cue_rate"] = round(agg(lambda r: r["false_cue_rate"], results), 4)
            out[name]["avg_cascade_events"] = round(agg(lambda r: r["cascade_events"], results), 1)
            out[name]["avg_socratic_events"] = round(agg(lambda r: r["socratic_events"], results), 1)
            out[name]["avg_archived"] = round(agg(lambda r: r["archived_count"], results), 1)
    return out


def main():
    ap = argparse.ArgumentParser(description="MSG v2 simulation")
    ap.add_argument("--seed", type=int, default=None, help="Fix the master seed for reproducibility")
    ap.add_argument("--repeats", type=int, default=12, help="Randomized world instances per sweep point")
    ap.add_argument("--outdir", type=str, default=None, help="Output directory (default: timestamped)")
    args = ap.parse_args()

    master_seed = args.seed if args.seed is not None else rand_seed()
    master_rng = np.random.default_rng(master_seed)
    tag = run_tag()
    outdir = args.outdir or f"run_{tag}"
    os.makedirs(outdir, exist_ok=True)

    print(f"=== MSG v2 simulation — master seed {master_seed} ===")
    print(f"Output dir: {outdir}  (rerun with --seed {master_seed} to reproduce)\n")

    # ---- Base run: N randomized instances, no fixed rate ----
    base_runs = {"full": [], "rag": [], "msg": []}
    base_params = []
    for _ in range(args.repeats):
        params, full, rag, msg = run_one(master_rng)
        base_params.append(params)
        full["_n_turns"] = rag["_n_turns"] = msg["_n_turns"] = params["n_turns"]
        base_runs["full"].append(full)
        base_runs["rag"].append(rag)
        base_runs["msg"].append(msg)

    base_summary = summarize_runs(base_runs)
    print("--- base (fully randomized instances) ---")
    print(json.dumps(base_summary, indent=2))

    with open(os.path.join(outdir, "results_base.json"), "w") as f:
        json.dump(dict(master_seed=master_seed, per_instance_params=base_params, summary=base_summary), f, indent=2)

    # ---- Sweep: vary update/contradiction rate, everything else randomized ----
    sweep_points = [0.05, 0.10, 0.15, 0.20, 0.30, 0.40]
    sweep = {}
    for ur in sweep_points:
        runs = {"full": [], "rag": [], "msg": []}
        for _ in range(args.repeats):
            params, full, rag, msg = run_one(master_rng, update_rate=ur)
            full["_n_turns"] = rag["_n_turns"] = msg["_n_turns"] = params["n_turns"]
            runs["full"].append(full)
            runs["rag"].append(rag)
            runs["msg"].append(msg)
        sweep[str(ur)] = summarize_runs(runs)

    with open(os.path.join(outdir, "results_sweep.json"), "w") as f:
        json.dump(sweep, f, indent=2)

    print("\n--- update-rate sweep ---")
    print(json.dumps(sweep, indent=2))

    # ---- Chart: always generated, every run ----
    render_chart(sweep, sweep_points, outdir, master_seed)

    print(f"\nSaved: {outdir}/results_base.json, results_sweep.json, sweep_chart.png")


def render_chart(sweep, sweep_points, outdir, master_seed):
    full_acc = [sweep[str(u)]["full"]["avg_accuracy"] for u in sweep_points]
    rag_acc = [sweep[str(u)]["rag"]["avg_accuracy"] for u in sweep_points]
    msg_acc = [sweep[str(u)]["msg"]["avg_accuracy"] for u in sweep_points]
    rag_tok = [sweep[str(u)]["rag"]["avg_tokens_per_turn"] for u in sweep_points]
    msg_tok = [sweep[str(u)]["msg"]["avg_tokens_per_turn"] for u in sweep_points]
    full_tok = [sweep[str(u)]["full"]["avg_tokens_per_turn"] for u in sweep_points]

    fig, axes = plt.subplots(1, 3, figsize=(17, 4.8))

    ax = axes[0]
    ax.plot(sweep_points, full_acc, marker="o", label="Full context")
    ax.plot(sweep_points, rag_acc, marker="o", label="Naive RAG")
    ax.plot(sweep_points, msg_acc, marker="o", label="MSG")
    ax.set_xlabel("Contradiction / update rate")
    ax.set_ylabel("Recall accuracy (latest fact)")
    ax.set_title("Accuracy vs. fact-churn rate")
    ax.set_ylim(0, 1.05)
    ax.legend()

    ax = axes[1]
    ax.plot(sweep_points, rag_tok, marker="o", label="Naive RAG")
    ax.plot(sweep_points, msg_tok, marker="o", label="MSG")
    ax.set_xlabel("Contradiction / update rate")
    ax.set_ylabel("Tokens / turn")
    ax.set_title("Token cost (full-context off-scale, right panel)")
    ax.legend()

    ax = axes[2]
    ax.plot(sweep_points, full_tok, marker="o", color="gray", label="Full context")
    ax.plot(sweep_points, rag_tok, marker="o", label="Naive RAG")
    ax.plot(sweep_points, msg_tok, marker="o", label="MSG")
    ax.set_xlabel("Contradiction / update rate")
    ax.set_ylabel("Tokens / turn (all systems)")
    ax.set_title("Token cost, all three systems")
    ax.set_yscale("log")
    ax.legend()

    fig.suptitle(f"MSG v2 simulation — master seed {master_seed} (randomized world per point)", fontsize=10, color="gray")
    plt.tight_layout()
    outpath = os.path.join(outdir, "sweep_chart.png")
    plt.savefig(outpath, dpi=140)
    plt.close(fig)


if __name__ == "__main__":
    main()

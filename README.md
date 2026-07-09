# Mnemonic State Graph (MSG)

> A Cue-Gated, Human-in-the-Loop Memory Architecture for Conversational AI Systems

[![Paper](https://img.shields.io/badge/Paper-Orcid-blue)](https://orcid.org/0009-0009-9195-7417)
[![Python](https://img.shields.io/badge/Python-3.12-red)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Runs](https://img.shields.io/badge/Runs-11%20independent-orange)]()
[![Instances](https://img.shields.io/badge/World%20Instances-132-purple)]
[![Portfolio](https://img.shields.io/badge/Porfolio-white)](https://agnel.machfold.in/)

---

## Overview

MSG (Mnemonic State Graph) is a memory architecture built on the thesis that cognition in a human-LLM system is **distributed**: the model's role is not to remember everything, but to manage a small set of pointers and trigger human recall at the moments it is useful.

### Core Innovation

Instead of treating the human as a passive query source, MSG treats the human as a second, much larger and cheaper memory store. The LLM becomes an **indexer and activator** of that store.

### Key Mechanisms

- **Dual-graph working memory**: Strict dependency DAG for invalidation + cyclic association graph for cueing/priming
- **Confidence model**: Decays only on ignored cues (not elapsed time) — aligned with cue-dependent forgetting from cognitive psychology
- **Six-type cue taxonomy**: Recognition, Contrast, Correction, Continuation, Branching, Elaboration — each with differentiated human-acceptance dynamics
- **Socratic Garbage Collection**: Routes contradictory updates through explicit human confirmation rather than silent overwrite
- **Progressive hydration**: Three-tier retrieval (summary → expansion → full) for token efficiency

---

## Results Summary

| Metric | MSG vs Naive RAG |
|--------|-----------------|
| **Accuracy advantage** | +22.8 pp (mean), +13.4 to +27.7 pp (range) |
| **Token efficiency** | 4.8x fewer tokens per turn than RAG |
| **Full context comparison** | ~3 orders of magnitude cheaper than full context |
| **Consistency** | MSG beat RAG in **66/66** sweep-point comparisons |

The accuracy gap **widens** as contradiction rate increases — the signature prediction of update-in-place deduplication.

---

## Repository Structure

```
msg-memory-architecture/
├── src/
│   └── msg_simulation.py          # Main simulation harness
├── data/
│   ├── msg_aggregate_summary_11runs.json   # Aggregated results
│   └── consolidated_results_20260704_011226.md  # Full per-run data
├── figures/
│   ├── figure1_accuracy_tokens_vs_churn.png    # Accuracy & token sweep
│   └── msg_aggregate_chart_11runs.png          # 11-run aggregate chart
├── paper/
│   └── msg_paper.pdf              # ArXiv-ready paper (PDF)
├── docs/
│   ├── architecture.md            # Detailed architecture spec
│   └── methodology.md             # Experimental methodology
├── requirements.txt               # Python dependencies
├── CITATION.cff                   # Citation metadata
├── LICENSE                        # MIT License
└── README.md                      # This file
```

---

## Quick Start

### Prerequisites

- Python 3.12+
- NumPy 2.0+
- NetworkX 3.3+
- Matplotlib 3.9+

### Installation

```bash
# Clone the repository
git clone https://github.com/agnelpm-jpg/msg-memory-architecture
cd msg-memory-architecture

# Install dependencies
pip install -r requirements.txt
```

### Running the Simulation

```bash
# Run with random seed (default: 12 instances)
python src/msg_simulation.py

# Run with fixed seed for reproducibility
python src/msg_simulation.py --seed 12345

# Run with more instances
python src/msg_simulation.py --repeats 20

# Custom output directory
python src/msg_simulation.py --outdir my_experiment
```

### Output

Each run creates a directory with:
- `results_base.json` — Base condition results
- `results_sweep.json` — Contradiction-rate sweep results
- `sweep_chart.png` — Automatically generated visualization

---

## Reproducing the Paper Results

All 11 runs from the paper can be reproduced exactly using the reported master seeds:

```python
import subprocess

# Master seeds from the paper (reported in consolidated_results)
master_seeds = [
    865576579,   # Run 1
    1003439118,  # Run 2
    1116670113,  # Run 3
    3188866900,  # Run 4
    512109876,   # Run 5
    2965694878,  # Run 6
    731770865,   # Run 7
    # ... (see consolidated_results for complete list)
]

for seed in master_seeds:
    subprocess.run([
        'python', 'src/msg_simulation.py',
        '--seed', str(seed),
        '--outdir', f'reproduction/run_{seed}'
    ])
```

The aggregated results in `data/msg_aggregate_summary_11runs.json` contain all numbers reported in the paper.

---

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `SUMMARY_TOKENS` | 50 | Base cost for summary-tier cue |
| `EXPANSION_TOKENS` | 400 | Cost for expansion-tier retrieval |
| `FULL_TOKENS` | 2,000 | Cost for full-tier retrieval |
| `LAMBDA` | 0.95 | Base confidence decay per missed cue |
| `RECENCY_HALFLIFE` | 10 | Recency boost half-life (turns) |
| `SOCRATIC_ASK_COST` | 35 | Token cost of Socratic-GC question |
| `RAG_TOPK` | 3 | Chunks retrieved by naive RAG |
| `base_tau` | 0.30 | Base adaptive cueing threshold |
| `min_gap` | 4 | Minimum turns between cues |

---

## Architecture Deep Dive

For a detailed specification of the MSG architecture, see [docs/architecture.md](docs/architecture.md).

### Four-Layer Stack

```
Layer 1: LLM + Cue Engine       → Natural language interface
Layer 2: VPC (Working Memory)   → Dual-graph (DAG + Association)
Layer 3: Vector Store           → Immutable, content-addressed
Layer 4: Session Store          → On-disk serialization + audit
```

### Confidence Formula

```
C(t) = C_base × C_structural × C_recency

where:
  C_base = C_0 · λ^(missed_cues)          [λ = 0.95]
  C_structural = 0.4·centrality + 0.4·priority + 0.2
  C_recency = 1 + 0.5·e^(-0.3·Δt)
```

---

## Citation

If you use MSG or this code in your research, please cite:

```bibtex
@article{suresh2026msg,
  title={Mnemonic State Graph (MSG): A Cue-Gated, Human-in-the-Loop Memory Architecture for Conversational AI Systems},
  author={Suresh, Agnel},
  journal={arXiv preprint},
  year={2026},
  url={https://github.com/agnelpm-jpg/msg-memory-architecture}
}
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Priority areas for contributions:
- Real sentence-embedding integration (see Future Work #1)
- Extended LLM-in-the-loop pilot (see Future Work #2)
- Per-mechanism ablation framework (see Future Work #4)
- Benchmark evaluation on LongMemEval and LoCoMo (see Future Work #3)

---

## Future Work

1. **Replace synthetic embeddings** with real sentence embeddings
2. **Scale LLM-in-the-loop pilot** to independently-authored scenarios
3. **Evaluate on standard benchmarks** (LongMemEval, LoCoMo)
4. **Per-mechanism ablations** to isolate marginal contributions
5. **Learned adaptive thresholds** via bandit-style policies
6. **Human-subjects pilot** for cue-type acceptance validation

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## Acknowledgments

This work draws on decades of research in cognitive psychology, particularly the work of Endel Tulving on cue-dependent forgetting and encoding specificity, Allan Collins and Elizabeth Loftus on spreading activation, and Asher Koriat on metacognition and the feeling of knowing.

The simulation framework was inspired by the rigorous ablation methodology of Kerestecioglu (Microsoft Research, 2026) and the memory architecture comparisons on LongMemEval and LoCoMo benchmarks.

---

## Contact

**Agnel Suresh** — Machfold Ventures, Mumbai  
Email: agnelpm@gmail.com  

For questions about the architecture, methodology, or reproduction, please open an issue.

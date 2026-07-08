# Contributing to MSG

Thank you for your interest in contributing to the Mnemonic State Graph (MSG) project! This document provides guidelines for contributions.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or request features
- Include Python version, OS, and steps to reproduce
- For reproduction issues, include the master seed if applicable

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes with clear messages
4. Push to your fork
5. Open a Pull Request

### Priority Contribution Areas

We particularly welcome contributions in these areas:

#### 1. Real Embedding Integration (High Priority)
Replace synthetic embeddings with real sentence-embedding models:
- Integrate sentence-transformers or similar
- Validate that effect sizes hold under real embeddings
- Document any geometry-dependent behaviors

#### 2. Extended LLM-in-the-Loop Pilot (High Priority)
Scale the pilot validation:
- Independently-authored scenarios (not by architecture designers)
- Multiple model judges (GPT-4, Claude, Llama, etc.)
- Statistical power analysis for acceptance rates

#### 3. Benchmark Evaluation (High Priority)
Evaluate on standard benchmarks:
- LongMemEval
- LoCoMo
- Comparison against Mem0, Zep, MemGPT/Letta, Mnemosyne

#### 4. Per-Mechanism Ablations (Medium Priority)
Isolate marginal contributions:
- Confidence decay only
- Cueing only
- Cascade only
- Socratic GC only

#### 5. Adaptive Threshold Learning (Medium Priority)
Replace hand-tuned thresholds:
- Bandit-style adaptive policies
- Compare against fixed-threshold results

#### 6. Documentation (Ongoing)
- Architecture deep-dives
- Tutorials for extending MSG
- API documentation for VPC tools

## Code Style

- Follow PEP 8
- Use type hints where possible
- Document functions with docstrings
- Keep functions focused and testable

## Testing

Before submitting:
- Verify your changes don't break existing simulations
- Run at least one full simulation with `--seed` for reproducibility
- Check that figures generate correctly

## Questions?

Open an issue or contact: agnelpm@gmail.com

## Code of Conduct

- Be respectful and constructive
- Focus on ideas, not individuals
- Assume good intent
- Welcome newcomers

# Recursive Adaptive System (RAS) – Toy Simulation

This repository contains the simulation code for the toy example presented in the paper:

> **A Recursive Framework for Adaptive Dynamics in Non-Equilibrium Systems**
> Helmut Eckardt (2026)

## Description

A minimal implementation of a Recursive Adaptive System (RAS) that tracks a non-stationary environmental probability. The system uses a meta-operator to dynamically adjust its learning rate based on recent prediction error.

## Features

- Self-adaptive learning rate (meta-adaptation)
- Emergent metastability (automatic switching between high and low plasticity regimes)
- Demonstration of resonance and adaptive coherence

## Requirements

```bash
pip install numpy matplotlib
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/helmuteckardt1-hub/recursive_Adaptive_System_paper1.git
   cd recursive_Adaptive_System_paper1
   ```

2. Install dependencies:
   ```bash
   pip install numpy matplotlib
   ```

3. Run the simulation:
   ```bash
   python simulation.py
   ```

## Output

The script generates two figures:
- Tracking performance over time
- Comparison with fixed learning rates

## Citation

If you use this code, please cite the paper:

```bibtex
@article{eckardt2026,
  title   = {A Recursive Framework for Adaptive Dynamics in Non-Equilibrium Systems},
  author  = {Eckardt, Helmut},
  year    = {2026}
}
```

## License

MIT License


markdown

# Recursive Adaptive System (RAS) – Toy Simulation

This repository contains the simulation code for the toy example presented in the paper:

> **A Recursive Framework for Adaptive Dynamics in Non-Equilibrium Systems**  
> Helmut Eckardt (2026)

## Description

A minimal implementation of a Recursive Adaptive System (RAS) that tracks a non-stationary environmental probability. The system uses a meta-operator to dynamically adjust its learning rate based on recent prediction error.

## Features

- Self-adaptive learning rate (meta-adaptation)
- Emergent metastability (switching between high and low plasticity)
- Simple demonstration of resonance and adaptive coherence

## Requirements

```bash
pip install numpy matplotlib

How to RunClone the repository:bash

git clone https://github.com/helmuteckardt1-hub/recursive_Adaptive_System_paper1.git
cd recursive_Adaptive_System_paper1

Install the required packages:bash

pip install numpy matplotlib

Run the simulation:bash

python simulation.py

OutputThe script generates two figures:Tracking performance over time
Comparison with fixed learning rates

CitationIf you use this code, please cite the paper:bibtex

@article{eckardt2026,
  title   = {A Recursive Framework for Adaptive Dynamics in Non-Equilibrium Systems},
  author  = {Eckardt, Helmut},
  year    = {2026}
}

LicenseMIT License

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

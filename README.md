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

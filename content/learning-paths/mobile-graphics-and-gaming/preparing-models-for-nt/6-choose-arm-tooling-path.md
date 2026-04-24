---
title: Arm-Tooling
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---


# The Model Gym

the model gym is a tool that allows users to export models in the vgf file format similar to how we have done in this learning path. 

Steps for that can be found here: https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/model-training-gym/1-introduction/

it gives a good run down into the VGF backend and is something that is incredibly useful for this subject as a whole.


# Arm ExecuTorch: Model Gym vs Arm ExecuTorch: Manual Lowering 

## Overview
- **Model Gym**: High-level automated pipeline for lowering and running models
- **Manual VGF Lowering**: Low-level, developer-controlled process using the VGF file format



## When to Use Model Gym
- Rapid prototyping
- Standard models (CNNs, Transformers)
- Benchmarking baseline performance
- You want results quickly without deep backend knowledge

---

## When to Use Manual VGF Lowering
- Performance optimization is critical
- Debugging incorrect outputs or crashes
- Working with custom operators
- Backend development or research
- Needing explicit control over execution

---


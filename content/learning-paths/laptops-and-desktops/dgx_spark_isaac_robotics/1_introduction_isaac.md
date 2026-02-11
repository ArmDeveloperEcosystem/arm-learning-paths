---
title: Understand Isaac Sim and Isaac Lab for robotic workflows on DGX Spark
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path you will build, configure, and run robotic simulation and reinforcement learning (RL) workflows using NVIDIA Isaac Sim and Isaac Lab on an Arm-based DGX Spark system. The NVIDIA DGX Spark is a personal AI supercomputer powered by the GB10 Grace Blackwell Superchip, combining an Arm-based Grace CPU with a Blackwell GPU in a compact desktop form factor.

Isaac Sim and Isaac Lab are NVIDIA's core tools for robotics simulation and learning. Together they provide an end-to-end pipeline: simulate robots in physically accurate environments, train control policies using reinforcement learning, and evaluate those policies before deploying to real hardware.

This section introduces both tools and explains why the DGX Spark platform is an ideal development environment for these workloads.

## What is Isaac Sim?

[Isaac Sim](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html) is a robotics simulation platform built on NVIDIA Omniverse. It provides GPU-accelerated physics simulation to enable fast, realistic robot simulations that can run faster than real time.

Key capabilities of Isaac Sim include:

| **Capability** | **Description** |
|----------------|-----------------|
| Physics simulation | High-fidelity rigid body, articulation, and soft-body physics powered by NVIDIA PhysX |
| Sensor simulation | Simulated cameras, LiDAR, IMU, and contact sensors that generate realistic data streams |
| Photorealistic rendering | Ray-traced rendering for vision-based tasks, domain randomization, and synthetic data generation |
| Parallel environments | Run thousands of simulation instances simultaneously on a single GPU for massive data throughput |
| Python API | Full programmatic control of scenes, robots, and simulations through Python scripting |

Isaac Sim enables you to create detailed virtual worlds where robots can learn, be tested, and be validated without the cost, time, or risk of physical experiments.

## What is Isaac Lab?

[Isaac Lab](https://isaac-sim.github.io/IsaacLab/main/index.html) is a reinforcement learning framework built on top of Isaac Sim. It provides pre-built RL environments, training scripts, and evaluation tools for common robotics tasks such as locomotion, manipulation, and navigation.

Isaac Lab supports two task design workflows:

| **Workflow** | **Description** | **Best for** |
|--------------|-----------------|--------------|
| Manager-Based | Modular design where observations, actions, rewards, and terminations are defined through separate manager classes | Structured environments with reusable components |
| Direct | A single class defines the entire environment logic, similar to traditional Gymnasium environments | Rapid prototyping and full control over environment logic |

Isaac Lab integrates with multiple RL libraries out of the box:

| **RL Library** | **Supported Algorithms** |
|----------------|--------------------------|
| RSL-RL | PPO (Proximal Policy Optimization) |
| rl_games | PPO, LSTM, vision-based policies |
| skrl | PPO, IPPO, MAPPO, AMP (Adversarial Motion Priors) |
| Stable Baselines3 (sb3) | PPO |

In this Learning Path you will use the **RSL-RL** library, which is a lightweight and efficient PPO implementation commonly used for locomotion tasks.

## Why DGX Spark for robotic simulation?

The NVIDIA DGX Spark combines the Grace CPU and Blackwell GPU through a unified memory architecture, making it uniquely suited for robotics simulation and training workloads.

| **DGX Spark feature** | **Impact on robotics workflows** |
|------------------------|----------------------------------|
| Grace CPU (Arm Cortex-X925 / A725, 20 cores) | Handles environment orchestration, reward computation, and data preprocessing with high single-thread performance |
| Blackwell GPU (CUDA cores + 5th-gen Tensor Cores) | Accelerates physics simulation, parallel environment stepping, and neural network forward/backward passes |
| 128 GB unified memory (NVLink-C2C) | Eliminates CPU-GPU data transfer bottlenecks; simulation state and model weights share the same address space |
| NVLink-C2C (900 GB/s bidirectional) | Enables near-zero-latency communication between CPU-driven orchestration and GPU-driven simulation |
| Compact desktop form factor | Run data-center-class robotics workloads on your desk without remote cluster access |

Traditional robotics development requires separate machines for simulation, training, and deployment. DGX Spark consolidates these into a single platform. The unified memory is especially valuable for Isaac Sim, where physics state, rendered sensor data, and RL training tensors all reside in GPU-accessible memory without explicit copies.

## How Isaac Sim and Isaac Lab work together

The following describes the typical workflow when using Isaac Sim and Isaac Lab together on DGX Spark:

1. **Define the environment**: Isaac Lab provides pre-built environment configurations for common tasks (locomotion, manipulation, navigation). You can also create custom environments.
2. **Launch the simulation**: Isaac Sim initializes the physics engine, loads robot models (URDF/USD), and sets up the scene on the Blackwell GPU.
3. **Train a policy**: Isaac Lab's training scripts use RL algorithms (such as PPO via RSL-RL) to optimize a neural network policy. The GPU runs thousands of parallel environments simultaneously.
4. **Evaluate and iterate**: Trained policies can be tested in simulation with visualization enabled, or exported for deployment to real hardware.

The entire pipeline runs locally on DGX Spark. Headless mode (without visualization) maximizes GPU utilization for training, while visualization mode lets you inspect robot behavior interactively.

## Available environment categories

Isaac Lab ships with a comprehensive set of pre-built environments across several categories:

| **Category** | **Examples** | **Description** |
|--------------|-------------|-----------------|
| Classic | Cartpole, Ant, Humanoid | MuJoCo-style control benchmarks for algorithm development |
| Manipulation | Reach, Lift, Stack, Open-Drawer | Fixed-arm tasks using Franka, UR10, and other robots |
| Contact-rich Manipulation | Peg insertion, Gear meshing, Nut threading | Precision assembly tasks with the Franka robot |
| Locomotion | Anymal B/C/D, Unitree A1/Go1/Go2/H1/G1, Spot, Digit | Velocity tracking on flat and rough terrain for quadrupeds and humanoids |
| Navigation | Anymal C navigation | Point-to-point navigation with heading control |
| Multi-agent | Cart-Double-Pendulum, Shadow-Hand-Over | Tasks requiring coordination between multiple agents |

You can list all available environments on your installation by running:

```bash
./isaaclab.sh -p scripts/environments/list_envs.py
```

You can also filter by keyword:

```bash
./isaaclab.sh -p scripts/environments/list_envs.py --keyword locomotion
```

For the complete list of environments, see the [Isaac Lab Available Environments](https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html) documentation.

## What you will accomplish in this Learning Path

In the sections that follow you will:

1. **Set up Isaac Sim and Isaac Lab** on your DGX Spark by building both tools from source
2. **Run a basic robot simulation** in Isaac Sim and interact with it through Python
3. **Train a reinforcement learning policy** for the Unitree H1 humanoid robot on rough terrain using RSL-RL
4. **Explore advanced RL scenarios** including multiple task types, different robot configurations, and multi-agent training

By the end, you will have a fully functional Isaac Sim and Isaac Lab development environment on DGX Spark and hands-on experience with the complete robotics RL pipeline.

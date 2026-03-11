---
title: Explore Isaac Sim and Isaac Lab for robotic workflows on DGX Spark
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path, you will build, configure, and run robotic simulation and [reinforcement learning (RL)](https://en.wikipedia.org/wiki/Reinforcement_learning) workflows using NVIDIA Isaac Sim and Isaac Lab on an Arm-based DGX Spark system. The NVIDIA DGX Spark is a personal AI supercomputer powered by the GB10 [Grace Blackwell](https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_llamacpp/1_gb10_introduction/) Superchip. The system couples an Arm CPU cluster with a Blackwell GPU and a unified memory architecture to accelerate simulation orchestration, sensor preprocessing, physics, rendering, and RL training.

NVIDIA's Isaac Sim and Isaac Lab tools together provide an end-to-end robotics development workflow:
  1. Simulate robots in physically realistic environments.
  2. Train control policies using reinforcement learning.
  3. Evaluate trained policies before deployment to physical robots.
     
This section introduces both tools and explains how DGX Spark supports high-performance robotic simulation and RL experimentation.

## What is Isaac Sim?

[Isaac Sim](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html) is a robotics simulation platform built on NVIDIA Omniverse. It provides GPU-accelerated physics and rendering to enable high-fidelity robot simulation.

Core capabilities include:

| **Capability** | **Description** |
|----------------|-----------------|
| Physics simulation | High-fidelity rigid body, articulation, and soft-body physics powered by NVIDIA PhysX |
| Sensor simulation | Simulated cameras, LiDAR, IMU, and contact sensors that generate realistic data streams |
| Photorealistic rendering | Ray-traced rendering for vision-based tasks, domain randomization, and synthetic data generation |
| Parallel environments | Run thousands of simulation instances simultaneously on a single GPU for massive data throughput |
| Python API | Full programmatic control of scenes, robots, and simulations through Python scripting |

Isaac Sim lets you prototype and validate robot behavior in a controlled virtual environment before physical testing.

## What is Isaac Lab?

[Isaac Lab](https://isaac-sim.github.io/IsaacLab/main/index.html) is a reinforcement learning framework built on top of Isaac Sim. It provides pre-built RL environments, training scripts, and evaluation tools for common robotics tasks such as locomotion, manipulation, and navigation.

Isaac Lab supports two task design workflows:

| **Workflow** | **Description** | **Best for** |
|--------------|-----------------|--------------|
| Manager-Based | Modular environment components (observations, rewards, terminations) defined through separate manager classes | Structured environments with reusable components |
| Direct | A single class defines the entire environment logic, similar to traditional Gymnasium environments | Rapid prototyping and full control over environment logic |

Isaac Lab integrates with multiple reinforcement learning libraries, including:

| **RL Library** | **Supported Algorithms** |
|----------------|--------------------------|
| RSL-RL | PPO ([Proximal Policy Optimization](https://en.wikipedia.org/wiki/Proximal_policy_optimization)) |
| rl_games | PPO, LSTM, vision-based policies |
| skrl | PPO, IPPO, MAPPO, AMP (Adversarial Motion Priors) |
| Stable Baselines3 (sb3) | PPO |

In this Learning Path, you will use RSL-RL, a lightweight and efficient PPO implementation commonly used for locomotion training.

## Why DGX Spark for robotic simulation?

The NVIDIA DGX Spark combines the Grace CPU and Blackwell GPU through a unified memory architecture, making it uniquely suited for robotics simulation and training workloads.

| **DGX Spark feature** | **Impact on robotics workflows** |
|------------------------|----------------------------------|
| Grace CPU (Arm Cortex-X925 / A725, 20 cores) | Manages environment orchestration, reward calculation, and sensor data preprocessing with high single-thread performance |
| Blackwell GPU (CUDA cores + 5th-gen Tensor Cores) | Accelerates physics simulation, parallel environment stepping, and neural network forward/backward passes |
| 128 GB unified memory (NVLink-C2C) | Eliminates CPU-GPU data transfer bottlenecks; simulation state and model weights share the same address space |
| NVLink-C2C (900 GB/s bidirectional) | Enables near-zero-latency communication between CPU-driven orchestration and GPU-driven simulation |
| Compact desktop form factor | Run data-center-class robotics workloads on your desk without remote cluster access |

Traditional robotics development requires separate machines for simulation, training, and deployment. DGX Spark consolidates these into a single platform. The unified memory is especially valuable for Isaac Sim, where physics state, rendered sensor data, and RL training tensors all reside in GPU-accessible memory without explicit copies.

## How Isaac Sim and Isaac Lab work together

A typical robotics workflow using Isaac Sim and Isaac Lab on DGX Spark follows these steps:

1. **Define the environment**: Isaac Lab provides pre-built environment configurations for common tasks (locomotion, manipulation, navigation). You can also create custom environments tailored to specific robots or tasks.
2. **Launch the simulation**: Isaac Sim initializes the physics engine, loads the robot models (URDF/USD), and constructs the simulation scene. Physics simulation and rendering run on the Blackwell GPU.
3. **Train a policy**: Isaac Lab's training scripts use RL algorithms (such as PPO via RSL-RL) to optimize a neural network policy. The GPU runs thousands of parallel environments simultaneously.
4. **Evaluate and iterate**: Trained policies can be tested in simulation with visualization enabled or exported for deployment to real hardware.

The full workflow can run locally on a DGX Spark system. Running Isaac Sim in headless mode (without visualization) maximizes GPU utilization for training, while enabling visualization allows interactive inspection of robot behavior during debugging or validation.

## Available environment categories

Isaac Lab includes a large set of pre-built environments organized by task type:

| **Category** | **Examples** | **Description** |
|--------------|-------------|-----------------|
| Classic | Cartpole, Ant, Humanoid | MuJoCo-style control benchmarks for algorithm development |
| Manipulation | Reach, Lift, Stack, Open-Drawer | Fixed-arm tasks using Franka, UR10, and other robots |
| Contact-rich Manipulation | Peg insertion, Gear meshing, Nut threading | Precision assembly tasks with the Franka robot |
| Locomotion | Anymal B/C/D, Unitree A1/Go1/Go2/H1/G1, Spot, Digit | Velocity tracking on flat and rough terrain for quadrupeds and humanoids |
| Navigation | Anymal C navigation | Point-to-point navigation with heading control |
| Multi-agent | Cart-Double-Pendulum, Shadow-Hand-Over | Tasks that require coordination among multiple agents |

After installing Isaac Lab in the next section, you can list the available environments using:

```bash
./isaaclab.sh -p scripts/environments/list_envs.py
```
You can also filter environments by keyword. For example, to list locomotion environments:

```bash
./isaaclab.sh -p scripts/environments/list_envs.py --keyword locomotion
```

For the complete list of environments, see the [Isaac Lab Available Environments](https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html) documentation.

## What you will accomplish in this Learning Path

In this Learning Path you will:

1. **Set up Isaac Sim and Isaac Lab** on your DGX Spark by building both tools from source
2. **Run a basic robot simulation** in Isaac Sim and interact with it through Python
3. **Train a reinforcement learning policy** for the Unitree H1 humanoid robot on rough terrain using RSL-RL
4. **Explore additional RL environments** to understand how the workflow generalizes to other robots and tasks.

By the end of the Learning Path, you will have a working Isaac Sim and Isaac Lab development environment on DGX Spark and practical experience running a complete robotics reinforcement learning pipeline.

---
title: Scale reinforcement learning with multiple tasks and multi-agent training
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Scale reinforcement learning beyond single-task locomotion

In the previous section you trained a single locomotion policy using RSL-RL. Isaac Lab supports a much broader range of tasks and training paradigms. In this final section you will explore manipulation tasks, multi-agent environments, different RL libraries, and advanced training configurations that leverage the full capabilities of DGX Spark.

## Manipulation tasks

Beyond locomotion, Isaac Lab provides environments for robotic manipulation where arms and hands must grasp, lift, and place objects. These tasks use different robots and control modes.

### Reach task: move the end-effector to a target

The simplest manipulation task is reaching a target position. Train a Franka robot to reach:

```bash
cd ~/IsaacLab
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Reach-Franka-v0 \
    --headless \
    --num_envs=2048
```

In this task the Franka 7-DOF arm must move its end-effector to a randomly sampled target pose. The observation space includes joint positions, joint velocities, and the target position. The action space is joint position targets.

Evaluate the trained policy:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task=Isaac-Reach-Franka-Play-v0 \
    --num_envs=16
```

### Lift task: pick up a cube

A more challenging task combines reaching with grasping:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --headless \
    --num_envs=2048
```

The robot must approach a cube on a table, close its gripper to grasp it, and lift it to a target height. This task requires learning a sequence of skills: approach, align, grasp, and lift.

### Open-Drawer task: articulated object interaction

Train a Franka robot to open a cabinet drawer:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Open-Drawer-Franka-v0 \
    --headless \
    --num_envs=2048
```

This task adds the complexity of interacting with articulated objects. The robot must grasp the drawer handle and pull it open. The environment includes contact forces between the gripper and the handle.

### Comparison of manipulation tasks

| **Environment** | **Robot** | **Task** | **Difficulty** | **Key challenge** |
|----------------|----------|----------|---------------|-------------------|
| `Isaac-Reach-Franka-v0` | Franka | Reach a target pose | Easy | Inverse kinematics through RL |
| `Isaac-Reach-UR10-v0` | UR10 | Reach a target pose | Easy | Different robot kinematics |
| `Isaac-Lift-Cube-Franka-v0` | Franka | Pick up and lift a cube | Medium | Coordinating reach + grasp + lift |
| `Isaac-Open-Drawer-Franka-v0` | Franka | Open a cabinet drawer | Medium | Contact-rich manipulation |
| `Isaac-Stack-Cube-Franka-v0` | Franka | Stack three cubes | Hard | Long-horizon sequential skills |
| `Isaac-Repose-Cube-Allegro-v0` | Allegro Hand | In-hand cube reorientation | Hard | Dexterous multi-finger control |
| `Isaac-Repose-Cube-Shadow-Direct-v0` | Shadow Hand | In-hand cube reorientation | Very hard | 24-DOF dexterous manipulation |

## Contact-rich manipulation with Factory environments

Isaac Lab includes Factory environments for high-precision assembly tasks. These environments simulate contact forces with high fidelity:

```bash
# Peg insertion
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py \
    --task=Isaac-Factory-PegInsert-Direct-v0 \
    --headless

# Gear meshing
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py \
    --task=Isaac-Factory-GearMesh-Direct-v0 \
    --headless

# Nut threading
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py \
    --task=Isaac-Factory-NutThread-Direct-v0 \
    --headless
```

{{% notice Note %}}
Factory tasks use the `rl_games` library rather than `rsl_rl`. Isaac Lab provides separate training scripts for each supported RL library under `scripts/reinforcement_learning/`.
{{% /notice %}}

The following table shows the Factory tasks and their precision requirements:

| **Environment** | **Task** | **Precision required** |
|----------------|----------|----------------------|
| `Isaac-Factory-PegInsert-Direct-v0` | Insert a peg into a socket | Sub-millimeter alignment |
| `Isaac-Factory-GearMesh-Direct-v0` | Mesh a gear with other gears | Rotational and translational alignment |
| `Isaac-Factory-NutThread-Direct-v0` | Thread a nut onto a bolt | Precise torque and position control |

## Multi-agent reinforcement learning

Some robotic tasks require multiple agents to cooperate. Isaac Lab supports multi-agent training through the [skrl](https://skrl.readthedocs.io/) library using IPPO (Independent PPO) and MAPPO (Multi-Agent PPO) algorithms.

### Shadow Hand Over: passing objects between hands

This task requires two Shadow Hands to coordinate: one hand holds an object and passes it to the other:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Shadow-Hand-Over-Direct-v0 \
    --headless \
    --algorithm MAPPO
```

The key differences from single-agent training are:

| **Aspect** | **Single-agent** | **Multi-agent (MAPPO)** |
|-----------|-----------------|------------------------|
| Policy | One policy controls the entire robot | Each agent has its own policy (or shares one) |
| Observations | Global observation vector | Each agent sees its own local observations |
| Actions | Single action vector | Each agent produces its own actions |
| Training | Standard PPO | MAPPO uses a centralized critic with decentralized actors |
| Algorithm flag | Not needed | `--algorithm MAPPO` or `--algorithm IPPO` |

### Cart-Double-Pendulum: multi-agent classic control

A simpler multi-agent environment for testing:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Cart-Double-Pendulum-Direct-v0 \
    --headless \
    --algorithm IPPO
```

In this task, two agents control different joints of a cart-double-pendulum system and must coordinate to balance both pendulums.

{{% notice Note %}}
Multi-agent training is currently supported only through the skrl library. If you run multi-agent environments with other libraries (rsl_rl, rl_games, sb3), they are automatically converted to single-agent environments.
{{% /notice %}}

## Advanced locomotion: Adversarial Motion Priors (AMP)

For more natural and human-like robot motion, Isaac Lab supports Adversarial Motion Priors (AMP). AMP uses reference motion capture data to guide the RL policy toward realistic movements:

```bash
# Humanoid walking with AMP
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Humanoid-AMP-Walk-Direct-v0 \
    --headless \
    --algorithm AMP

# Humanoid running with AMP
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Humanoid-AMP-Run-Direct-v0 \
    --headless \
    --algorithm AMP

# Humanoid dancing with AMP
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Humanoid-AMP-Dance-Direct-v0 \
    --headless \
    --algorithm AMP
```

AMP adds a discriminator network that distinguishes between the agent's behavior and the reference motion data. The agent receives an additional reward for matching the reference style, producing more natural-looking locomotion.

| **AMP task** | **Reference motion** | **Result** |
|-------------|---------------------|-----------|
| `Isaac-Humanoid-AMP-Walk-Direct-v0` | Human walking capture | Natural walking gait |
| `Isaac-Humanoid-AMP-Run-Direct-v0` | Human running capture | Realistic running motion |
| `Isaac-Humanoid-AMP-Dance-Direct-v0` | Human dance capture | Creative dance movements |

## Using different RL libraries

Isaac Lab supports multiple RL libraries. Each library has its own training script and configuration format. The following shows how to train the same task with different libraries:

```bash
# RSL-RL (PPO) - lightweight, fast for locomotion
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Velocity-Rough-H1-v0 --headless

# rl_games (PPO) - feature-rich, supports LSTM and vision
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py \
    --task=Isaac-Velocity-Rough-Anymal-C-v0 --headless

# skrl (PPO) - modular, supports multi-agent and AMP
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Velocity-Rough-H1-v0 --headless

# Stable Baselines3 (PPO) - well-documented, Gymnasium compatible
./isaaclab.sh -p scripts/reinforcement_learning/sb3/train.py \
    --task=Isaac-Velocity-Flat-Unitree-A1-v0 --headless
```

### Library comparison

| **Library** | **Strengths** | **Best for** |
|------------|---------------|-------------|
| RSL-RL | Fast, minimal, efficient PPO | Locomotion tasks, quick experiments |
| rl_games | LSTM, vision encoders, Factory tasks | Complex observation spaces, contact-rich tasks |
| skrl | IPPO, MAPPO, AMP, modular design | Multi-agent tasks, imitation learning |
| Stable Baselines3 | Extensive documentation, Gymnasium API | Learning, prototyping, benchmarking |

## Multi-GPU training

For large-scale experiments, Isaac Lab supports multi-GPU training. DGX Spark has a single GPU, but if you connect two DGX Spark systems together (supported via NVLink) or use a multi-GPU workstation, you can distribute training:

```bash
# Multi-GPU training with PyTorch distributed
python -m torch.distributed.run --nnodes=1 --nproc_per_node=2 \
    scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Velocity-Rough-H1-v0 \
    --headless \
    --distributed
```

{{% notice Note %}}
Multi-GPU training requires additional setup. Refer to the [Isaac Lab Multi-GPU Training Guide](https://isaac-sim.github.io/IsaacLab/main/source/features/multi_gpu.html) for details. On a single DGX Spark, the Blackwell GPU is powerful enough for most locomotion and manipulation training tasks.
{{% /notice %}}

## Summary of all environment categories

The table below summarizes all the environment categories available in Isaac Lab, with example commands you can try on your DGX Spark:

| **Category** | **Example environment** | **Training command** |
|-------------|------------------------|---------------------|
| Classic control | `Isaac-Cartpole-Direct-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Cartpole-Direct-v0 --headless` |
| Locomotion (flat) | `Isaac-Velocity-Flat-Unitree-Go2-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Velocity-Flat-Unitree-Go2-v0 --headless` |
| Locomotion (rough) | `Isaac-Velocity-Rough-H1-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Velocity-Rough-H1-v0 --headless` |
| Manipulation (reach) | `Isaac-Reach-Franka-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Reach-Franka-v0 --headless` |
| Manipulation (lift) | `Isaac-Lift-Cube-Franka-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Lift-Cube-Franka-v0 --headless` |
| Contact-rich | `Isaac-Factory-PegInsert-Direct-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py --task=Isaac-Factory-PegInsert-Direct-v0 --headless` |
| Multi-agent | `Isaac-Shadow-Hand-Over-Direct-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py --task=Isaac-Shadow-Hand-Over-Direct-v0 --headless --algorithm MAPPO` |
| AMP (motion priors) | `Isaac-Humanoid-AMP-Walk-Direct-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py --task=Isaac-Humanoid-AMP-Walk-Direct-v0 --headless --algorithm AMP` |
| Navigation | `Isaac-Navigation-Flat-Anymal-C-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Navigation-Flat-Anymal-C-v0 --headless` |
| Dexterous manipulation | `Isaac-Repose-Cube-Allegro-v0` | `./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Repose-Cube-Allegro-v0 --headless` |

For the full list of over 100 environments, run:

```bash
./isaaclab.sh -p scripts/environments/list_envs.py
```

## What you have accomplished

You have completed this Learning Path on building robotic simulation and reinforcement learning workflows with Isaac Sim and Isaac Lab on DGX Spark.

Throughout this Learning Path you have learned how to:

- Describe the roles of Isaac Sim (physics simulation) and Isaac Lab (RL framework) and how the DGX Spark Grace-Blackwell architecture accelerates robotics workflows
- Build Isaac Sim and Isaac Lab from source on an Arm-based DGX Spark system, producing aarch64-optimized binaries
- Run basic robot simulations in Isaac Sim, including spawning robots and stepping physics
- Train a reinforcement learning policy for the Unitree H1 humanoid robot using PPO via RSL-RL, with a detailed understanding of every hyperparameter
- Explore manipulation tasks (reach, lift, open-drawer, stack), contact-rich assembly (Factory), and dexterous hand manipulation (Allegro, Shadow)
- Run multi-agent training with MAPPO and IPPO using the skrl library
- Use Adversarial Motion Priors (AMP) for natural humanoid locomotion
- Compare multiple RL libraries (RSL-RL, rl_games, skrl, Stable Baselines3) and understand when to use each one

The DGX Spark platform provides a complete environment for developing, training, and evaluating robotic control policies. The unified memory architecture and Blackwell GPU acceleration make it possible to run thousands of parallel simulation environments on a single desktop system, dramatically reducing the time from idea to trained policy.

For additional learning, see the resources in the Further Reading section. Continue experimenting with different environments, tuning hyperparameters, and exploring the Isaac Lab codebase to build increasingly sophisticated robotic AI systems.

---
title: Choose a reinforcement learning library for your task
description: Choose an Isaac Lab reinforcement learning library by matching its registered configurations and algorithms to your task.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose your technical toolkit

You've used RSL-RL for manipulation, RL Games for Factory, and `skrl` for Multi-Agent Proximal Policy Optimization (MAPPO) and Adversarial Motion Priors (AMP) tasks. Now, you'll compare why each task uses a different library.

Isaac Lab integrates several reinforcement learning libraries. Library choice affects the agent configuration, checkpoint format, and available algorithms.  Start with a library that has an upstream agent configuration for your task, then consider algorithm support and workflow needs. 

The following table summarizes four commonly used reinforcement learning libraries in Isaac Lab, with links to their repositories and the task profiles they fit best:

| Library | Core strength | Best fit |
|---|---|---|
| [RSL-RL](https://github.com/leggedrobotics/rsl_rl) | Efficient on-policy training | Locomotion and many manager-based tasks |
| [RL Games](https://github.com/Denys88/rl_games) | Recurrent-policy support | Factory tasks and other registered RL Games configurations |
| [`skrl`](https://github.com/Toni-SM/skrl) | MAPPO, Independent PPO (IPPO), and AMP support | Multi-agent and motion-prior tasks |
| [Stable Baselines3 (SB3)](https://github.com/DLR-RM/stable-baselines3) | Standardized algorithms and API | When the environment registers an SB3 configuration and supports baselines and prototyping |

{{% notice Tip %}}
No single library is the best choice for every task. A practical strategy is to start with the tool that helps you establish a baseline quickly, then move to a more specialized training stack when the task requires it.
{{% /notice %}}

## What you've accomplished

You've progressed from basic manipulation to workflow-level decisions for Isaac Lab on Arm. You've practiced task selection, library tradeoffs, MARL and AMP workflows, and when distributed training is worth considering.

Next, you can adapt these scripts as reference implementations for your own USD assets, robot models, scenes, and task constraints. Start with a single-GPU baseline, then expand only when workload scale requires it.


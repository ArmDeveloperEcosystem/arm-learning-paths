---
title: Choose an RL library
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## From task runner to workflow architect

You have used RSL-RL for manipulation, RL Games for Factory, and skrl for multi-agent and AMP tasks. Now compare why each task uses a different library.


## Choosing your technical toolkit

Isaac Lab integrates several RL libraries. Start with a library that has an upstream agent configuration for your task, then consider algorithm support and workflow needs.


## Library tradeoffs and decision guidance

The following table summarizes four commonly used RL libraries in Isaac Lab, with links to their repositories and the task profiles they fit best.

| Library | Core strength | Best fit |
|---|---|---|
| [**RSL-RL**](https://github.com/leggedrobotics/rsl_rl) | Efficient on-policy training | Locomotion and many manager-based tasks |
| [**RL Games**](https://github.com/Denys88/rl_games) | Recurrent-policy support | Factory tasks and other registered RL Games configurations |
| [**skrl**](https://github.com/Toni-SM/skrl) | MAPPO, IPPO, and AMP support | Multi-agent and motion-prior tasks |
| [**Stable Baselines3**](https://github.com/DLR-RM/stable-baselines3) | Standardized algorithms and API | Supported baselines and prototyping |

### Choose based on task and workflow needs

Use a first-pass mapping from task needs to library behavior:

* Use **RSL-RL** for the Franka and locomotion configurations used in these Learning Paths.
* Use **RL Games** for the upstream Factory configurations.
* Use **skrl** for MAPPO, IPPO, or AMP.
* Use **Stable Baselines3** when the task provides an SB3 configuration and you want its standard API.

Library choice affects the agent configuration, checkpoint format, and available algorithms. Use the configuration registered for the selected task rather than assuming every library supports every environment.


## Mapping libraries to task types

To make the decision more concrete, the following table maps the task categories from the earlier sections to common library choices.

| Task type | Suggested library | Why |
|---|---|---|
| Franka Reach, Lift, and Open-Drawer | **RSL-RL** | Upstream PPO configurations are registered for these tasks |
| Factory peg insertion | **RL Games** | The Factory task registers an RL Games PPO configuration |
| Multi-agent object handover | **skrl** | The task registers MAPPO and IPPO configurations |
| Humanoid AMP Walk, Run, and Dance | **skrl** | These tasks register skrl AMP configurations |
| Supported baseline comparisons | **Stable Baselines3** | Use only when the environment registers an SB3 configuration |

{{% notice Tip %}}
No single library is the best choice for every task. A practical strategy is to start with the tool that helps you establish a baseline quickly, then move to a more specialized training stack when the task requires it.
{{% /notice %}}


## Scaling up: multi-GPU distributed training

DGX Spark has one GPU, so run the earlier tasks as single-GPU jobs. If you move the same checkout to a system with two GPUs, Isaac Lab supports distributed training.

### Run

PyTorch's distributed launcher creates one process per GPU. Replace `<example task>` with the task to train on a two-GPU system:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
python -m torch.distributed.run --nnodes=1 --nproc_per_node=2 \
    scripts/reinforcement_learning/rsl_rl/train.py \
    --task=<example task> \
    --headless \
    --distributed
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
python -m torch.distributed.run --nnodes=1 --nproc_per_node=2 \
    scripts/reinforcement_learning/train.py \
    --rl_library rsl_rl \
    --task=<example task> \
    --viz none \
    --distributed
{{< /tab >}}
{{< /tabpane >}}

For multi-node options and NCCL troubleshooting, use the guide for [Isaac Lab 2.3.2](https://isaac-sim.github.io/IsaacLab/v2.3.2/source/features/multi_gpu.html) or [Isaac Lab 3.0 Beta 2](https://isaac-sim.github.io/IsaacLab/release/3.0.0-beta2/source/features/multi_gpu.html).



## What you've learned and what's next

You progressed from basic manipulation to workflow-level decisions for Isaac Lab on Arm. You practiced task selection, library tradeoffs, MARL and AMP workflows, and when distributed training is worth considering.

Next, adapt these scripts as reference implementations for your own USD assets, robot models, scenes, and task constraints. Start with a single-GPU baseline, then expand only when workload scale requires it.

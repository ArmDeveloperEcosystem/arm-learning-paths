---
title: Choosing RL Libraries
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## From task runner to workflow architect

In the previous sections, you used an Arm-based Isaac Sim / Isaac Lab environment for manipulation, contact-rich interaction, multi-agent training, and AMP-based motion. Now move from running tasks to designing the workflow.

**Given your task characteristics, which RL library should you choose, and how should you scale the workflow from one platform?**


## Choosing your technical toolkit

One of Isaac Lab's main strengths is that it is not tied to a single RL framework. Instead, it provides an open and extensible ecosystem, allowing you to choose different RL libraries and training entry points depending on the problem you want to solve.

For an architect, this choice is mostly about tradeoffs. Different tasks impose different requirements for throughput, observation complexity, algorithm features, debugging convenience, and extensibility. It directly affects how fast you can iterate and how well the workflow scales for your specific use case. Choose an RL library for an Isaac Lab workflow based on task type and development goals.


## Library tradeoffs and decision guidance

The following table summarizes four commonly used RL libraries in Isaac Lab, with links to their repositories and the task profiles they fit best.

| Library | Core strength | Best fit |
|---|---|---|
| [**RSL-RL**](https://github.com/leggedrobotics/rsl_rl) | Lightweight, fast, memory-efficient | Locomotion, fast iteration, large parallel training |
| [**rl_games**](https://github.com/Denys88/rl_games) | Supports LSTM and visual encoders | Complex observation spaces, contact-rich manipulation, Factory tasks |
| [**skrl**](https://github.com/Toni-SM/skrl) | Modular design with MARL and AMP support | Multi-agent training, natural-motion imitation, flexible workflow extension |
| [**Stable Baselines3**](https://github.com/DLR-RM/stable-baselines3) | Strong documentation and standardized API | Teaching, prototyping, baseline comparison |

### Choose based on task and workflow needs

Use a first-pass mapping from task needs to library behavior:

* For maximum training speed and throughput, start with **RSL-RL**.
* For complex observations or recurrent policies, use **rl_games**.
* For multi-agent workflows or AMP-style training, use **skrl**.
* For educational baselines and standardized comparisons, use **Stable Baselines3**.

In Isaac Lab, this choice also affects scripts, configuration style, and experiment structure. On Arm-based systems, this workflow is practical because you can switch stacks through script entry points and CLI flags. Unified memory also helps startup because simulation and learning can avoid host-to-device transfers. Because CPU and GPU share one memory pool, each side can use more or less memory as needed for better throughput, instead of hitting bottlenecks from fixed per-device limits. Environment count can then scale to use much of the available 128 GB memory.


## Mapping libraries to task types

To make the decision more concrete, the following table maps the task categories from the earlier sections to common library choices.

| Task type | Suggested library | Why |
|---|---|---|
| Franka Reach / Lift and other basic manipulation tasks | **RSL-RL** | Simple setup and good for fast baselines with large parallel rollout |
| Drawer / Factory and other contact-rich tasks | **rl_games** | Better suited for more complex observation and policy structures |
| Multi-agent object handover | **skrl** | A more natural fit for MARL workflows |
| Humanoid AMP Walk / Run / Dance | **skrl** | Direct fit for AMP-style algorithms and natural-motion tasks |
| Educational examples and standard RL baselines | **Stable Baselines3** | Standardized API and easy comparison workflow |

{{% notice Tip %}}
No single library is the best choice for every task. A practical strategy is to start with the tool that helps you establish a baseline quickly, then move to a more specialized training stack when the task requires it.
{{% /notice %}}


## Scaling up: multi-GPU distributed training

Most readers in this Learning Path use one GPU, and that setup is already enough for many manipulation and locomotion tasks. If you later move to multi-GPU systems, distributed training can improve throughput for very large workloads.

### Run

`torch.distributed.run` is PyTorch's distributed launcher. It creates one process per GPU and coordinates rank-to-rank communication so all workers train synchronously. The following example is for one node with two GPUs:

If your setup includes multiple networked systems, the same pattern extends to clusters, for example Grace Hopper servers or DGX Spark systems connected over a high-speed network. In those cases, `--nnodes` and rank settings are expanded to span the full cluster.

{{< tabpane code=true >}}
{{< tab header="IsaacLab 2.3 API" >}}
python -m torch.distributed.run --nnodes=1 --nproc_per_node=2 \
    scripts/reinforcement_learning/rsl_rl/train.py \
    --task=<example task> \
    --headless \
    --distributed
{{< /tab >}}
{{< tab header="IsaacLab 3.0 API" >}}
python -m torch.distributed.run --nnodes=1 --nproc_per_node=2 \
    scripts/reinforcement_learning/train.py \
    --rl_library rsl_rl \
    --task=<example task> \
    --viz none \
    --distributed
{{< /tab >}}
{{< /tabpane >}}

This command defines the training entry point, worker-process count, distributed mode, and task selection in one place. In this workflow, the CPU side handles launch and orchestration while GPUs handle simulation and learning throughput.



## What you've learned and what's next

You progressed from basic manipulation to workflow-level decisions for Isaac Lab on Arm. You practiced task selection, library tradeoffs, MARL and AMP workflows, and when distributed training is worth considering.

Next, adapt these scripts as reference implementations for your own USD assets, robot models, scenes, and task constraints. Start with a single-GPU baseline, then expand only when workload scale requires it.

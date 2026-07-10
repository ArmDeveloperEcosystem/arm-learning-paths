---
title: Multi-Agent Training
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## From working alone to working together with MAPPO

In the previous section, you used an Arm-based Isaac Sim / Isaac Lab environment to run single-arm manipulation and contact-rich tasks. This section continues on the same development platform and moves into **multi-agent reinforcement learning (MARL)**, where multiple agents learn to cooperate inside the same simulation.

In real logistics centers, automated production lines, and dual-arm robotics systems, a single agent is often not enough. A task may require two hands to transfer an object, multiple controllers to stabilize a system, or several agents to coordinate under partial observation. The challenge is no longer only about controlling one robot correctly. It is about **coordination, role allocation, and shared task success**.

In this section, you will use the **skrl** library with **MAPPO** (Multi-Agent Proximal Policy Optimization). MAPPO trains agents using a shared critic that incorporates global state information during training, while each agent still executes independently using only its own local observations at deployment. 

Isaac Lab also supports **IPPO** (Independent PPO), where each agent treats all other agents as part of the environment and learns entirely independently. IPPO works well when agents have clearly separated roles, limited interaction, or when you want to avoid the added complexity of centralized training. If you want to experiment with IPPO or explore other multi-agent environments, the [comprehensive list of Isaac Lab environments](https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html#comprehensive-list-of-environments) shows which tasks support which algorithms.

As in the earlier section, this section also highlights how Arm-based systems enable **workflow control**. You can use Python scripts, task flags, and algorithm options to control multi-agent training flows, switch configurations, and continue running GPU-backed simulation on the same platform.

## Shadow Hand Over — coordinated transfer between hands

In this task, the policy must solve a classic cooperation scenario. One Shadow Hand holds an object and transfers it to the other hand. Each agent controls only its own motion but must learn to anticipate the other agent's behavior and timing from partial local observations. MAPPO is well suited for this task because the shared critic can encourage coordinated behavior during training, even though each hand uses only local observations during execution.

### Run

You'll now use the **skrl** library for multi-agent training. Pass the `--algorithm` flag to select MAPPO for this task:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Shadow-Hand-Over-Direct-v0 \
    --headless \
    --algorithm MAPPO
```

This command loads the task, selects the MAPPO training algorithm, and runs the simulation headless. Like earlier tasks, the Python entry point controls task and algorithm selection, letting you switch workflows without any recompilation.

{{% notice Please Note %}}

Training this task can take up to **30 minutes** on a DGX Spark. 

If you want to run the model from a pre-trained checkpoint available from NVIDIA Omniverse. You can optionally skip this training part and move to the verify section. When running the `play.py` script you will need to replace the 

```bash
--checkpoint=<path_to_your_factory_model.pth>
```

with

```bash
--use_pretrained_checkpoint
```

Please note that there may not be a model available from NVIDIAs Omniverse for your specific task and `IsaacLab` version tag. 
{{% /notice %}}


### Verify

After training, look for the following behaviors:

* The two hands coordinate rather than moving independently.
* The hand holding the object adjusts its pose to create a feasible transfer path.
* Drops, collisions, and action conflicts decrease as training progresses.

To view the trained policy, replace the checkpoint path with your trained model directory and run:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/skrl/play.py \
    --task=Isaac-Shadow-Hand-Over-Direct-v0 \
    --num_envs=1 \
    --algorithm=MAPPO \
    --real-time \
    --checkpoint=<path_to_your_best_agent.pt>
```

![Shadow Hand Over training progress showing two dexterous hands coordinating an object transfer. The left panel shows early training (iteration 3600) where motion is uncoordinated and the object is still held. The right panel shows the policy at convergence using the best_agent.pt checkpoint identified by skrl, where the hands smoothly coordinate the handover.#center](./multi_agent_hand.gif "Shadow Hand Over training progression. Left: iteration 3600. Right: best_agent.pt.")

### Optional: Try IPPO and experiment with model size

You can also try training an example using the IPPO (Independent Proximal Policy Optimization) algorithm. To do this, change the `--algorithm` flag to `IPPO` in your training command:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task=Isaac-Shadow-Hand-Over-Direct-v0 \
    --headless \
    --algorithm IPPO
```

IPPO treats each agent as independent, which can be useful for tasks where agents have separate roles or limited interaction. For further exploration, try altering the model size or network architecture in your training configuration. Experimenting with different model sizes can help you understand the trade-offs between training speed, memory usage, and policy performance.

For more environments and supported algorithms, see the [comprehensive list of Isaac Lab environments](https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html#comprehensive-list-of-environments).

## Core comparison: single-agent vs multi-agent training

When you move from single-agent tasks to multi-agent training, the change is not just about adding more controllers. The problem definition itself becomes different.

| Feature | Single-agent | Multi-agent (MAPPO / IPPO) |
| --- | --- | --- |
| Policy | One policy controls the whole robot | Each agent has its own policy, or partially shared policies |
| Observations | Often one observation vector | Each agent receives its own local observations |
| Actions | One action vector | Each agent outputs its own actions |
| Training paradigm | Standard PPO or other single-agent RL | Centralized training with decentralized execution, or independent learning |
| Algorithm flag | Usually not required | Selected with `--algorithm MAPPO` or optionally `--algorithm IPPO` |

{{% notice Note %}}
In Isaac Lab, multi-agent training is currently driven mainly by the **skrl** library. If you try to run a multi-agent environment with another library such as **rsl_rl**, the task may fall back to a single-agent mode or lack full multi-agent support.
{{% /notice %}}

## Wrap-up

This section showed the main shift from single-agent control to multi-agent cooperation in Isaac Lab. Instead of focusing only on whether one robot moves correctly, you now have to think about how multiple agents form a coordinated strategy under partial information.

On an Arm-based system, the key value in this section is not raw CPU performance. It is the ability of the **Arm CPU to control the overall simulation workflow**. Through Python scripts, task options, and algorithm flags, you can switch multi-agent scenarios quickly and continue developing, training, and comparing workflows on the same platform.

## Next up

Your robots can now perform precise actions and even cooperate, but the resulting motion may still look rigid. For humanoid robots that must coexist with people, moving in a more natural way is another important challenge.

In the next section, you will explore **AMP (Adversarial Motion Priors)** and learn how robots can use reference motion data to produce more natural and fluent behavior.
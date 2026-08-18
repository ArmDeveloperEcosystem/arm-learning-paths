---
title: Fine manipulation and contact-rich interaction
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Move from grasping to constrained motion

In the previous section, you trained the Franka arm to reach and lift. You will now use the same Isaac Sim and Isaac Lab setup for constrained, contact-rich tasks.

In industrial environments, a robot does more than pick up free objects. Drawers move along rails, pegs fit into tight sockets, and nuts must align with bolts. These tasks add contact, constrained motion, and failure modes caused by small errors.

Start with an articulated drawer, then move to a Factory peg-insertion environment.

## Task 1: Open-Drawer

In this task, you train the same Franka arm to reach the drawer handle, grasp it, and pull the drawer open along its rail. Unlike the Lift task from the previous section, a drawer is an articulated object: it is made of linked parts connected by a joint, so it can move only along a defined path (the rail) instead of moving freely in any direction. The policy must handle stable contact, constrained motion, and contact forces throughout the interaction.

### Run

From the Isaac Lab directory, run the RSL-RL training command:

```console
cd ~/IsaacLab
```

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Open-Drawer-Franka-v0 \
    --headless \
    --num_envs=2048
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh train \
    --rl_library rsl_rl \
    --task=Isaac-Open-Drawer-Franka-v0 \
    --viz none \
    --num_envs=2048
{{< /tab >}}
{{< /tabpane >}}

{{% notice Note %}}

The Open-Drawer PPO configuration uses `[256, 128, 64]` actor and critic networks and collects 96 steps per environment per iteration. Reach collects 24.

Training will take approximately 25 minutes on a DGX Spark. 

{{% /notice %}}

### What makes this task harder

The policy must align the gripper with the handle, establish contact, and pull along the drawer rail. The task observations include robot joint state, drawer joint state, the relative end-effector position, and the previous action.

### Verify

After training, confirm the following:

* The robotic arm approaches and aligns with the handle instead of stopping in front of the drawer.
* Once contact is established, the drawer moves along the rail direction.
* The opening motion remains stable without slipping, shaking, or applying force in the wrong direction.

Set `--checkpoint` to the model file you want to evaluate:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task=Isaac-Open-Drawer-Franka-v0 \
    --num_envs=1 \
    --checkpoint=<path_to_checkpoint>
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh play \
    --rl_library rsl_rl \
    --task=Isaac-Open-Drawer-Franka-v0 \
    --num_envs=1 \
    --checkpoint=<path_to_checkpoint>
{{< /tab >}}
{{< /tabpane >}}

![Drawer-opening policy progression shown side by side. The left panel shows early training (iteration 50) with slow and unstable drawer motion. The right panel shows converged policy (iteration 399) with reliable contact and smooth opening along the rail.#center](./open_drawer.gif "Drawer-opening policy progression shown side by side. The left panel shows early training (iteration 50) with slow and unstable drawer motion. The right panel shows converged policy (iteration 399) with reliable contact and smooth opening along the rail")


## Task 2: Factory environments — perform peg insertion

Isaac Lab's Factory environments cover peg insertion, gear meshing, and nut threading. Here, you will train peg insertion with RL Games. The task uses tight-clearance geometry and contact simulation, so small pose errors can prevent insertion.

### Run

Select the API version installed on your system:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py \
    --task=Isaac-Factory-PegInsert-Direct-v0 \
    --headless
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh train \
    --rl_library rl_games \
    --task=Isaac-Factory-PegInsert-Direct-v0 \
    --viz none
{{< /tab >}}
{{< /tabpane >}}

Training runs for the `max_epochs` value in `source/isaaclab_tasks/isaaclab_tasks/direct/factory/agents/rl_games_ppo_cfg.yaml`. The output is similar to:

```output
fps step: 408 fps step and policy inference: 401 fps total: 332 epoch: 33/200 frames: 524288
saving next best rewards: [300.05377]
=> saving checkpoint '<checkpoint_path>'
```

`fps total` reports overall throughput, `epoch` shows training progress, and `frames` counts environment transitions processed.



{{% notice Note %}}

In the authors' testing, this task took up to one hour on DGX Spark.

To try a published checkpoint, add `--use_pretrained_checkpoint` to the play command instead of training first.

A checkpoint might not be available for every task and Isaac Lab version.

{{% /notice %}}

## Verify

Set `--checkpoint` to a local checkpoint, or replace it with `--use_pretrained_checkpoint`. The additional environment parameters make the peg insertion quicker to observe:


{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/play.py \
  --task=Isaac-Factory-PegInsert-Direct-v0 \
  --checkpoint=<path_to_checkpoint> \
  --num_envs=1 \
  --real-time \
  --seed=-1 \
  env.episode_length_s=4.0 \
  env.task.fixed_asset_init_pos_noise=[0.08,0.08,0.02] \
  env.task.hand_init_pos_noise=[0.03,0.03,0.02]
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh play \
  --rl_library rl_games \
  --task=Isaac-Factory-PegInsert-Direct-v0 \
  --checkpoint=<path_to_checkpoint> \
  --num_envs=1 \
  --real-time \
  --seed=-1 \
  env.episode_length_s=4.0 \
  env.task.fixed_asset_init_pos_noise=[0.08,0.08,0.02] \
  env.task.hand_init_pos_noise=[0.03,0.03,0.02]
{{< /tab >}}
{{< /tabpane >}}

![Franka arm inserting a peg into a tight-clearance socket after 50 PPO training epochs.#center](./peg.gif "Peg insertion after 50 PPO training epochs")


### What changes in the workflow

You changed both the task and the RL library without rebuilding Isaac Lab. The command-line interface selects the registered task and its matching agent configuration.


### Why these tasks matter

Factory tasks are common in industrial automation and assembly scenarios. They are challenging because:

* alignment tolerances are very small
* contact behavior is sensitive to small pose errors
* position, orientation, and contact dynamics become tightly coupled

For example, peg insertion requires stable alignment before insertion, while nut threading adds even more demanding pose control and rotational behavior. These tasks are usually much more sensitive to small errors than Reach, Lift, or drawer interaction.

## Compare manipulation tasks

Each task adds a different control challenge:

| Environment | Task | Added challenge |
|---|---|---|
| Isaac-Reach-Franka-v0 | Reach a target pose | Track a sampled target pose |
| Isaac-Open-Drawer-Franka-v0 | Open a drawer | Maintain contact while following a mechanical constraint |
| Isaac-Factory-NutThread-Direct-v0 | Thread a nut onto a bolt | Control precise alignment and rotation |

The progression moves from free-space control to articulated objects and precision assembly.


## Next up

A single robotic arm can already complete more precise interactions, but more complex automation scenarios often require multiple agents working together.

In the next section, you will move beyond single-robot operation and explore how multiple robotic agents can cooperate to complete a task.

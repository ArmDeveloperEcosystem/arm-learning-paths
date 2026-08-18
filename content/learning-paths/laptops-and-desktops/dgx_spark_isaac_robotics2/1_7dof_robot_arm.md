---
title: Manipulate objects with a 7-DOF robot arm
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## From locomotion to interaction

Complete the previous [Isaac Sim and Isaac Lab Learning Path](https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_isaac_robotics/) before continuing. It builds Isaac Sim, installs Isaac Lab, and configures both on an Arm-based [DGX Spark](https://www.nvidia.com/en-gb/products/workstations/dgx-spark/) system.

{{% notice Isaac Lab API versions %}}

Use one compatible version set throughout this Learning Path:

| Command tab | Isaac Lab | Isaac Sim | Python |
|---|---|---|---|
| Isaac Lab 2.3 API | `v2.3.2` | 5.1.0 | 3.11 |
| Isaac Lab 3.0 API | `v3.0.0-beta2.patch1` | 6.0.0 or 6.0.1 | 3.12 |

For a direct continuation from the previous Learning Path, use the 2.3 tab. Use the 3.0 tab only if you installed the [3.0 Beta 2 release](https://isaac-sim.github.io/IsaacLab/release/3.0.0-beta2/source/setup/installation/index.html).

The previous Learning Path installs packages into the Isaac Sim Python environment, so there is no virtual environment to activate. Restore its environment variables and check the installed versions before selecting a tab:

```console
source ~/.bashrc
cd ~/IsaacLab
git describe --tags --always
head -n 1 "${ISAACSIM_PATH}/VERSION"
"${ISAACSIM_PYTHON_EXE}" --version
```

If the versions don't match a row, follow the documentation for your installed release before continuing. Isaac Lab 3.0 uses the unified `train` and `play` commands shown in the 3.0 tabs.

{{% /notice %}}


You will train policies for a seven-degree-of-freedom Franka arm on two tasks:

* **Reach** - Move the arm's end effector to a target pose
* **Lift** - Grasp a cube and move it to a target position

These tasks continue the same source-built Isaac Sim and Isaac Lab workflow used in the previous Learning Path.


## Task 1: Reach — build spatial control

The Reach task trains the Franka arm to move its end-effector to a randomly sampled target pose. This is your first manipulation baseline because it teaches position control before adding grasping.

### Run

Use your existing Isaac Lab setup from the previous Learning Path, then run:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
cd ~/IsaacLab

# Improve runtime compatibility on aarch64 systems
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"

./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Reach-Franka-v0 \
    --headless \
    --num_envs=2048
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
cd ~/IsaacLab

# Improve runtime compatibility on aarch64 systems
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"

./isaaclab.sh train \
    --rl_library rsl_rl \
    --task=Isaac-Reach-Franka-v0 \
    --viz none \
    --num_envs=2048
{{< /tab >}}
{{< /tabpane >}}



This training flow uses the RSL-RL implementation of proximal policy optimization (PPO). Its hyperparameters and actor-critic network sizes are defined in `source/isaaclab_tasks/isaaclab_tasks/manager_based/manipulation/<task>/config/franka/agents/rsl_rl_ppo_cfg.py`.

In these config files, the example PPO model sizes are:

* Reach actor and critic: `[64, 64]`
* Lift actor and critic: `[256, 128, 64]`

The default training iterations are:

* Reach: `1000` iterations
* Lift: `1500` iterations

Training the simple reach task on the DGX Spark will take approximately 10 minutes. 


### What this script controls

The entry point controls:

* The task configuration
* The RL library
* Runtime options such as visualization and environment count

An *environment* is one simulated task instance. With `--num_envs=2048`, Isaac Lab runs 2048 Franka arms and targets in parallel. PPO uses their combined trajectories to update the actor and critic each iteration.


### Task structure

* **Goal**: Move the Franka end effector to a sampled target pose
* **Observations**: Joint positions, joint velocities, target pose, and previous action
* **Actions**: Joint position targets

### Verify

Set `--checkpoint` to the model file you want to evaluate. Two environments keep the simulation quick to load:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task=Isaac-Reach-Franka-Play-v0 \
    --num_envs=2 \
    --checkpoint=logs/rsl_rl/franka_reach/<run_timestamp>/model_<iteration>.pt
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh play \
    --rl_library rsl_rl \
    --task=Isaac-Reach-Franka-Play-v0 \
    --num_envs=2 \
    --checkpoint=logs/rsl_rl/franka_reach/<run_timestamp>/model_<iteration>.pt
{{< /tab >}}
{{< /tabpane >}}

{{% notice Tip %}}

To inspect the Franka arm, right-click in the viewport and use `W`, `A`, `S`, and `D` to fly the camera. These are standard industry viewport navigation controls used in many 3D tools.

{{% /notice %}}

![Franka Reach training comparison that shows early and late policy behavior. The left side shows less stable motion around iteration 100, and the right side shows improved target tracking near iteration 999.#center](./reach.gif "Franka reach training comparison that shows early and late policy behavior. The left side shows less stable motion around iteration 100, and the right side shows improved target tracking near iteration 999")

You should observe the following:

* The robotic arm can consistently move its end-effector to the target position.
* Multiple environments execute the reaching behavior in parallel.
* The policy no longer shows obvious random oscillation or unstable motion.

### Why it matters on Arm

The coherent unified memory lets you quickly start and stop training with little data transfer overhead and flexibly scale memory for large environments. The Arm CPU orchestrates training, enabling rapid experimentation and iteration.


## Task 2: Lift — balancing force and precision

Once the robot can reach reliably, the next step is physical interaction. In the Lift task, you train the arm to grasp a cube on the table and lift it to a target height. The policy must coordinate approach, alignment, gripper closure, and stable lifting under contact and gravity. Run the following command to train the `Isaac-Lift-Cube-Franka-v0` task with the PPO algorithm from the `rsl_rl` library.

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --headless \
    --num_envs=2048
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh train \
    --rl_library rsl_rl \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --viz none \
    --num_envs=2048
{{< /tab >}}
{{< /tabpane >}}

{{% notice Note %}}

After an initial run, the end-effector might still fail to lift consistently. To continue training from a checkpoint rerun with the additional arguments shown below:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
  --task=Isaac-Lift-Cube-Franka-v0 \
  --headless \
  --num_envs=2048 \
  --resume \
  --experiment_name=franka_lift \
  --load_run=<run_timestamp_folder> \
  --checkpoint=model_<iteration>.pt \
  --max_iterations=<additional_iterations>
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh train \
  --rl_library rsl_rl \
  --task=Isaac-Lift-Cube-Franka-v0 \
  --viz none \
  --num_envs=2048 \
  --resume \
  --experiment_name=franka_lift \
  --load_run=<run_timestamp_folder> \
  --checkpoint=model_<iteration>.pt \
  --max_iterations=<additional_iterations>
{{< /tab >}}
{{< /tabpane >}}

Use the run folder format `YYYY-MM-DD_HH-MM-SS` for `--load_run` (note the underscore between date and time), for example `2026-05-15_09-24-13`.

{{% /notice %}}

The training log prints a **learning-iteration summary** each cycle:

```output
Learning iteration 902/2650
Episode_Reward/lifting_object: 11.2984
ETA: 00:23:11
```

Watch `Episode_Reward/lifting_object` to assess whether the policy is learning to lift the cube without explicitly running a visual simulation of the model. You can see jumps and plateaus during PPO training, so short flat periods are normal. Use the broader trend across many iterations, together with ETA, to decide whether to keep training.

### What changes in the workflow

Compared with Reach, you do not rebuild the project or switch platforms. You keep the same training entry point and environment, and only change `--task`. That lets you move quickly between manipulation scenarios while keeping the same workflow.

### Verify

After training, confirm the following:

* The robotic arm can approach the cube and adjust its gripper position.
* The gripper closes at an appropriate time.
* The cube is lifted off the table rather than slipping away or bouncing after collision.


Set `--checkpoint` to the model file you want to evaluate:

{{< tabpane code=true >}}
{{< tab header="Isaac Lab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --num_envs=2 \
    --checkpoint=<path_to_checkpoint>
{{< /tab >}}
{{< tab header="Isaac Lab 3.0 API" >}}
./isaaclab.sh play \
    --rl_library rsl_rl \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --num_envs=2 \
    --checkpoint=<path_to_checkpoint>
{{< /tab >}}
{{< /tabpane >}}

![Franka 7-DOF arm progressing through Reach and Lift. The left panel shows iteration 150, where grasp stability is still developing. The right panel shows around iteration 900, where the policy keeps the end-effector inverted to reduce cube drops during lifting.#center](./reach_and_lift.gif "Franka 7-DOF arm progressing through Reach and Lift. The left panel shows iteration 150, where grasp stability is still developing. The right panel shows around iteration 900, where the policy keeps the end-effector inverted to reduce cube drops during lifting")


## Next up

The Franka robotic arm now has basic grasping ability. However, objects in the real world often introduce more complex mechanical constraints.

In the next section, you will explore how a robot can interact with joint-constrained objects such as drawers, and move one step closer to high-precision industrial manipulation tasks.

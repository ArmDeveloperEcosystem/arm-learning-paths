---
title: Manipulate Objects with a 7-DOF Robot Arm
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## From locomotion to interaction

Use the installation instructions in the previous [Learning Path](https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_isaac_robotics/)to  installed and run [Isaac Sim](https://developer.nvidia.com/isaac/sim) and [Isaac Lab](https://developer.nvidia.com/isaac/lab) on an Arm-based [DGX Spark](https://www.nvidia.com/en-gb/products/workstations/dgx-spark/) system. 

{{% notice IsaacLab API versions %}}

As of July 2026, support for **IsaacSim 6.0.0 and later** through IsaacLab is still in beta. For the most stable experience with this learning path, use **IsaacLab 2.3.2** with **IsaacSim 5.1.0**.

Before installing, verify that your chosen **IsaacLab** version is compatible with **IsaacSim** using the version compatibility table in the IsaacLab [README.md](https://github.com/isaac-sim/IsaacLab/blob/main/README.md). If you choose different versions, follow the compatibility table rather than assuming that the latest IsaacLab and IsaacSim releases work together.

The command examples provide tabs for both the **IsaacLab 2.3 API** and the **IsaacLab 3.0 API**. The IsaacLab 3.0 commands are included for future-proofing as support for IsaacSim 6.0.0 and later matures. They use the use the unified `train` and `play` entry points described in the [IsaacLab 3.0 Migration Guide](https://isaac-sim.github.io/IsaacLab/develop/source/migration/migrating_to_isaaclab_3-0.html).

Additionally, IsaacLab 3.0.0 and newer require **Python 3.12 or later** to build and install all required Python packages. You may need to upgrade your system Python version before continuing.

{{% /notice %}}


In this section, you move from locomotion to manipulation. You will train a simulation model of the [Franka 3](https://franka.de/franka-research-3) robotic arm with 7 Degrees-of-freedom (DOF) on two tasks:

* **Reach** - to build spatial control of the arm's end effector, the part that interacts with the environment.
* **Lift** - to further add contact, grasping, and stable object motion.

This workflow also shows how DGX Spark maps work across CPU and GPU resources. DGX Spark provides 128 GB of coherent unified LPDDR5X memory shared by the Arm CPUs (10 Cortex-X925 and 10 Cortex-A725 cores) and the Blackwell GPU, so CPU and GPU can work on the same data without separate host-to-device copies. That can reduce startup overhead, and the unified memory pool can scale to whichever side of the workload needs more memory at a given point.


## Task 1: Reach — Building Spatial Awareness

The Reach task trains the Franka arm to move its end-effector to a randomly sampled target pose. This is your first manipulation baseline because it teaches position control before adding grasping.

### Run

Use your existing Isaac Lab setup from the previous Learning Path, then run:

{{< tabpane code=true >}}
{{< tab header="IsaacLab 2.3 API" >}}
cd ~/IsaacLab

# Improve runtime compatibility on aarch64 systems
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"

./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Reach-Franka-v0 \
    --headless \
    --num_envs=2048
{{< /tab >}}
{{< tab header="IsaacLab 3.0 API" >}}
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



This training flow uses the **RSL-RL PPO** algorithm. The PPO hyperparameters and actor/critic network sizes are defined in the task config file at `source/isaaclab_tasks/isaaclab_tasks/manager_based/manipulation/<task>/config/franka/agents/rsl_rl_ppo_cfg.py`.

In these config files, the example PPO model sizes are:

* Reach actor and critic: `[64, 64]`
* Lift actor and critic: `[256, 128, 64]`

The default training iterations are:

* Reach: `1000` iterations
* Lift: `1500` iterations

Training the simple reach task on the DGX Spark will take approximately 10 minutes. 


### What this script controls

This command does more than start training. The Python entry point controls:

* which task configuration is loaded
* which RL training entry point is used
* runtime behavior such as headless execution and the number of environments

In Isaac Lab, an **environment** is one simulated instance of the task. For example, one environment includes one Franka arm, one target, and one physics rollout. When you set `--num_envs=2048`, Isaac Lab runs 2048 instances in parallel to scale to the GPU capacity available. Proximal policy optimization (PPO) then uses trajectories from all environments to update the actor and critic networks each iteration converging quicker to an optimal solution compared to a single environment.


### Task structure

* **Goal**: Move the end-effector of the Franka 7-DOF arm to a randomly sampled target pose.
* **Observation space**: Joint positions, joint velocities, and target position.
* **Action space**: Joint position targets.

### Verify

After training, run the following command to observe the learned policy in simulation, replace the `--checkpoint` with the PyTorch model file for your desired iteration. We are limiting the number of environments to 2 simply to allow the simulation to load faster but you can increase to observe multiple instances:

{{< tabpane code=true >}}
{{< tab header="IsaacLab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task=Isaac-Reach-Franka-Play-v0 \
    --num_envs=2 \
    --checkpoint=logs/rsl_rl/franka_reach/<run_timestamp>/model_<iteration>.pt
{{< /tab >}}
{{< tab header="IsaacLab 3.0 API" >}}
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
{{< tab header="IsaacLab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --headless \
    --num_envs=2048
{{< /tab >}}
{{< tab header="IsaacLab 3.0 API" >}}
./isaaclab.sh train \
    --rl_library rsl_rl \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --viz none \
    --num_envs=2048
{{< /tab >}}
{{< /tabpane >}}

{{% notice Please Note %}}

After an initial run, the end-effector might still fail to lift consistently. To continue training from a checkpoint rerun with the additional arguments shown below:

{{< tabpane code=true >}}
{{< tab header="IsaacLab 2.3 API" >}}
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
{{< tab header="IsaacLab 3.0 API" >}}
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

The training log prints a **learning-iteration summary** each cycle. Watch `Episode_Reward/lifting_object` to assess whether the policy is learning to lift the cube without the needing to explicitly run a visual simulation of the model. You can see jumps and plateaus during PPO training, so short flat periods are normal. Use the broader trend across many iterations, together with ETA, to decide whether to keep training.

```output
################################################################################
                          Learning iteration 902/2650                            

                            Total steps: 37011456 
                       Steps per second: 68548 
                        Collection time: 0.600s 
                          Learning time: 0.117s 
                        Mean value loss: 2.1550
                    Mean surrogate loss: -0.0023
                      Mean entropy loss: 7.1831
                            Mean reward: 79.76
                    Mean episode length: 246.64
                        Mean action std: 0.64
         Episode_Reward/reaching_object: 0.7022
          Episode_Reward/lifting_object: 11.2984
    Episode_Reward/object_goal_tracking: 5.6466
Episode_Reward/object_goal_tracking_fine_grained: 0.0891
             Episode_Reward/action_rate: -0.7642
               Episode_Reward/joint_vel: -1.4792
                 Curriculum/action_rate: -0.1000
                   Curriculum/joint_vel: -0.1000
     Metrics/object_pose/position_error: 0.2638
  Metrics/object_pose/orientation_error: 0.8218
           Episode_Termination/time_out: 0.9782
    Episode_Termination/object_dropping: 0.0218
--------------------------------------------------------------------------------
                         Iteration time: 0.72s
                           Time elapsed: 00:09:59
                                    ETA: 00:23:11
```


### What changes in the workflow

Compared with Reach, you do not rebuild the project or switch platforms. You keep the same training entry point and environment, and only change `--task`. That lets you move quickly between manipulation scenarios while keeping the same workflow.

### Verify

After training, confirm the following:

* The robotic arm can approach the cube and adjust its gripper position.
* The gripper closes at an appropriate time.
* The cube is lifted off the table rather than slipping away or bouncing after collision.


You can use the command below to verify the result.

{{< tabpane code=true >}}
{{< tab header="IsaacLab 2.3 API" >}}
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --num_envs=2 \
    --checkpoint=<path_to_checkpoint>
{{< /tab >}}
{{< tab header="IsaacLab 3.0 API" >}}
./isaaclab.sh play \
    --rl_library rsl_rl \
    --task=Isaac-Lift-Cube-Franka-v0 \
    --num_envs=2 \
    --checkpoint=<path_to_checkpoint>
{{< /tab >}}
{{< /tabpane >}}

![Franka 7-DOF arm progressing through Reach and Lift. The left panel shows iteration 150, where grasp stability is still developing. The right panel shows around iteration 900, where the policy keeps the end-effector inverted to reduce cube drops during lifting.#center](./reach_and_lift.gif "Franka 7-DOF arm progressing through Reach and Lift. The left panel shows iteration 150, where grasp stability is still developing. The right panel shows around iteration 900, where the policy keeps the end-effector inverted to reduce cube drops during lifting")


## Extended exploration: comparing different locomotion robots

Isaac Lab also includes locomotion environments you can switch to with the same script pattern. If you want a quick comparison, run one quadruped task and one biped task to observe convergence differences.

| Environment | Robot | Type | Terrain | Training difficulty |
|---|---|---|---|---|
| Isaac-Velocity-Flat-Unitree-Go2-v0 | Unitree Go2 | Quadruped | Flat | Easy |
| Isaac-Velocity-Rough-H1-v0 | Unitree H1 | Biped humanoid | Rough | Hard |

Quadrupeds often converge faster because they are more statically stable. Bipeds usually need longer training because balance is harder to learn.

## Next up

The Franka robotic arm now has basic grasping ability. However, objects in the real world often introduce more complex mechanical constraints.

In the next section, you will explore how a robot can interact with joint-constrained objects such as drawers, and move one step closer to high-precision industrial manipulation tasks.

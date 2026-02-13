---
title: Train a Humanoid Locomotion Policy with Isaac Lab on DGX Spark
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Train a reinforcement learning policy using Isaac Lab and RSL-RL

In this section you will train a reinforcement learning (RL) policy for the Unitree H1 humanoid robot to walk over rough terrain. You will use Isaac Lab's RSL-RL integration, which implements the Proximal Policy Optimization (PPO) algorithm. By the end of this section you will understand the full training pipeline, including task configuration, PPO hyperparameters, and policy evaluation.

## What is RSL-RL?

RSL-RL (Robotic Systems Lab Reinforcement Learning) is a lightweight RL library developed at [ETH Zurich](https://ethz.ch/en.html) specifically for locomotion tasks. It implements PPO with features tailored to robotics:

- GPU-accelerated rollout collection across thousands of parallel environments
- Efficient on-policy training with generalized advantage estimation (GAE)
- Asymmetric actor-critic support (the critic can observe more than the actor)
- Minimal dependencies and tight integration with Isaac Lab

Isaac Lab provides ready-to-use training scripts for RSL-RL under `scripts/reinforcement_learning/rsl_rl/`.

## Step 1: Understand the training task

The task you will train is **Isaac-Velocity-Rough-H1-v0**. This is a locomotion task where the [Unitree H1](https://www.unitree.com/h1/) humanoid robot must track a velocity command while navigating rough terrain.

The task details are:

| **Property** | **Value** |
|-------------|-----------|
| Environment ID | `Isaac-Velocity-Rough-H1-v0` |
| Robot | Unitree H1 (19 actuated joints, bipedal humanoid) |
| Terrain | Procedurally generated rough terrain with slopes, stairs, and obstacles |
| Workflow | Manager-Based |
| Objective | Track a commanded forward velocity, lateral velocity, and yaw rate |
| Observation space | Joint positions, joint velocities, gravity projection, velocity commands, and previous actions |
| Action space | Target joint positions for all actuated joints |
| RL library | RSL-RL (PPO) |

The robot receives a velocity command (for example, "walk forward at 1.0 m/s") and must learn to coordinate all 19 joints to achieve that velocity while maintaining balance on uneven ground.

This setup provides a high-dimensional control problem ideal for testing locomotion learning under challenging terrain.

## Step 2: Launch the training

Navigate to the Isaac Lab directory and start training in headless mode for maximum performance:

```bash
cd ~/IsaacLab
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Velocity-Rough-H1-v0 \
    --headless
```

Once the training starts, you will see log messages reporting iteration progress, rewards, and performance statistics.

This command launches the training with default hyperparameters. The Blackwell GPU runs thousands of parallel H1 environments simultaneously while the Grace CPU handles logging and orchestration.

{{% notice Warning %}}
**Known issue: NVRTC GPU architecture error on DGX Spark**

When running RL training on the Blackwell GPU (GB10, compute capability 12.1), you may encounter:

```
RuntimeError: nvrtc: error: invalid value for --gpu-architecture (-arch)
```

This error occurs because the NVRTC runtime compiler inside PyTorch does not yet fully support the `sm_121` architecture. It is a known compatibility issue tracked in [Isaac Lab Discussion #2406](https://github.com/isaac-sim/IsaacLab/discussions/2406) and [PyTorch Issue #87595](https://github.com/pytorch/pytorch/issues/87595).

**Workaround**: Make sure you are using the Isaac Sim build from source (as described in the setup section) rather than a pip-installed version. The source build includes the correct CUDA 13 runtime for Blackwell. If the error persists, try running with `--headless` mode, which avoids some NVRTC code paths used by the renderer. Also ensure your NVIDIA driver is up to date (`nvidia-smi` should show driver 580.x or later).

This issue is expected to be resolved in future Isaac Sim and PyTorch releases with full Blackwell support.
{{% /notice %}}

You can also override default parameters from the command line:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task=Isaac-Velocity-Rough-H1-v0 \
    --headless \
    --num_envs=2048 \
    --max_iterations=1500 \
    --seed=42
```

### Command-line arguments

The following table explains the key command-line arguments:

| **Argument** | **Default** | **Description** |
|-------------|-------------|-----------------|
| `--task` | (required) | The Isaac Lab environment ID. Use `Isaac-Velocity-Rough-H1-v0` for rough-terrain humanoid locomotion |
| `--headless` | off | Disables visualization for faster training. All GPU resources go to simulation and training |
| `--num_envs` | 4096 | Number of parallel environments. Each environment runs an independent simulation of the H1 robot |
| `--max_iterations` | 1500 | Total number of PPO training iterations. Each iteration collects a batch of experience and updates the policy |
| `--seed` | 0 | Random seed for reproducibility. Set this to get deterministic results across runs |

{{% notice Tip %}}
On DGX Spark, 2048 to 4096 parallel environments work well for locomotion tasks. Higher values increase sample throughput but require more GPU memory. Start with 2048 if you want faster iteration cycles during development.
{{% /notice %}}

## Step 3: Understand the PPO hyperparameters

This section explains the core PPO training parameters used by RSL-RL and how they influence learning quality and stability.

PPO (Proximal Policy Optimization) is the RL algorithm used by RSL-RL. Understanding each hyperparameter helps you tune training for different tasks. The following table describes the key hyperparameters and their roles:

### Policy network hyperparameters

| **Hyperparameter** | **Typical value** | **Description** |
|--------------------|-------------------|-----------------|
| `policy_class_name` | `ActorCritic` | The neural network architecture. `ActorCritic` uses separate networks for the policy (actor) and value function (critic) |
| `actor_hidden_dims` | `[512, 256, 128]` | Hidden layer sizes for the actor (policy) network. Larger networks can represent more complex behaviors but train more slowly |
| `critic_hidden_dims` | `[512, 256, 128]` | Hidden layer sizes for the critic (value) network. The critic estimates how good each state is |
| `activation` | `elu` | Activation function between hidden layers. ELU (Exponential Linear Unit) provides smooth gradients and avoids dead neurons |
| `init_noise_std` | `1.0` | Initial standard deviation of the exploration noise. Higher values encourage more exploration early in training |

### PPO algorithm hyperparameters

| **Hyperparameter** | **Typical value** | **Description** |
|--------------------|-------------------|-----------------|
| `num_learning_epochs` | `5` | Number of times the policy is updated using each batch of collected experience. Higher values extract more learning from each batch but risk overfitting |
| `num_mini_batches` | `4` | Number of mini-batches the experience buffer is split into for each epoch. More mini-batches mean smaller gradient updates |
| `learning_rate` | `1e-3` | Step size for the Adam optimizer. Controls how much the network weights change per update. Too high causes instability; too low slows convergence |
| `discount_factor` (gamma) | `0.99` | How much the agent values future rewards vs. immediate rewards. A value of 0.99 means the agent considers rewards ~100 steps into the future |
| `gae_lambda` (lambda) | `0.95` | Generalized Advantage Estimation smoothing parameter. Balances bias (low lambda) vs. variance (high lambda) in advantage estimates |
| `clip_param` | `0.2` | PPO clipping range. Prevents the policy from changing too much in a single update. Keeps training stable |
| `value_loss_coef` | `1.0` | Weight of the value function loss relative to the policy loss. Ensures the critic learns at an appropriate rate |
| `entropy_coef` | `0.01` | Weight of the entropy bonus. Encourages exploration by penalizing overly deterministic policies. Reduce this as training converges |
| `desired_kl` | `0.01` | Target KL divergence between old and new policies. If KL exceeds this value, the learning rate is reduced adaptively |
| `max_grad_norm` | `1.0` | Maximum gradient norm for gradient clipping. Prevents exploding gradients during training |

### Rollout hyperparameters

| **Hyperparameter** | **Typical value** | **Description** |
|--------------------|-------------------|-----------------|
| `num_steps_per_env` | `24` | Number of simulation steps collected per environment per iteration. Together with `num_envs`, this determines the total batch size: `batch_size = num_envs × num_steps_per_env` |
| `save_interval` | `50` | Save a model checkpoint every N iterations. Useful for resuming training or evaluating intermediate policies |

### How the hyperparameters interact

The total amount of experience collected per training iteration is:

```
batch_size = num_envs × num_steps_per_env
```

For example, with `num_envs=4096` and `num_steps_per_env=24`:

```
batch_size = 4096 × 24 = 98,304 environment steps per iteration
```

This batch is then split into `num_mini_batches` (4) mini-batches of ~24,576 steps each. The policy is updated `num_learning_epochs` (5) times per iteration, meaning each batch of experience is used for 5 × 4 = 20 gradient updates.

## Step 4: Monitor the training

During training, RSL-RL prints statistics to the terminal at regular intervals. A typical output looks like:

```output
Learning iteration 100/1500
    mean reward:              12.45
    mean episode length:      234.5
    value function loss:       0.032
    surrogate loss:           -0.0156
    mean std:                  0.42
    learning rate:             0.001
    fps:                       48523
```

Interpreting these values helps track convergence and diagnose training instability, such as stagnating rewards or exploding losses.

The following table explains each metric:

| **Metric** | **What it means** | **What to look for** |
|-----------|-------------------|----------------------|
| `mean reward` | Average cumulative reward across all environments per episode | Should increase over time. Higher values mean the robot is walking better |
| `mean episode length` | Average number of steps before the episode ends | Should increase as the robot learns to stay upright longer |
| `value function loss` | How well the critic predicts future rewards | Should decrease and stabilize |
| `surrogate loss` | The PPO policy loss (negative because PPO maximizes the objective) | Should be small and negative |
| `mean std` | Average exploration noise standard deviation | Should decrease as the policy becomes more confident |
| `learning rate` | Current learning rate (may be adjusted by the adaptive KL mechanism) | Stays at the initial value unless KL divergence exceeds `desired_kl` |
| `fps` | Frames (environment steps) per second | Indicates training throughput. On DGX Spark, expect 40,000-60,000+ fps for locomotion tasks |

{{% notice Note %}}
Training checkpoints are saved to the `logs/rsl_rl/` directory. Each run creates a timestamped folder containing the model weights, configuration, and training logs.
{{% /notice %}}

## Step 5: Evaluate the trained policy

After training completes, evaluate the policy by running inference with visualization. Use the `play.py` script with the trained checkpoint:

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task=Isaac-Velocity-Rough-H1-Play-v0 \
    --num_envs=32
```

{{% notice Note %}}
For evaluation, use the inference task name `Isaac-Velocity-Rough-H1-Play-v0` instead of the training task name. The play variant disables runtime perturbations used during training and loads the checkpoint automatically.
{{% /notice %}}

The play script loads the most recent checkpoint and runs the policy in real time. You will observe the Unitree H1 humanoid walking over procedurally generated rough terrain, responding to live velocity commands.

You can also specify a particular checkpoint manually, which is useful for comparing intermediate policy performance.

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task=Isaac-Velocity-Rough-H1-Play-v0 \
    --num_envs=32 \
    --checkpoint=logs/rsl_rl/Isaac-Velocity-Rough-H1-v0/<timestamp>/model_1500.pt
```

### Understanding the evaluation

During evaluation, observe these behaviors:

- **Early training checkpoints (iterations 0-200)**: The robot falls immediately or takes a few uncoordinated steps
- **Mid-training checkpoints (iterations 200-800)**: The robot can walk forward but may stumble on rough terrain
- **Late training checkpoints (iterations 800-1500)**: The robot walks confidently over rough terrain, handles slopes and obstacles, and tracks velocity commands accurately

The progression from falling to walking demonstrates how PPO gradually optimizes the policy through trial and error across thousands of parallel environments.


## What you have accomplished

In this module, you have:

- Trained a reinforcement learning policy for the Unitree H1 humanoid robot using RSL-RL and the PPO algorithm
- Understood every key hyperparameter in the training pipeline, including policy architecture, PPO parameters, and rollout strategy
- Monitored training progress using reward trends, episode statistics, and performance metrics
- Evaluated the trained policy through interactive visualization in Isaac Lab

You have now completed the end-to-end workflow of training, evaluating, and understanding a reinforcement learning policy for humanoid locomotion using Isaac Lab on DGX Spark. This includes configuring simulation environments, tuning algorithm parameters, and deploying trained policies.

This marks the completion of your core learning journey for single-task humanoid reinforcement learning with Isaac Lab.

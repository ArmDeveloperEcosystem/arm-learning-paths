---
title: Run a sample robot simulation in Isaac Sim
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy a basic robot simulation

Now that Isaac Sim and Isaac Lab are installed, you can run your first robot simulation. In this section you will launch a pre-built simulation scene, interact with it programmatically, and understand the key concepts behind Isaac Sim's simulation loop.

You will work with the Cartpole environment, a classic control benchmark where a cart must balance a pole by applying horizontal forces. This environment is simple enough to understand quickly but demonstrates all the core simulation concepts you need for more complex robotics tasks.

## Step 1: Launch a sample scene from Isaac Lab

Isaac Lab provides tutorial scripts that demonstrate how to create and interact with simulation scenes. Start by running the interactive scene tutorial:

```bash
cd ~/IsaacLab
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"
./isaaclab.sh -p scripts/tutorials/00_sim/create_empty.py
```

This script creates an empty simulation world with a ground plane and default lighting. It validates that the Isaac Sim rendering and physics engines are working on your DGX Spark system.

You should see a viewer window open (if a display is connected) or see log messages confirming the simulation initialized successfully in headless mode.

Press `Ctrl+C` to exit the simulation.

## Step 2: Spawn and simulate a robot

Next, run a more complete example that spawns articulated robots into the scene. This tutorial demonstrates how Isaac Sim handles multi-body physics:

```bash
./isaaclab.sh -p scripts/tutorials/01_assets/run_articulation.py
```

This script loads a robot model, steps the physics simulation, and prints joint states to the terminal. It demonstrates:

- Loading a robot from a USD (Universal Scene Description) asset file
- Configuring joint actuators and control modes
- Stepping the physics simulation and reading back joint positions and velocities

![img1 alt-text#center](sample_run.gif "Figure 1: run_articulation.py")

## Step 3: Run the Cartpole environment

Now run a complete RL environment. The Cartpole Direct environment is a self-contained example that you can use to verify the full Isaac Lab pipeline:

```bash
./isaaclab.sh -p scripts/tutorials/03_envs/create_direct_rl_env.py --task=Isaac-Cartpole-Direct-v0 --num_envs=32
```

This command launches 32 parallel Cartpole environments on the Blackwell GPU. Each environment runs its own independent simulation with random actions applied to the cart.

The key command-line arguments are:

| **Argument** | **Description** |
|-------------|-----------------|
| `--task=Isaac-Cartpole-Direct-v0` | Specifies the environment to load. This uses the Direct workflow where all environment logic is in a single class |
| `--num_envs=32` | Number of parallel environment instances. Each runs independently on the GPU |

You will see output showing the observation space, action space, and episode statistics as the random agent interacts with the environments.

## Step 4: Understand the simulation code

To understand what happens inside an Isaac Lab environment, examine the Cartpole Direct environment source code. The key elements are:

### Environment configuration

Every Isaac Lab environment starts with a configuration class that defines the simulation parameters. For the Cartpole Direct environment, the configuration specifies:

```python
@configclass
class CartpoleEnvCfg(DirectRLEnvCfg):
    # Simulation parameters
    decimation = 2              # Number of physics steps per RL step
    episode_length_s = 5.0      # Maximum episode duration in seconds
    action_scale = 100.0        # Multiplier applied to raw policy actions
    num_observations = 4        # Observation vector size: [cart_pos, cart_vel, pole_angle, pole_angular_vel]
    num_actions = 1             # Single continuous action: force on the cart

    # Simulation settings
    sim: SimulationCfg = SimulationCfg(dt=1 / 120)  # Physics timestep: 120 Hz
```

The table below explains each parameter:

| **Parameter** | **Value** | **Description** |
|---------------|-----------|-----------------|
| `decimation` | 2 | The policy acts every 2 physics steps. With a 120 Hz physics rate, the policy runs at 60 Hz |
| `episode_length_s` | 5.0 | Each episode lasts a maximum of 5 seconds before resetting |
| `action_scale` | 100.0 | Raw policy outputs (typically in the range [-1, 1]) are multiplied by this value to produce physical forces in Newtons |
| `num_observations` | 4 | The agent observes cart position, cart velocity, pole angle, and pole angular velocity |
| `num_actions` | 1 | A single continuous value representing the horizontal force applied to the cart |
| `sim.dt` | 1/120 | The physics engine advances by 1/120th of a second per step |

### The simulation loop

The core simulation loop in Isaac Lab follows a standard Gymnasium-style interface:

```python
# Reset the environment
obs, info = env.reset()

while simulation_running:
    # Agent selects an action (random in this example)
    action = env.action_space.sample()

    # Step the environment: apply action, advance physics, compute reward
    obs, reward, terminated, truncated, info = env.step(action)

    # If the episode ended, the environment auto-resets
```

Each call to `env.step(action)` performs these operations on the GPU:

1. **Apply actions**: The action tensor is scaled and applied as joint forces or position targets
2. **Step physics**: The simulation advances by `decimation` physics steps (2 steps at 120 Hz = 1/60 second of simulated time)
3. **Compute observations**: Joint positions, velocities, and other sensor data are read from the simulation
4. **Compute rewards**: A reward function evaluates how well the agent performed
5. **Check terminations**: The environment checks if the episode should end (for example, pole fell too far)

### Reward function

The Cartpole reward function encourages the agent to keep the pole upright and the cart centered:

```python
def _get_rewards(self) -> torch.Tensor:
    total_reward = compute_rewards(
        self.cfg.rew_scale_alive,       # Bonus for each step the pole stays upright
        self.cfg.rew_scale_terminated,   # Penalty when the episode terminates early
        self.cfg.rew_scale_pole_pos,     # Reward for keeping the pole angle near zero
        self.cfg.rew_scale_cart_vel,     # Penalty for excessive cart velocity
        self.cfg.rew_scale_pole_vel,     # Penalty for excessive pole angular velocity
        self.joint_pos[:, self._pole_dof_idx[0]],   # Current pole angle
        self.joint_vel[:, self._pole_dof_idx[0]],   # Current pole angular velocity
        self.joint_pos[:, self._cart_dof_idx[0]],    # Current cart position
        self.joint_vel[:, self._cart_dof_idx[0]],    # Current cart velocity
        self.reset_terminated,
    )
    return total_reward
```

All computations happen in parallel across all environments using PyTorch tensors on the GPU. This is what makes Isaac Lab fast: thousands of environments run simultaneously with no Python loop overhead.

## Step 5: Run with headless mode

For training workloads you will typically run without visualization to maximize GPU utilization. Test headless mode:

```bash
./isaaclab.sh -p scripts/tutorials/03_envs/create_direct_rl_env.py \
    --task=Isaac-Cartpole-Direct-v0 \
    --num_envs=64 \
    --headless
```

In headless mode, all GPU resources are dedicated to physics simulation and tensor computation. This is the recommended mode for training reinforcement learning policies, which you will do in the next section.

{{% notice Note %}}
When running headless on DGX Spark, the Blackwell GPU handles both the physics simulation and neural network computation. The unified memory architecture means there is no performance penalty for sharing GPU memory between these workloads.
{{% /notice %}}

## What you have accomplished

In this section you have:

- Launched your first Isaac Sim scene on DGX Spark and verified the rendering and physics engines work correctly
- Spawned articulated robots and observed multi-body physics simulation
- Run 32 parallel Cartpole environments on the Blackwell GPU with random actions
- Understood the key components of an Isaac Lab environment: configuration, simulation loop, observation space, action space, and reward function
- Tested headless mode for maximum training performance

You now understand the fundamental building blocks of Isaac Lab environments. In the next section, you will use these concepts to train a reinforcement learning policy for a humanoid robot.

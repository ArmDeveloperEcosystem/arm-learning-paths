---
title: Set up Isaac Sim and Isaac Lab on DGX Spark
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

Before running robotic simulations and reinforcement learning tasks, you need to build Isaac Sim and Isaac Lab from source on your DGX Spark system. This section walks you through verifying your system, installing dependencies, building Isaac Sim, and then setting up Isaac Lab on top of it.

The build process takes approximately 15-20 minutes on the Grace CPU and requires around 50 GB of available disk space.

## Step 1: Verify your system

Start by confirming that your DGX Spark system has the required hardware and software configuration.

Check the CPU architecture:

```bash
lscpu | head -5
```

The output is similar to:

```output
Architecture:             aarch64
  CPU op-mode(s):         64-bit
  Byte Order:             Little Endian
CPU(s):                   20
  On-line CPU(s) list:    0-19
```

Verify the Blackwell GPU is recognized:

```bash
nvidia-smi
```

You will see output similar to:

```output
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
|=========================================+========================+======================|
|   0  NVIDIA GB10                    On  |   0000000F:01:00.0 Off |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

Confirm the CUDA toolkit is installed:

```bash
nvcc --version
```

The expected output includes:

```output
Cuda compilation tools, release 13.0, V13.0.88
```

{{% notice Note %}}
Isaac Sim requires GCC/G++ 11, Git LFS, and CUDA 13.0 or later. If any of these checks fail, resolve the issue before proceeding.
{{% /notice %}}

## Step 2: Install GCC 11 and Git LFS

Isaac Sim requires GCC/G++ version 11 for compilation. Install it and set it as the default compiler:

```bash
sudo apt update && sudo apt install -y gcc-11 g++-11
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 200
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 200
```

Install Git LFS, which is needed to pull large binary assets from the Isaac Sim repository:

```bash
sudo apt install -y git-lfs
```

Verify both installations:

```bash
gcc --version
g++ --version
git lfs version
```

The GCC output should show version 11.x. Git LFS should report a version number confirming it is installed.

## Step 3: Clone and build Isaac Sim

Clone the Isaac Sim repository from GitHub. The `--depth=1` flag creates a shallow clone to reduce download time, and `--recursive` fetches all submodules:

```bash
cd ~
git clone --depth=1 --recursive https://github.com/isaac-sim/IsaacSim
cd IsaacSim
git lfs install
git lfs pull
```

{{% notice Note %}}
The Git LFS pull downloads several gigabytes of simulation assets (USD files, textures, and pre-built libraries). Ensure you have a stable network connection.
{{% /notice %}}

Build Isaac Sim by running the build script. This compiles the simulation engine and all its components:

```bash
./build.sh
```

The build uses all available CPU cores on the Grace processor. On DGX Spark, compilation typically takes 10-15 minutes.

When the build succeeds, you will see output similar to:

```output
BUILD (RELEASE) SUCCEEDED (Took 674.39 seconds)
```

## Step 4: Set Isaac Sim environment variables

After the build completes, configure your shell to recognize the Isaac Sim installation. Run the following commands from inside the `IsaacSim` directory:

```bash
export ISAACSIM_PATH="${PWD}/_build/linux-aarch64/release"
export ISAACSIM_PYTHON_EXE="${ISAACSIM_PATH}/python.sh"
```

The table below explains each variable:

| **Variable** | **Purpose** |
|--------------|-------------|
| `ISAACSIM_PATH` | Points to the compiled Isaac Sim binaries and libraries under the `_build` directory |
| `ISAACSIM_PYTHON_EXE` | References the Python wrapper script that runs Python with Isaac Sim's dependencies preloaded |

{{% notice Tip %}}
Add these `export` lines to your `~/.bashrc` file so they persist across terminal sessions:

```bash
echo 'export ISAACSIM_PATH="$HOME/IsaacSim/_build/linux-aarch64/release"' >> ~/.bashrc
echo 'export ISAACSIM_PYTHON_EXE="${ISAACSIM_PATH}/python.sh"' >> ~/.bashrc
source ~/.bashrc
```
{{% /notice %}}

## Step 5: Validate the Isaac Sim build

Launch Isaac Sim to verify the build was successful. The `LD_PRELOAD` setting resolves a library compatibility issue on aarch64:

```bash
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"
${ISAACSIM_PATH}/isaac-sim.sh
```

If the build is correct, Isaac Sim opens its viewer window (or starts in headless mode if no display is available). You should see initialization messages confirming that the Blackwell GPU is detected and the physics engine is ready.

Press `Ctrl+C` in the terminal to close Isaac Sim after verifying it starts successfully.

## Step 6: Clone and install Isaac Lab

Now that Isaac Sim is built and working, set up Isaac Lab. Clone the repository into your home directory:

```bash
cd ~
git clone --recursive https://github.com/isaac-sim/IsaacLab
cd IsaacLab
```

Create a symbolic link so Isaac Lab can find your Isaac Sim installation:

```bash
echo "ISAACSIM_PATH=$ISAACSIM_PATH"
ln -sfn "${ISAACSIM_PATH}" "${PWD}/_isaac_sim"
```

Verify the symbolic link is correct:

```bash
ls -l "${PWD}/_isaac_sim/python.sh"
```

You should see the symlink pointing to your Isaac Sim build directory.

Install Isaac Lab and all its dependencies:

```bash
./isaaclab.sh --install
```

This command installs the Isaac Lab Python packages, RL libraries (RSL-RL, rl_games, skrl, Stable Baselines3), and additional dependencies into the Isaac Sim Python environment.

## Step 7: Validate the Isaac Lab installation

Verify that Isaac Lab is installed correctly by listing the available RL environments:

```bash
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"
./isaaclab.sh -p scripts/environments/list_envs.py
```

You should see a list of available environments, including entries such as:

```output
Isaac-Cartpole-v0
Isaac-Cartpole-Direct-v0
Isaac-Velocity-Flat-H1-v0
Isaac-Velocity-Rough-H1-v0
Isaac-Lift-Cube-Franka-v0
Isaac-Reach-Franka-v0
...
```

If the environment list displays without errors, both Isaac Sim and Isaac Lab are correctly installed and ready for use.

## What you have accomplished

In this section you have:

- Verified your DGX Spark system has the required Grace CPU, Blackwell GPU, and CUDA 13 environment
- Installed GCC 11 and Git LFS as build prerequisites
- Cloned and built Isaac Sim from source, producing aarch64-optimized binaries for the Grace-Blackwell platform
- Configured environment variables so Isaac Lab can locate the Isaac Sim installation
- Cloned and installed Isaac Lab with all RL library dependencies
- Validated both installations by launching Isaac Sim and listing available environments

Your development environment is now ready. In the next section, you will run your first robot simulation in Isaac Sim.

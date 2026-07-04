---
title: Set up Isaac Sim and Isaac Lab on DGX Spark
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

Before you run robotic simulations and reinforcement learning workloads, you need to prepare your DGX Spark development environment and install the dependencies required for Isaac Sim and Isaac Lab.

In this section you'll:
  * Verify the DGX Spark system configuration
  * Install required build dependencies
  * Build and configure Isaac Sim
  * Set up Isaac Lab on top of the Isaac Sim environment

The full setup typically takes 15–20 minutes on a DGX Spark system and requires approximately 50 GB of available disk space.

## Step 1: Verify your DGX Spark system

Begin by confirming that the DGX Spark system has the expected hardware and software configuration.

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
The Architecture field should report `aarch64`, indicating that the system is running on Arm.

Check that the Blackwell GPU is detected by the NVIDIA driver:

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
The GPU name should appear as NVIDIA GB10, confirming that the Grace–Blackwell GPU is available.

Confirm the CUDA toolkit is installed:

```bash
nvcc --version
```

The expected output includes:

```output
Cuda compilation tools, release 13.0, V13.0.88
```

{{% notice Note %}}Isaac Sim requires GCC/G++ 11, Git LFS, and CUDA 13.0 or later. If any of these checks fail, resolve the issue before you proceed.{{% /notice %}}

## Step 2: Install GCC 11 and Git LFS

Isaac Sim requires GCC/G++ version 11 when building components from source. Install the required compiler version and configure it as the system default.
Update the package index and install the GCC 11 toolchain:

```bash
sudo apt update && sudo apt install -y gcc-11 g++-11
```

Register GCC 11 as the default compiler using `update-alternatives`. This allows multiple compiler versions to coexist while prioritizing GCC 11 for builds. The priority value of 200 ensures GCC 11 takes precedence over other installed versions:
```bash
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 200
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 200
```

Next, install Git LFS (Large File Storage). Isaac Sim repositories use Git LFS to manage large binary assets such as models and simulation data.

```bash
sudo apt install -y git-lfs
```

After installation, verify that the compiler and Git LFS are available:

```bash
gcc --version
g++ --version
git lfs version
```

The gcc and g++ commands should report version 11.x, and git lfs version should display the installed Git LFS version.

## Step 3: Clone and build Isaac Sim

Next, download the Isaac Sim source repository and its required assets.

Start by cloning the repository. The --depth=1 option performs a shallow clone to reduce download size, and --recursive ensures all required submodules are fetched.
```bash
cd ~
git clone --depth=1 --recursive https://github.com/isaac-sim/IsaacSim
cd IsaacSim
```
Isaac Sim stores large simulation assets (such as USD environments, textures, and prebuilt components) using Git Large File Storage (LFS). Initialize Git LFS and download the required assets:
```bash
git lfs install
git lfs pull
```

{{% notice Note %}}The Git LFS download retrieves several gigabytes of simulation assets. Ensure you have a stable internet connection and sufficient disk space before you run this step.{{% /notice %}}

Once the repository and assets are downloaded, build Isaac Sim using the provided build script:

```bash
./build.sh
```
By default, the build uses all available CPU cores on the Grace processor. On DGX Spark, compilation typically takes 10-15 minutes.

When the build finishes successfully, you will see output similar to:

```output
BUILD (RELEASE) SUCCEEDED (Took 674.39 seconds)
```

## Step 4: Set Isaac Sim environment variables

After the build completes, configure environment variables so that your shell can locate the Isaac Sim binaries and Python runtime.

Navigate to the IsaacSim directory if you are not already there, then export the following variables:
```bash
export ISAACSIM_PATH="${PWD}/_build/linux-aarch64/release"
export ISAACSIM_PYTHON_EXE="${ISAACSIM_PATH}/python.sh"
```

These variables are used by Isaac Lab and other tools to locate the Isaac Sim runtime.

| **Variable** | **Purpose** |
|--------------|-------------|
| `ISAACSIM_PATH` | Points to the compiled Isaac Sim binaries and libraries under the `_build` directory |
| `ISAACSIM_PYTHON_EXE` | References the Python wrapper script that runs Python with Isaac Sim's dependencies preloaded |

{{% notice Tip %}}
To make these environment variables persist across terminal sessions, add them to your shell configuration file.
Run the following commands:
```bash
echo 'export ISAACSIM_PATH="$HOME/IsaacSim/_build/linux-aarch64/release"' >> ~/.bashrc
echo 'export ISAACSIM_PYTHON_EXE="${ISAACSIM_PATH}/python.sh"' >> ~/.bashrc
source ~/.bashrc
```
After this step, the variables will be available automatically whenever you open a new terminal.

{{% /notice %}}

## Step 5: Validate your Isaac Sim build

Launch Isaac Sim to verify the build was successful. On some aarch64 systems, Isaac Sim may require preloading the GNU OpenMP runtime (libgomp) to avoid library compatibility issues. Setting the LD_PRELOAD environment variable ensures the correct library is loaded before Isaac Sim starts.

Run the following command to launch Isaac Sim:
```bash
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"
${ISAACSIM_PATH}/isaac-sim.sh
```

If the installation is correct, Isaac Sim opens its viewer window (or starts in headless mode if no display is available). During startup, the console output should report initialization of the Blackwell GPU and the physics simulation engine.

Once you confirm that Isaac Sim starts successfully, stop the application by pressing:
`Ctrl + C`

This returns you to the terminal and confirms that the build and runtime environment are functioning correctly.

## Step 6: Clone and install Isaac Lab

After confirming that Isaac Sim runs correctly, you can install Isaac Lab, which provides the reinforcement learning environments and training pipelines used in this learning path.
Start by cloning the Isaac Lab repository into your home directory:

```bash
cd ~
git clone --recursive https://github.com/isaac-sim/IsaacLab
cd IsaacLab
```
Isaac Lab expects to locate an Isaac Sim installation in a directory named `_isaac_sim` inside the repository. Instead of copying files, create a symbolic link pointing to the Isaac Sim build directory that you configured earlier.

First confirm that the ISAACSIM_PATH variable is set:

```bash
echo "ISAACSIM_PATH=$ISAACSIM_PATH"
```
Then create the symbolic link
```bash
ln -sfn "${ISAACSIM_PATH}" "${PWD}/_isaac_sim"
```
This links the Isaac Lab repository to the Isaac Sim installation that was built in the previous steps.

Verify the symbolic link is correct:

```bash
ls -l "${PWD}/_isaac_sim/python.sh"
```

You should see the symlink pointing to your Isaac Sim build directory.

Next, install Isaac Lab and its Python dependencies:

```bash
./isaaclab.sh --install
```

This command installs the Isaac Lab Python packages, RL libraries (RSL-RL, rl_games, skrl, Stable Baselines3), and additional dependencies into the Isaac Sim Python environment.

## Step 7: Validate the Isaac Lab installation

Confirm that Isaac Lab is installed correctly by listing the available RL environments:

```bash
export LD_PRELOAD="$LD_PRELOAD:/lib/aarch64-linux-gnu/libgomp.so.1"
./isaaclab.sh -p scripts/environments/list_envs.py
```
If the installation is successful, the command prints a list of available environments. The output will include entries similar to:

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

You're now ready to run and train RL tasks using Isaac Lab environments.

## What you've learned and what's next

In this section you've:

- Verified your DGX Spark system has the required Grace CPU, Blackwell GPU, and CUDA 13 environment
- Installed GCC 11 and Git LFS as build prerequisites
- Cloned and built Isaac Sim, producing binaries for the aarch64 Grace–Blackwell platform
- Configured environment variables so Isaac Lab can locate the Isaac Sim installation
- Cloned and installed Isaac Lab with all RL library dependencies
- Validated both installations by launching Isaac Sim and listing available environments

Your development environment is now fully configured for robot simulation and RL workflows. In the next section, you'll run your first robot simulation and begin interacting with Isaac Sim through Python scripts.

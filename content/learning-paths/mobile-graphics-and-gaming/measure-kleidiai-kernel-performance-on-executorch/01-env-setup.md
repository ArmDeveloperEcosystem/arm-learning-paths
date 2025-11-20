---
title: Environment setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Python Environment Setup 

Before building ExecuTorch, it is highly recommended to create an isolated Python environment.
This prevents dependency conflicts with your system Python installation and ensures that all required build and runtime dependencies remain consistent across runs.

```bash 
sudo apt update
sudo apt install -y python3 python3.12-dev python3-venv build-essential cmake
python3 -m venv pyenv
source pyenv/bin/activate

```
Once activated, all subsequent steps should be executed within this Python virtual environment.

### Download the ExecuTorch Source Code

Clone the ExecuTorch repository from GitHub. The following command checks out the stable v1.0.0 release and ensures all required submodules are fetched.

```bash
export WORKSPACE=$HOME
cd $WORKSPACE
git clone -b v1.0.0 --recurse-submodules https://github.com/pytorch/executorch.git

```

  {{% notice Note %}}
  The instructions in this guide are based on ExecuTorch v1.0.0. Commands or configuration options may differ in later releases.
  {{% /notice %}}

### Build and Install the ExecuTorch Python Components

Next, you’ll build the ExecuTorch Python bindings and install them into your active virtual environment.
This process compiles the C++ runtime, links hardware-optimized backends such as KleidiAI and XNNPACK, and enables optional developer utilities for debugging and profiling.

Run the following command from your ExecuTorch workspace:
```bash 
cd $WORKSPACE/executorch
CMAKE_ARGS="-DEXECUTORCH_BUILD_DEVTOOLS=ON" ./install_executorch.sh

```
This will build ExecuTorch and its dependencies using cmake, enabling optional developer utilities such as ETDump and Inspector.

### Verify the Installation
After the build completes successfully, verify that ExecuTorch was installed into your current Python environment:

```bash 
python -c "import executorch; print('Executorch build and install successfully.')"
```

If the output confirms success, you’re ready to begin cross-compilation and profiling preparation for KleidiAI micro-kernels.

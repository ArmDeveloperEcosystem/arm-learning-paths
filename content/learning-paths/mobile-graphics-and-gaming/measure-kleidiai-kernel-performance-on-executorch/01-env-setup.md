---
title: Environment setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Python Environment Setup 

Before building ExecuTorch, it is highly recommended to create an isolated Python environment.
This prevents dependency conflicts with your system Python installation and ensures a clean build environment.

```bash 
cd $HOME
sudo apt update
sudo apt install -y python3 python3-venv
python3 -m venv pyenv
source pyenv/bin/activate

```
All subsequent steps should be executed within this Python virtual environment.

### Download the ExecuTorch Source Code

Clone the ExecuTorch repository from GitHub. The following command checks out the stable v1.0.0 release and ensures all required submodules are fetched.

```bash 
cd $WORKSPACE
git clone -b v1.0.0 --recurse-submodules https://github.com/pytorch/executorch.git

```

   > **Note:**  
   > The instructions in this guide are based on **ExecuTorch v1.0.0**.  
   > Commands or configuration options may differ in later releases.

### Build and Install the ExecuTorch Python Components

Next, build the Python bindings and install them into your environment. The following command uses the provided installation script to configure, compile, and install ExecuTorch with developer tools enabled.

```bash 
cd $WORKSPACE/executorch
CMAKE_ARGS="-DEXECUTORCH_BUILD_DEVTOOLS=ON" ./install_executorch.sh

```

This will build ExecuTorch and its dependencies using CMake, enabling optional developer utilities such as ETDump and Inspector.

After installation completes successfully, you can verify the environment by running:

```bash 
python -c "import executorch; print('Executorch build and install successfully.')"
```


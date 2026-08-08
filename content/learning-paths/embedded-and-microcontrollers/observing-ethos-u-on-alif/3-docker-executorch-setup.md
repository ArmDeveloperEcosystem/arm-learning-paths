---
title: (Optional) Set up a Docker development environment
description: Set up a Docker environment with ExecuTorch, PyTorch, and Arm Ethos-U dependencies for exporting an MNIST model to `.pte` format.
weight: 4
layout: learningpathall
---

## Install Docker Desktop

To train and export an MNIST model to ExecuTorch `.pte` format, you'll need to create a Docker environment.

{{% notice Note %}}
If you're using the provided `.pte` file, skip the entire Docker setup section and proceed with [Prepare firmware artifacts](/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/). Complete the Docker setup only if you want to train and export the model yourself.
{{% /notice %}}

Docker provides an isolated environment with all the build dependencies needed. 

Start by downloading and installing Docker Desktop. For more information, see the [Docker Desktop install guide](/install-guides/docker/docker-desktop/).

## Verify Docker installation

After installation, start Docker Desktop and verify that Docker is available from your terminal:

```bash
docker --version
```
The output is similar to:

```output
Docker version 24.0.7, build afdd53b
```

Test Docker is working:

```bash
docker run hello-world
```

The output is similar to:
```output
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

## Create the Docker workspace

Create a folder for the Docker files, model scripts, and generated output:

{{< tabpane code=true >}}
  {{< tab header="macOS and Linux" language="bash" >}}
cd ~/mnist_alif
mkdir -p executorch-alif/models executorch-alif/output
cd executorch-alif
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
cd ~\mnist_alif
New-Item -ItemType Directory -Force -Path .\executorch-alif\models, .\executorch-alif\output
cd .\executorch-alif
  {{< /tab >}}
{{< /tabpane >}}

The directory will be used as follows:

```text
executorch-alif/
├── Dockerfile
├── start-dev.sh              # macOS/Linux
├── start-dev.ps1             # Windows
├── models/                   # mounted to /home/developer/models
└── output/                   # mounted to /home/developer/output
```

## Create the Dockerfile

Create a file named `Dockerfile`:

{{< tabpane code=true >}}
  {{< tab header="macOS and Linux" language="bash" >}}
touch Dockerfile
code Dockerfile
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
New-Item -ItemType File -Path .\Dockerfile
notepad .\Dockerfile
  {{< /tab >}}
{{< /tabpane >}}

Paste the following in the `Dockerfile`:

```dockerfile
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y build-essential ca-certificates cmake curl git ninja-build python3 python3-pip python3-venv unzip vim wget xxd xz-utils && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash developer
USER developer
WORKDIR /home/developer
RUN python3 -m venv /home/developer/executorch-venv
RUN /bin/bash -c "source /home/developer/executorch-venv/bin/activate && pip install --upgrade pip setuptools wheel && pip install torch==2.9.0 torchvision==0.24.0 torchaudio==2.9.0 --index-url https://download.pytorch.org/whl/cpu && pip install ethos-u-vela==4.4.1"
ENV VIRTUAL_ENV=/home/developer/executorch-venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
CMD ["/bin/bash"]
```

## Build the Docker image

Build the image from the `executorch-alif` directory:

```bash
docker build -t executorch-alif:latest .
```

{{% notice Note %}}
The build can take 5 to 10 minutes.
{{% /notice %}}

The output is similar to:
```output
[+] Building 320.5s (12/12) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 1.2kB
 => [internal] load .dockerignore
 ...
 => => naming to docker.io/library/executorch-alif:latest
```

Verify the image:

```bash
docker images
```

The output is similar to:
```output
executorch-alif    latest
```

## Create the container startup script

After building the image, create the container startup script:

{{< tabpane code=true >}}
  {{< tab header="macOS and Linux" language="bash" >}}
cat > start-dev.sh << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
docker run -it --rm --name executorch-alif-dev -v "${SCRIPT_DIR}/models:/home/developer/models" -v "${SCRIPT_DIR}/output:/home/developer/output" -w /home/developer executorch-alif:latest /bin/bash
EOF
chmod +x start-dev.sh
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
@'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
docker run -it --rm --name executorch-alif-dev -v "${ScriptDir}/models:/home/developer/models" -v "${ScriptDir}/output:/home/developer/output" -w /home/developer executorch-alif:latest /bin/bash
'@ | Set-Content -Encoding ascii .\start-dev.ps1
  {{< /tab >}}
{{< /tabpane >}}

## Start the development container

Run the script to start the container:

{{< tabpane code=true >}}
  {{< tab header="macOS and Linux" language="bash">}}
./start-dev.sh
  {{< /tab >}}
  {{< tab header="Windows (PowerShell)" language="powershell">}}
.\start-dev.ps1
  {{< /tab >}}
{{< /tabpane >}}

You'll see the following command prompt:

```output
developer@container_ID:~$
```

You're now inside the Docker container.

## Clone ExecuTorch in the container

Inside the Docker container, clone ExecuTorch v1.0.0:

```bash
cd /home/developer
# Clone ExecuTorch
git clone https://github.com/pytorch/executorch.git
cd executorch
# Checkout stable release
git checkout v1.0.0
# Initialize submodules
git submodule sync
git submodule update --init --recursive
```

{{% notice Note %}}
Submodule initialization might take 5-10 minutes depending on your connection.
{{% /notice %}}

Set the environment variable `ET_HOME`:

```bash
export ET_HOME=/home/developer/executorch
echo 'export ET_HOME=/home/developer/executorch' >> ~/.bashrc
```

## Install Python dependencies

Activate the Python environment and run the installer script:

```bash
# Ensure virtual environment is active
source ~/executorch-venv/bin/activate
cd $ET_HOME
# Upgrade pip
pip install --upgrade pip
# Install ExecuTorch base dependencies
./install_requirements.sh
# IMPORTANT: Install lxml with version compatible with Vela
# Vela 4.4.1 requires lxml>=4.7.1,<6.0.1
pip install 'lxml>=4.7.1,<6.0.1'
```

## Install ExecuTorch

After activating the environment, install ExecuTorch:

```bash
cd $ET_HOME
# Install ExecuTorch in editable mode
CMAKE_BUILD_PARALLEL_LEVEL=2 pip install --no-build-isolation -e .
```

{{% notice Note %}}
The `--no-build-isolation` flag is required so ExecuTorch finds the PyTorch installation from `install_requirements.sh`. 

`CMAKE_BUILD_PARALLEL_LEVEL=2` limits the number of parallel CMake build jobs during installation. This limit reduces peak memory usage and helps avoid out-of-memory failures.
{{% /notice %}}

Verify the installation:

```bash
python3 -c "from executorch.exir import to_edge; print('ExecuTorch installed successfully')"
```

The output is similar to:

```output
ExecuTorch installed successfully
```

## Set up Arm Ethos-U dependencies

Run the ExecuTorch Arm setup script:
```bash
cd $ET_HOME
# Run the Arm setup script
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

This script sets up the following dependencies:
- TOSA Libraries
- Ethos-U SDK structure
- CMake toolchain files

<!-- ### Download Arm GNU Toolchain

The setup script doesn't download the toolchain automatically. Download it manually:

```bash
cd $ET_HOME/examples/arm
mkdir -p ethos-u-scratch && cd ethos-u-scratch
# Detect architecture and download appropriate toolchain
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
    echo "Downloading toolchain for x86_64..."
    wget -q --show-progress https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz
    tar -xf arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz
    TOOLCHAIN_DIR="arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi"
else
    echo "Downloading toolchain for aarch64..."
    wget -q --show-progress https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-aarch64-arm-none-eabi.tar.xz
    tar -xf arm-gnu-toolchain-13.3.rel1-aarch64-arm-none-eabi.tar.xz
    TOOLCHAIN_DIR="arm-gnu-toolchain-13.3.rel1-aarch64-arm-none-eabi"
fi
# Clean up archive to save space
rm -f arm-gnu-toolchain-*.tar.xz*
# Add to PATH
export PATH="$(pwd)/$TOOLCHAIN_DIR/bin:$PATH"
echo "export PATH=\"$(pwd)/$TOOLCHAIN_DIR/bin:\$PATH\"" >> ~/.bashrc
```

{{% notice Note %}}
The toolchain download is approximately 139 MB and may take 10-30 minutes depending on your connection speed.
{{% /notice %}} -->

## Create an environment setup script

Create a reusable environment script for future sessions:

```bash
cat > $ET_HOME/setup_arm_env.sh << 'EOF'
#!/usr/bin/env bash

export ET_HOME=/home/developer/executorch
source ~/executorch-venv/bin/activate
if [ -f "$ET_HOME/examples/arm/arm-scratch/setup_path.sh" ]; then
  source "$ET_HOME/examples/arm/arm-scratch/setup_path.sh"
fi
if [ -f "$ET_HOME/examples/arm/ethos-u-scratch/setup_path.sh" ]; then
  source "$ET_HOME/examples/arm/ethos-u-scratch/setup_path.sh"
fi
export TARGET_CPU=cortex-m55
export ETHOSU_TARGET_NPU_CONFIG=ethos-u85-256
export SYSTEM_CONFIG=Ethos_U85_SYS_DRAM_Mid
export MEMORY_MODE=Shared_Sram
echo "ExecuTorch Arm environment loaded"
echo "ET_HOME: $ET_HOME"
echo "Vela: $(which vela 2>/dev/null || echo not found)"
EOF

chmod +x $ET_HOME/setup_arm_env.sh
echo 'source $ET_HOME/setup_arm_env.sh' >> ~/.bashrc
source $ET_HOME/setup_arm_env.sh
```

## Verify complete installation

Run all verification checks:

<!-- Check Arm GCC Toolchain

```bash
arm-none-eabi-gcc --version
```

Expected output:
```output
arm-none-eabi-gcc (Arm GNU Toolchain 13.3.Rel1 (Build arm-13.24)) 13.3.1 20240614
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
``` -->

1. Check Vela compiler

    ```bash
    vela --version
    ```

    The output is similar to:

    ```output
    4.4.1
    ```
2. Check ExecuTorch:

    ```bash
    python3 -c "from executorch.exir import to_edge; print('ExecuTorch OK')"
    ```

    The output is similar to:

    ```output
    ExecuTorch OK
    ```

3. Then, run a minimal export test to verify the complete setup:

    ```bash
    cd $ET_HOME
    python3 -m examples.arm.aot_arm_compiler --model_name=add --delegate --quantize   --target=ethos-u85-256 --output=/home/developer/output/add_ethos_u85.pte
    ```

    The output is similar to:

    ```output
    Exporting model add...
    Lowering to TOSA...
    Compiling with Vela...
    PTE file saved as add_ethos_u85.pte
    ```

    Verify the `.pte` file was created:

    ```bash
    ls -lh /home/developer/output/add_ethos_u85.pte
    ```

    The `output` directory is mounted from your host machine, so the file is also available at `~/mnist_alif/executorch-alif/output/`.

## (Optional) Save container state 

To preserve your work, you can commit the container to a new image:

```bash
# On your host machine (outside Docker)
docker commit executorch-alif-dev executorch-alif:configured
```

## What you've accomplished and what's next

You've now created a Docker environment for model export. The container has Python and PyTorch, ExecuTorch, and Ethos-U Vela installed. You've also mounted models and output directories on the container for sharing files with the host.

Next, you'll export a PyTorch model to ExecuTorch `.pte` format.

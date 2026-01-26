---
title: Set up Docker development environment
weight: 4
layout: learningpathall
---

## Overview

This section covers setting up a Docker-based development environment with ExecuTorch v1.0.0, the Arm toolchain, and Vela compiler for the Alif Ensemble E8.

## Why Docker?

Docker provides an isolated environment with:
- ExecuTorch v1.0.0 and dependencies
- Arm GNU Toolchain 13.3.rel1
- Vela 4.4.1 compiler for Ethos-U55
- Python 3.10+ with PyTorch
- Consistent build environment across platforms

## Project Structure

Create a workspace directory:

```bash
mkdir -p ~/executorch-alif/{models,output}
cd ~/executorch-alif
```

Your directory structure will be:

```
executorch-alif/
├── Dockerfile
├── start-dev.sh         (macOS/Linux)
├── start-dev.ps1        (Windows)
├── models/              (your PyTorch models)
└── output/              (compiled .pte files and binaries)
```

## Create the Dockerfile

Create a `Dockerfile` with all required dependencies:

```dockerfile
cat > Dockerfile << 'EOF'
# ExecuTorch Development Environment for Alif Ensemble E8
FROM ubuntu:22.04

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    xxd \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Create developer user
RUN useradd -m -s /bin/bash developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to developer user
USER developer
WORKDIR /home/developer

# Create Python virtual environment
RUN python3 -m venv ~/executorch-venv

# Activate venv and install Python dependencies
RUN /bin/bash -c "source ~/executorch-venv/bin/activate && \
    pip install --upgrade pip && \
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip install ethos-u-vela==4.4.1"

# Set up environment variables
ENV VIRTUAL_ENV=/home/developer/executorch-venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set working directory
WORKDIR /home/developer

CMD ["/bin/bash"]
EOF
```

## Build the Docker Image

Build the image (this takes 5-10 minutes):

```bash
docker build -t executorch-alif:latest .
```

The output shows:
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
docker images | grep executorch-alif
```

Expected output:
```output
executorch-alif    latest    container_ID    2 minutes ago    3.2GB
```

## Create Startup Scripts

### For macOS and Linux

Create `start-dev.sh`:

```bash
cat > start-dev.sh << 'EOF'
#!/bin/bash
# Start ExecuTorch development container with volume mounts

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

docker run -it --rm \
    --name executorch-alif-dev \
    -v "${SCRIPT_DIR}/models:/home/developer/models" \
    -v "${SCRIPT_DIR}/output:/home/developer/output" \
    -w /home/developer \
    executorch-alif:latest \
    /bin/bash
EOF

chmod +x start-dev.sh
```

### For Windows PowerShell

Create `start-dev.ps1`:

```powershell
cat > start-dev.ps1 << 'EOF'
# Start ExecuTorch development container with volume mounts
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

docker run -it --rm `
    --name executorch-alif-dev `
    -v "${ScriptDir}/models:/home/developer/models" `
    -v "${ScriptDir}/output:/home/developer/output" `
    -w /home/developer `
    executorch-alif:latest `
    /bin/bash
EOF
```

## Start the Development Container

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash">}}
./start-dev.sh
  {{< /tab >}}
  {{< tab header="Windows" language="powershell">}}
.\start-dev.ps1
  {{< /tab >}}
{{< /tabpane >}}

You should see the following prompt:

```output
developer@container_ID:~$
```

You are now inside the Docker container.

## Install ExecuTorch

Inside the Docker container, clone and install ExecuTorch v1.0.0:

### Clone the Repository

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
Submodule initialization may take 5-10 minutes depending on your connection.
{{% /notice %}}

### Set Environment Variables

```bash
# Set ExecuTorch home directory
export ET_HOME=/home/developer/executorch

# Add to bashrc for persistence
echo 'export ET_HOME=/home/developer/executorch' >> ~/.bashrc
```

### Install Python Dependencies

```bash
cd $ET_HOME

# Ensure virtual environment is active
source ~/executorch-venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install ExecuTorch base dependencies
./install_requirements.sh

# IMPORTANT: Install lxml with version compatible with Vela
# Vela 4.4.1 requires lxml>=4.7.1,<6.0.1
pip install 'lxml>=4.7.1,<6.0.1'
```

### Install ExecuTorch Python Package

```bash
cd $ET_HOME

# Install ExecuTorch in editable mode
pip install --no-build-isolation -e .
```

{{% notice Note %}}
The `--no-build-isolation` flag is required so ExecuTorch finds the PyTorch installation from `install_requirements.sh`.
{{% /notice %}}

Verify the installation:

```bash
python3 -c "from executorch.exir import to_edge; print('ExecuTorch installed successfully')"
```

Expected output:
```output
ExecuTorch installed successfully
```

## Set Up Arm Ethos-U Dependencies

### Run ExecuTorch Arm Setup Script

```bash
cd $ET_HOME

# Run the Arm setup script
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

This script sets up:
- TOSA Libraries
- Ethos-U SDK structure
- CMake toolchain files

### Download Arm GNU Toolchain

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
{{% /notice %}}

### Create Environment Setup Script

Create a reusable environment script for future sessions:

```bash
cat > $ET_HOME/setup_arm_env.sh << 'EOF'
#!/bin/bash
# ExecuTorch Arm Environment Setup for Alif E8

export ET_HOME=/home/developer/executorch

# Detect architecture
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
    TOOLCHAIN_DIR="arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi"
else
    TOOLCHAIN_DIR="arm-gnu-toolchain-13.3.rel1-aarch64-arm-none-eabi"
fi

# Add toolchain to PATH
export PATH="$ET_HOME/examples/arm/ethos-u-scratch/$TOOLCHAIN_DIR/bin:$PATH"

# Alif E8 Target Configuration (Ethos-U55 with 128 MACs)
export TARGET_CPU=cortex-m55
export ETHOSU_TARGET_NPU_CONFIG=ethos-u55-128
export SYSTEM_CONFIG=Ethos_U55_High_End_Embedded
export MEMORY_MODE=Shared_Sram

echo "ExecuTorch Arm environment loaded"
echo "  ET_HOME: $ET_HOME"
echo "  Toolchain: $(which arm-none-eabi-gcc 2>/dev/null || echo 'NOT FOUND')"
echo "  Vela: $(which vela 2>/dev/null || echo 'NOT FOUND')"
echo "  Target: $TARGET_CPU + $ETHOSU_TARGET_NPU_CONFIG"
EOF

chmod +x $ET_HOME/setup_arm_env.sh

# Source it now
source $ET_HOME/setup_arm_env.sh

# Add to bashrc for persistence
echo 'source $ET_HOME/setup_arm_env.sh' >> ~/.bashrc
```

## Verify Complete Installation

Run all verification checks:

### Check Arm GCC Toolchain

```bash
arm-none-eabi-gcc --version
```

Expected output:
```output
arm-none-eabi-gcc (Arm GNU Toolchain 13.3.Rel1 (Build arm-13.24)) 13.3.1 20240614
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

### Check Vela Compiler

```bash
vela --version
```

Expected output:
```output
4.4.1
```

### Check ExecuTorch

```bash
python3 -c "from executorch.exir import to_edge; print('ExecuTorch OK')"
```

Expected output:
```output
ExecuTorch OK
```

## Alif E8 Target Configuration Reference

| Parameter | Value | Description |
|-----------|-------|-------------|
| `TARGET_CPU` | `cortex-m55` | CPU core target |
| `ETHOSU_TARGET_NPU_CONFIG` | `ethos-u55-128` | NPU with 128 MAC units |
| `SYSTEM_CONFIG` | `Ethos_U55_High_End_Embedded` | Performance profile |
| `MEMORY_MODE` | `Shared_Sram` | CPU/NPU share SRAM |

### Alif E8 Memory Map

| Region | Address | Size | Usage |
|--------|---------|------|-------|
| ITCM | 0x00000000 | 256 KB | Fast code execution |
| DTCM | 0x20000000 | 256 KB | Fast data access |
| MRAM | 0x80000000 | 5.5 MB | Main code storage |
| SRAM0 | 0x02000000 | 4 MB | General SRAM |
| SRAM1 | 0x08000000 | 4 MB | NPU tensor arena |

## Quick Verification Test

Run a minimal export test to verify the complete setup:

```bash
cd $ET_HOME

python3 -m examples.arm.aot_arm_compiler \
    --model_name=add \
    --delegate \
    --quantize \
    --target=ethos-u55-128 \
    --system_config=Ethos_U55_High_End_Embedded \
    --memory_mode=Shared_Sram
```

Expected output:
```output
Exporting model add...
Lowering to TOSA...
Compiling with Vela...
PTE file saved as add_arm_delegate_ethos-u55-128.pte
```

Verify the `.pte` file was created:

```bash
ls -la *.pte
```

The output shows:
```output
-rw-r--r-- 1 developer developer 1234 Dec 14 12:00 add_arm_delegate_ethos-u55-128.pte
```

## Directory Structure After Setup

```
/home/developer/
├── executorch/
│   ├── setup_arm_env.sh              # Environment script (created above)
│   ├── examples/
│   │   └── arm/
│   │       ├── setup.sh              # ExecuTorch Arm setup script
│   │       ├── aot_arm_compiler.py   # Model export script
│   │       ├── ethos-u-scratch/      # Downloaded tools
│   │       │   └── arm-gnu-toolchain-13.3.rel1-*/
│   │       └── ethos-u-setup/
│   │           ├── arm-none-eabi-gcc.cmake
│   │           └── ethos-u/
│   └── backends/
│       └── arm/                      # Arm backend implementation
├── executorch-venv/                  # Python virtual environment
├── models/                           # Your PyTorch models (mounted)
└── output/                           # Build artifacts (mounted)
```

## Save Container State (Optional)

To preserve your work, you can commit the container to a new image:

```bash
# On your host machine (outside Docker)
docker commit executorch-alif-dev executorch-alif:configured
```

## Working with Mounted Directories

Files in `/home/developer/models` and `/home/developer/output` inside the container are automatically synced with `~/executorch-alif/models` and `~/executorch-alif/output` on your host machine.

This allows you to:
- Edit models on your host machine
- Access compiled `.pte` files on your host for flashing
- Preserve work between container sessions

## Summary

You have:
- ✅ Created a Docker development environment
- ✅ Installed ExecuTorch v1.0.0
- ✅ Set up Arm GNU Toolchain 13.3.rel1
- ✅ Installed Vela 4.4.1 compiler
- ✅ Configured Alif E8 target settings
- ✅ Verified the complete installation

In the next section, you'll export a PyTorch model to ExecuTorch `.pte` format.

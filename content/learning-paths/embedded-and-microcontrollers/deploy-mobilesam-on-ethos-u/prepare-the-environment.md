---
title: Prepare the ExecuTorch and Arm environment
description: Set up ExecuTorch, Ethos-U dependencies, the Arm GNU Toolchain, and the Corstone-320 FVP to build and run the MobileSAM example.
weight: 3

layout: "learningpathall"
---

## Check your development machine

Run the following preflight check before downloading the source:

```bash
case "$(uname -s)/$(uname -m)" in
  Linux/x86_64|Linux/aarch64|Linux/arm64|Darwin/arm64)
    echo "Supported host: $(uname -s)/$(uname -m)"
    ;;
  *)
    echo "Unsupported host: $(uname -s)/$(uname -m)" >&2
    exit 1
    ;;
esac

for tool in python3.12 git cmake c++; do
  command -v "$tool" >/dev/null || {
    echo "Missing required tool: $tool" >&2
    exit 1
  }
done

if ! command -v ninja >/dev/null && ! command -v make >/dev/null; then
  echo "Install Ninja or Make before continuing." >&2
  exit 1
fi

python3.12 --version
git --version
cmake --version | head -n 1
c++ --version | head -n 1
```

The check confirms that you are using a supported Linux host or Apple silicon Mac. It also checks for the availability of the following:

- Python 3.12
- Git
- CMake
- A host C++ compiler
- Ninja or Make

## Clone the ExecuTorch source

Clone ExecuTorch and initialize its submodules:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 4fd161058ebe2b9d80d11242a9d21811c0e92dac
git submodule sync
git submodule update --init --recursive
```

Run the remaining commands from the ExecuTorch repository root.

## Create a Python environment

Create and activate a Python 3.12 virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the current ExecuTorch checkout with its Ethos-U dependencies:

```bash
./install_executorch.sh --optional-dependency ethos_u
python -m pip install -r \
  examples/arm/mobilesam_prompt_segmentation_example_ethos_u/requirements.txt
```

Using the checkout's installer keeps the Python package aligned with the example source.

## Install the Arm development tools

{{% notice Note %}}
Before you run the Arm setup command on macOS, install [Docker Desktop](/install-guides/docker/docker-desktop/) and follow the [AVH FVPs on macOS install guide](/install-guides/fvps-on-macos/). Add the FVPs-on-Mac `bin` directory to `PATH`. The wrapper runs the Linux Corstone-320 FVP in a container. Confirm that Docker is running and that `FVP_Corstone_SSE-320` resolves to the wrapper:

```bash
docker info >/dev/null
command -v FVP_Corstone_SSE-320
```
{{% /notice %}}

The Arm setup script installs the pinned GNU bare-metal toolchain, Ethos-U Vela compiler, and Corstone FVP used by the example. Read the End User License Agreements presented by the tooling before you accept them, then run:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```

## Verify the environment

Confirm that Python imports ExecuTorch:

```bash
python -c "import executorch; print('ExecuTorch import succeeded')"
```

The output is similar to:

```output
ExecuTorch import succeeded
```

Check the target compiler and FVP:

```bash
arm-none-eabi-gcc -dumpmachine
command -v FVP_Corstone_SSE-320
```

The output of the first command is similar to:

```output
arm-none-eabi
```

The second command prints the path to the Corstone-320 FVP. On macOS, confirm that this path is inside the FVPs-on-Mac `bin` directory.

## What you've accomplished and what's next

You've installed the Python, compiler, Vela, and virtual-platform dependencies used by the example.

Next, you'll prepare and export MobileSAM for Ethos-U85.

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

python3.12 - <<'PY' || exit 1
import platform
import sys

if sys.platform == "darwin":
    version = platform.mac_ver()[0]
    if not version or int(version.split(".")[0]) < 15:
        raise SystemExit(f"macOS 15 or later is required; found {version or 'unknown'}.")
elif sys.platform.startswith("linux"):
    libc, version = platform.libc_ver()
    if libc != "glibc" or tuple(map(int, version.split(".")[:2])) < (2, 28):
        raise SystemExit(
            f"Linux with glibc 2.28 or later is required; found {libc} {version}."
        )
PY

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

The Python export dependencies require macOS 15 or later on Apple silicon, or glibc 2.28 or later on Linux. The pinned [TOSA tools](https://pypi.org/project/tosa-tools/2026.5.0/#files) set the macOS minimum, and the [PyTorch wheels](https://pypi.org/project/torch/2.14.0/#files) require the Linux glibc version. The preflight check verifies these requirements before you install the dependencies.

On Linux, the Corstone-320 FVP also requires `libstdc++.so.6` providing `GLIBCXX_3.4.26` or later.

## Clone the ExecuTorch source

Clone ExecuTorch, select the revision used by this Learning Path, and initialize its submodules:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 5c4d2c4a0150a0809bc77be9a67093f80f60a60f
git submodule sync
git submodule update --init --recursive
```

Run the remaining commands from the ExecuTorch repository root. The pinned revision keeps the commands aligned with the [MobileSAM example source](https://github.com/pytorch/executorch/tree/5c4d2c4a0150a0809bc77be9a67093f80f60a60f/examples/arm/mobilesam_prompt_segmentation_example_ethos_u).

## Create a Python environment

Create and activate a fresh Python 3.12 virtual environment for this checkout:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

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

## Install ExecuTorch

Remove unused developer packages installed by Arm setup:

```bash
python -m pip uninstall -y \
  tosa-adapter-model-explorer ai-edge-model-explorer \
  pte-adapter-model-explorer pytest-timeout
```

Install released PyTorch, Torchvision, and TorchAO packages. Linux uses the stable CPU wheel index; macOS uses the Apple silicon wheels from PyPI:

```bash
case "$(uname -s)" in
  Linux)
    python -m pip install \
      --index-url https://pypi.org/simple \
      --extra-index-url https://download.pytorch.org/whl/cpu \
      'torch==2.14.0+cpu' 'torchvision==0.29.0+cpu' 'torchao==0.18.0+cpu'
    ;;
  Darwin)
    python -m pip install --index-url https://pypi.org/simple \
      'torch==2.14.0' 'torchvision==0.29.0' 'torchao==0.18.0'
    ;;
  *)
    echo "Use a supported Linux host or Apple silicon Mac." >&2
    exit 1
    ;;
esac
```

Install the source build dependencies and the `timm` version used by the pinned MobileSAM example:

```bash
python -m pip install --index-url https://pypi.org/simple \
  'cmake==3.31.10' 'packaging==26.3' 'setuptools==84.0.0' \
  'wheel==0.48.0' 'pyyaml==6.0.3' 'zstd==1.5.7.2' \
  'certifi==2026.7.22' 'patchelf==0.19.1.0; sys_platform == "linux"' \
  'timm==1.0.7'
```

Build and install ExecuTorch from the same checkout used by the example and native runner:

```bash
CMAKE_ARGS='-DEXECUTORCH_BUILD_MLX=OFF' env -u DEBUG \
  python -m pip install --no-build-isolation '.[ethos_u]'
python -m pip check
```

Installing the Ethos-U extra after Arm setup resolves its older FlatBuffers dependency. Before exporting, confirm that `pip check` reports `No broken requirements found.`

These commands replace `install_executorch.sh` and its TorchAO nightly with released dependencies. If you rerun Arm setup, repeat the package removal and Python installation steps.

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

## Choose how to run the example

To run preparation, export, build, FVP execution, and validation together, use the example's script without arguments:

```bash
./examples/arm/mobilesam_prompt_segmentation_example_ethos_u/run.sh
```

The expected output at the end of a successful run is:

```output
MobileSAM example: PASS
```

The comparison image, `fvp_comparison.png`, is saved under `arm_test/mobilesam/result/`. After the script completes, continue to [Validate the MobileSAM segmentation result](../validate-the-results/) to inspect the artifacts.

To work through each stage manually, skip this script and continue to the next page. The following pages explain the same preparation, export, build, and validation steps. Continue only after each command succeeds; files from an earlier run can remain after a failed command.

## What you've accomplished and what's next

You've installed the Python, compiler, Vela, and virtual-platform dependencies used by the example.

Next, you'll prepare and export MobileSAM for Ethos-U85.

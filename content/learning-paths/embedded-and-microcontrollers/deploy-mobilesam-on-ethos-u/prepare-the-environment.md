---
title: Prepare the ExecuTorch and Arm environment
description: Set up ExecuTorch, Ethos-U dependencies, the Arm GNU Toolchain, and the Corstone-320 FVP to build and run the MobileSAM example.
weight: 3

layout: "learningpathall"
---

## Check your development machine

Use Python 3.12 with development headers and virtual-environment support. On Linux, also install the GLib and OpenMP runtime packages (`libglib2.0-0` and `libgomp1` on Ubuntu). Run the following preflight check before downloading the source:

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

for tool in python3.12 git c++ ninja curl pkg-config xz; do
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

python3.12 --version
git --version
c++ --version | head -n 1
```

The check confirms that you are using a supported Linux host or Apple silicon Mac. It also checks for the availability of the following:

- Python 3.12
- Git
- A host C++ compiler
- Ninja
- curl, pkg-config, and xz

The Python export dependencies require macOS 15 or later on Apple silicon, or glibc 2.28 or later on Linux. The pinned [TOSA tools](https://pypi.org/project/tosa-tools/2026.5.0/#files) set the macOS minimum, and the [PyTorch wheels](https://pypi.org/project/torch/2.14.0/#files) require the Linux glibc version. The preflight check verifies these requirements before you install the dependencies.

On Linux, the Corstone-320 FVP also requires `libstdc++.so.6` providing `GLIBCXX_3.4.26` or later.

## Clone the ExecuTorch source

Clone ExecuTorch, select the revision used by this Learning Path, and initialize its submodules:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git fetch origin fe93a8b0fc8d363fbb3bfa2aa18e253507fd13f8
git checkout fe93a8b0fc8d363fbb3bfa2aa18e253507fd13f8
git submodule sync
git submodule update --init --recursive
```

Run the remaining commands from the ExecuTorch repository root. The pinned revision keeps the commands aligned with the [MobileSAM example source](https://github.com/pytorch/executorch/tree/fe93a8b0fc8d363fbb3bfa2aa18e253507fd13f8/examples/arm/mobilesam_prompt_segmentation_example_ethos_u).

## Create a Python environment

Create and activate a fresh Python 3.12 virtual environment for this checkout:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

## Install ExecuTorch

Build the Python package from the same checkout used by the example and native runner:

```bash
CMAKE_GENERATOR=Ninja ./install_executorch.sh --optional-dependency ethos_u
```

The installer supplies CMake, the model export dependencies, and the example requirements. It selects released PyTorch and TorchAO packages for the CPU workflow.

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

Check that the Python dependencies are consistent after Arm setup:

```bash
python -m pip check
```

Confirm that the output is `No broken requirements found.`

Check the ExecuTorch and Ethos-U imports used by the exporter:

```bash
python - <<'PYTHON'
import executorch.kernels.quantized
from executorch.backends.arm.ethosu import EthosUPartitioner
from executorch.backends.arm.quantizer import EthosUQuantizer

print("ExecuTorch Ethos-U imports succeeded")
PYTHON
```

The output is similar to:

```output
ExecuTorch Ethos-U imports succeeded
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

To run the same workflow with simulated NPU counters, use timing mode:

```bash
./examples/arm/mobilesam_prompt_segmentation_example_ethos_u/run.sh --timed
```

Timing mode uses a 7,200-second timeout; the default fast mode uses 300 seconds. CPU timing and CPU/NPU ratios remain unavailable on FVP.

To work through each stage manually, skip this script and continue to the next page. The following pages explain the same preparation, export, build, and validation steps. Continue only after each command succeeds; files from an earlier run can remain after a failed command.

## What you've accomplished and what's next

You've installed the Python, compiler, Vela, and virtual-platform dependencies used by the example.

Next, you'll prepare and export MobileSAM for Ethos-U85.

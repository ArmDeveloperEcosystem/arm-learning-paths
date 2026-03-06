---
title: Compile the model on an Arm cloud instance
weight: 3

layout: "learningpathall"
---

## Why an Arm cloud instance?

ExecuTorch's Arm backend build scripts are designed for native Arm compilation. The Vela compiler, which generates optimized command streams for Ethos-U NPUs, and the CMSIS-NN kernels all target Arm natively. Using an Arm-based EC2 instance avoids the complexity of cross-compilation from x86.

In this section, you launch a Graviton-based EC2 instance, install ExecuTorch, compile a MobileNetV2 model for the Ethos-U85, and build the ExecuTorch static libraries that your firmware will link against.

## Launch an EC2 instance

Create an AWS EC2 instance with the following configuration:

- **Instance type**: `c7g.4xlarge` (Arm Graviton3, 16 vCPUs, 32 GB RAM)
- **OS**: Ubuntu 22.04 LTS
- **Storage**: 50 GB

The 16 cores speed up the ExecuTorch build significantly, and the 50 GB disk accommodates the repository, submodules, and build artifacts.

Set up your SSH config so you can connect with a short alias (for example, `ssh alif`). This makes the `scp` commands later more convenient.

## Install system dependencies

Connect to your instance and install the required packages:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y \
  git \
  cmake \
  ninja-build \
  build-essential \
  python3.10 \
  python3.10-venv \
  python3-pip \
  unzip \
  wget \
  rsync
```

Reboot if the kernel was updated:

```bash
sudo reboot
```

After reconnecting, verify that Python 3.10 is available:

```bash
python3 --version
```

The output is similar to:

```output
Python 3.10.12
```

## Set up the Python environment

Create an isolated Python environment and install PyTorch:

```bash
python3 -m venv ~/venv_executorch
source ~/venv_executorch/bin/activate

pip install --upgrade pip setuptools wheel ninja cmake
pip install pyyaml
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install pillow
```

You use CPU-only PyTorch because this instance has no GPU. You only need PyTorch for model export and ahead-of-time compilation; the actual inference happens on the microcontroller.

Verify the installation:

```bash
python - <<'PY'
import torch, torchvision
print(torch.__version__, torchvision.__version__)
PY
```

## Clone and install ExecuTorch

```bash
mkdir -p ~/alif
cd ~/alif
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 40d94b6d62a195a2f46b2baa20383fa4af27f7d4
git submodule update --init --recursive
```

{{% notice Note %}}
The `git checkout` command pins ExecuTorch to a known-working commit. The Arm backend and Vela toolchain integration can change between commits, so pinning avoids unexpected breakage.
{{% /notice %}}

Install the ExecuTorch Python package:

```bash
python -m pip install -e . --no-build-isolation
```

## Set up the Arm/Ethos-U toolchain

ExecuTorch includes a setup script that downloads the Arm GNU toolchain, CMSIS, and the Vela compiler:

```bash
cd ~/alif/executorch
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

{{% notice Note %}}
The setup script may fail at the `tosa_serialization_lib` build step due to a pybind11 version incompatibility. If you see an error containing `def_property family does not currently support keep_alive`, run the following commands to complete the setup manually:

```bash
pip install "pybind11<2.14" scikit-build-core setuptools_scm

CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install --no-build-isolation \
  --no-dependencies \
  ~/alif/executorch/examples/arm/arm-scratch/tosa-tools/serialization

pip install --no-dependencies \
  -r ~/alif/executorch/backends/arm/requirements-arm-ethos-u.txt
```

The first command installs a pybind11 version that doesn't have the breaking change, along with the build tools that the serialization library needs. The second command builds and installs the serialization library using those local packages instead of downloading new ones. The third command installs the Ethos-U Vela compiler, which the setup script never reached due to the earlier failure.
{{% /notice %}}

Source the environment paths that the setup script generated:

```bash
source examples/arm/arm-scratch/setup_path.sh
```

After the setup script, reinstall ExecuTorch and its dependencies:

```bash
python -m pip install -e . --no-build-isolation
pip install "torchao==0.15.0"
```

## Compile MobileNetV2 for Ethos-U85

Source the setup paths and run the ahead-of-time compiler:

```bash
cd ~/alif/executorch
source examples/arm/arm-scratch/setup_path.sh

mkdir -p ~/alif/models

python -m examples.arm.aot_arm_compiler \
  -m mv2 \
  -q \
  -d \
  -t ethos-u85-256 \
  -o ~/alif/models/mv2_ethosu85_256.pte
```

The flags are:
- `-m mv2`: MobileNetV2 model
- `-q`: quantize the model (int8)
- `-d`: delegate computation to the NPU
- `-t ethos-u85-256`: target the Ethos-U85 with 256 MAC configuration
- `-o`: output path for the compiled `.pte` file

Verify the output:

```bash
ls -lh ~/alif/models/mv2_ethosu85_256.pte
```

The file should be approximately 3.7 MB. This `.pte` file contains the model graph, quantized weights, and the Vela-compiled command stream that the Ethos-U85 executes directly.

## Build ExecuTorch static libraries

Your firmware needs to link against ExecuTorch's runtime libraries. Build them for bare-metal Cortex-M:

```bash
cd ~/alif/executorch
source ~/venv_executorch/bin/activate

rm -rf cmake-out
bash backends/arm/scripts/build_executorch.sh
```

This step takes several minutes. When complete, list the output libraries:

```bash
find arm_test/cmake-out -type f -name "*.a" | sort
```

You should see approximately 13 libraries, including `libexecutorch.a`, `libexecutorch_core.a`, `libexecutorch_delegate_ethos_u.a`, `libcortex_m_ops_lib.a`, and `libcmsis-nn.a`.

## Package headers and libraries

Bundle the headers and libraries for transfer to your development machine:

```bash
cd ~/alif/executorch

rm -rf ~/alif/et_bundle
mkdir -p ~/alif/et_bundle
cp -a arm_test/cmake-out/include ~/alif/et_bundle/
cp -a arm_test/cmake-out/lib     ~/alif/et_bundle/

tar -C ~/alif -czf ~/alif/et_bundle.tar.gz et_bundle
ls -lh ~/alif/et_bundle.tar.gz
```

## Transfer artifacts to your development machine

Run these commands on your Mac or Linux development machine (not on the EC2 instance). The paths below use `~/repo/alif/` as the working directory; adjust these to match your own project location:

```bash
mkdir -p ~/repo/alif/models
mkdir -p ~/repo/alif/third_party/executorch/lib

scp alif:/home/ubuntu/alif/models/mv2_ethosu85_256.pte ~/repo/alif/models/
scp alif:/home/ubuntu/alif/et_bundle.tar.gz ~/repo/alif/models/
scp 'alif:/home/ubuntu/alif/executorch/arm_test/cmake-out/lib/*.a' \
  ~/repo/alif/third_party/executorch/lib/
```

Verify the transfer:

```bash
ls -lh ~/repo/alif/models/mv2_ethosu85_256.pte
ls ~/repo/alif/third_party/executorch/lib/*.a | wc -l
```

You should see the 3.7 MB model file and 13 library files.

## Convert the model to a C header

The firmware embeds the model as a byte array in flash memory. Use `xxd` to generate a C header:

```bash
cd ~/repo/alif/models
xxd -i mv2_ethosu85_256.pte > mv2_ethosu85_256_pte.h
```

Open `mv2_ethosu85_256_pte.h` and change the first line from:

```c
unsigned char mv2_ethosu85_256_pte[] = {
```

to:

```c
#include <stdint.h>
const uint8_t __attribute__((aligned(16))) mv2_ethosu85_256_pte[] = {
```

The `aligned(16)` attribute is required because the Ethos-U85 needs the Vela command stream data aligned to 16 bytes. Without it, the NPU driver will report an alignment error at runtime.

## Extract the header bundle

On your development machine, extract the ExecuTorch headers into the VS Code template project:

```bash
cd ~/repo/alif/alif_vscode-template
mkdir -p third_party/executorch
tar -C third_party/executorch -xzf ~/repo/alif/models/et_bundle.tar.gz
```

Verify the headers are in place:

```bash
ls third_party/executorch/et_bundle/include/executorch/
```

You should see `runtime/` and other directories.

You now have the compiled model, prebuilt libraries, and headers on your development machine, ready to integrate into the firmware project.

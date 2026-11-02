---
title: Prepare the environment and model inputs
description: Install ExecuTorch and the Arm tools, then prepare the Silero VAD model and audio inputs.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the workflow

Voice activity detection (VAD) classifies short audio frames as speech or silence. VAD is useful for voice assistants, transcription pipelines, and other systems that should avoid processing silent audio.

You'll deploy the 16 kHz Silero VAD model with ExecuTorch. The workflow quantizes the model, lowers supported operations to the Arm Ethos-U backend, builds a bare-metal application, and runs it on a Corstone-320 Fixed Virtual Platform (FVP). You don't need a physical development board.

The application processes 512 audio samples every 32 ms. It keeps the long short-term memory (LSTM) hidden and cell state inside the ExecuTorch program between frames, then produces one speech probability for each frame.

The host uses the validation clip to generate reference probabilities. The bare-metal application processes the same clip on the FVP. The final comparison verifies that both paths produce the same speech decisions.

![Three-lane workflow showing host preparation from the Silero model and source audio to a stateful PTE, virtual target execution from the embedded PTE and validation audio to an FVP log, and host verification that compares reference probabilities with the FVP result.#center](silero-vad-deployment-lanes.svg "Silero VAD workflow separated into prepare, run, and verify lanes")

Use the FVP for functional validation. The FVP's Ethos-U model is cycle accurate, but don't use its Cortex-M CPU model for CPU performance measurements.

## Check your development machine

Use Python 3.12 with development headers and virtual-environment support. The release wheels require glibc 2.28 or later on Linux, or macOS 15 or later on Apple silicon. On Linux, the FVP also requires `libstdc++.so.6` providing `GLIBCXX_3.4.26` or later. Run the following preflight check before downloading the source; CMake is installed in the virtual environment later:

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

for tool in python3.12 git c++ curl; do
  command -v "$tool" >/dev/null || {
    echo "Missing required tool: $tool" >&2
    exit 1
  }
done

if ! command -v ninja >/dev/null && ! command -v make >/dev/null; then
  echo "Install Ninja or Make before continuing." >&2
  exit 1
fi

printf 'int main() { return 0; }\n' | \
  c++ -std=c++17 -x c++ -fsyntax-only -

python3.12 --version
```

## Create an isolated ExecuTorch environment

Use the source revision from the Silero VAD end-to-end example with the released ExecuTorch `1.5.1` Python package:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git fetch origin d78bc1b0ba1c33a90d2d93662de118577f37efd4
git checkout d78bc1b0ba1c33a90d2d93662de118577f37efd4
git submodule sync --recursive
git submodule update --init --recursive
```

Confirm the checked-out revision:

```bash
git rev-parse --short=12 HEAD
```

The expected output is:

```output
d78bc1b0ba1c
```

Create and activate a Python virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## Install the Arm backend tools

The Arm setup script installs the Arm GNU Toolchain and, on Linux, the Corstone FVPs. Review the license terms presented by the script before using its EULA acceptance option.

{{% notice macOS %}}
Before running Arm setup, install [Docker Desktop](/install-guides/docker/docker-desktop/) and start Docker. Install the [FVPs-on-Mac wrappers](https://github.com/Arm-Examples/FVPs-on-Mac) at the revision for FVP `11.31.28`:

```bash
mkdir -p examples/arm/arm-scratch "$HOME/.armlm"
git clone https://github.com/Arm-Examples/FVPs-on-Mac.git \
  examples/arm/arm-scratch/FVPs-on-Mac
git -C examples/arm/arm-scratch/FVPs-on-Mac checkout --detach \
  cc7a4be5456db085619647811fac29e9795f806e
bash examples/arm/arm-scratch/FVPs-on-Mac/build.sh
export PATH="$PWD/examples/arm/arm-scratch/FVPs-on-Mac/bin:$PATH"
export FVP_MOUNT_DIR="$PWD"
FVP_Corstone_SSE-320 --version
```
{{% /notice %}}

Install released PyTorch and run Arm setup from the ExecuTorch repository root. The setup options select the cross-compiler and FVPs; the next section installs the Python export tools:

```bash
python -m pip install "torch==2.14.0" --index-url https://download.pytorch.org/whl/cpu
./examples/arm/setup.sh --i-agree-to-the-contained-eula \
  --disable-ethos-u-deps --enable-baremetal-toolchain --enable-fvps
```

## Install ExecuTorch

Install the released ExecuTorch package and its Ethos-U dependencies:

```bash
python -m pip install "executorch[ethos_u]==1.5.1" "torchao==0.18.0" "cmake<4" pytest
source examples/arm/arm-scratch/setup_path.sh
```

The path script adds the downloaded cross-compiler and, on Linux, FVP binaries to the current shell. Check the target tools and Python installation:

```bash
command -v arm-none-eabi-g++
command -v FVP_Corstone_SSE-320
python -m pip check
python - <<'PY'
import executorch.codegen.tools.selective_build
from executorch.backends.arm.ethosu import EthosUPartitioner
from executorch.backends.arm.quantizer import EthosUQuantizer

print("ExecuTorch installation verified")
PY
```

The Python checks should report `No broken requirements found.` and `ExecuTorch installation verified`.

In each new shell, return to the ExecuTorch repository root and restore the environment and tool paths:

```bash
source .venv/bin/activate
source examples/arm/arm-scratch/setup_path.sh
if [ "$(uname -s)" = Darwin ]; then
  export PATH="$PWD/examples/arm/arm-scratch/FVPs-on-Mac/bin:$PATH"
  export FVP_MOUNT_DIR="$PWD"
fi
```

## Download the model and sample audio

Create a directory for the model and audio inputs:

```bash
mkdir -p silero-vad
```

Download the model and sample audio from the tested Silero VAD revision:

```bash
curl --fail --location \
  --output silero-vad/silero_vad.jit \
  https://raw.githubusercontent.com/snakers4/silero-vad/dbacf536adadf42210f37ae50fbaf75f6235b3cf/src/silero_vad/data/silero_vad.jit

curl --fail --location \
  --output silero-vad/test.wav \
  https://raw.githubusercontent.com/snakers4/silero-vad/dbacf536adadf42210f37ae50fbaf75f6235b3cf/tests/data/test.wav
```

## Create the validation clip

Use the example's helper to take the first 40,000 samples of `test.wav`. This creates a 2.5-second validation clip that fits the runtime's audio limit and produces 79 frames:

```bash
python examples/arm/silero_vad_example_ethos_u/model_export/generate_smoke_audio.py \
  --source-wav silero-vad/test.wav \
  --output silero-vad/validation.wav
```

Use `test.wav` for calibration and `validation.wav` for the host reference and FVP. These recordings overlap to check deployment consistency. Use representative calibration audio and separate validation recordings when measuring model quality.

## What you've accomplished and what's next

You've installed the pinned ExecuTorch source, prepared the Arm tools, and created the model inputs.

Next, you'll export the model as a quantized ExecuTorch program for Ethos-U85.

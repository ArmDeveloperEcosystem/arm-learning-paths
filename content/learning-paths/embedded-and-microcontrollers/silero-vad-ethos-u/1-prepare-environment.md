---
title: Prepare the environment and model inputs
description: Install ExecuTorch and the Arm tools, then prepare the Silero VAD model and audio inputs.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the workflow

Voice activity detection (VAD) classifies short audio frames as speech or silence. It is useful for voice assistants, transcription pipelines, and other systems that should avoid processing silent audio.

You will deploy the 16 kHz Silero VAD model with ExecuTorch. The workflow quantizes the model, lowers supported operations to the Arm Ethos-U backend, builds a bare-metal application, and runs it on a Corstone-320 Fixed Virtual Platform (FVP). You do not need a physical development board.

The application processes 512 audio samples every 32 ms. It keeps the long short-term memory (LSTM) hidden and cell state inside the ExecuTorch program between frames, then produces one speech probability for each frame.

The validation clip follows two paths. The host uses it to generate reference probabilities, while the bare-metal application processes the same clip on the FVP. The final comparison verifies that both paths produce the same speech decisions.

![Three-lane workflow showing host preparation from the Silero model and source audio to a stateful PTE, virtual target execution from the embedded PTE and validation audio to an FVP log, and host verification that compares reference probabilities with the FVP result.#center](silero-vad-deployment-lanes.svg "Silero VAD workflow separated into prepare, run, and verify lanes")

Use the FVP for functional validation. Its Ethos-U model is cycle accurate, but don't use its Cortex-M CPU model for CPU performance measurements.

## Check your development machine

Run this preflight check before downloading the source:

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

for tool in python3 git cmake c++ curl; do
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

python3 - <<'PY'
import re
import subprocess
import sys

if not (3, 10) <= sys.version_info[:2] <= (3, 13):
    raise SystemExit("Python 3.10 through 3.13 is required")

output = subprocess.check_output(["cmake", "--version"], text=True)
version = tuple(map(int, re.search(r"\d+(?:\.\d+)+", output).group().split(".")[:2]))
if version < (3, 24):
    raise SystemExit("CMake 3.24 or later is required")

print(f"Python {sys.version.split()[0]}")
print(output.splitlines()[0])
PY
```

## 1. Create an isolated ExecuTorch environment

The Silero VAD Ethos-U example is available in the upstream ExecuTorch repository. Use the tested main-branch commit so that the commands and generated artifacts match this Learning Path.

Clone ExecuTorch and check out the tested revision:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 4fd161058ebe2b9d80d11242a9d21811c0e92dac
git submodule sync --recursive
git submodule update --init --recursive
```

Confirm the checked-out revision:

```bash
git rev-parse --short=12 HEAD
```

The expected output is:

```output
4fd161058ebe
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install ExecuTorch and its Python dependencies:

```bash
CMAKE_ARGS="-DEXECUTORCH_BUILD_MLX=OFF" \
  env -u DEBUG ./install_executorch.sh \
  --minimal --optional-dependency ethos_u

python - <<'PY'
import executorch.codegen.tools.selective_build
from executorch.backends.arm.ethosu import EthosUPartitioner
from executorch.backends.arm.quantizer import EthosUQuantizer

print("ExecuTorch installation verified")
PY
```

The installation script initializes the Git submodules needed by the build and installs the matching PyTorch and ExecuTorch packages. The command omits the unrelated MLX backend and optional packages used by other examples.

## 2. Install the Arm backend tools

The Arm setup script downloads the Arm GNU Toolchain, Ethos-U Vela compiler, and supporting Python packages. On Linux it also installs the Corstone FVPs. Review the license terms presented by the script before using its EULA acceptance option.

{{% notice macOS %}}
Before you run the Arm setup command on macOS, install Docker Desktop and follow the [AVH FVPs on macOS install guide](/install-guides/fvps-on-macos/). Add the FVPs-on-Mac `bin` directory to `PATH`. Confirm that Docker is running and that `FVP_Corstone_SSE-320` resolves to the wrapper:

```bash
docker info >/dev/null
command -v FVP_Corstone_SSE-320
```
{{% /notice %}}

Run the setup script from the ExecuTorch repository root:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```

The second command adds the downloaded cross-compiler and, on Linux, FVP binaries to the current shell environment. Run it again when you start a new shell.

Check that the two target tools are available:

```bash
command -v arm-none-eabi-g++
command -v FVP_Corstone_SSE-320
```

The compiler resolves under `examples/arm/arm-scratch/`. On Linux, the FVP does too; on macOS, it resolves under the FVPs-on-Mac wrapper directory. If the compiler is missing, source `examples/arm/arm-scratch/setup_path.sh` again. If the FVP is missing on macOS, add the wrapper directory to `PATH`.

## 3. Download the model and sample audio

Create one workspace for the files generated in this Learning Path:

```bash
mkdir -p silero-vad-work/{assets,export}
```

Download the model and sample audio from the tested Silero VAD revision:

```bash
curl --fail --location \
  --output silero-vad-work/assets/silero_vad.jit \
  https://raw.githubusercontent.com/snakers4/silero-vad/dbacf536adadf42210f37ae50fbaf75f6235b3cf/src/silero_vad/data/silero_vad.jit

curl --fail --location \
  --output silero-vad-work/assets/test.wav \
  https://raw.githubusercontent.com/snakers4/silero-vad/dbacf536adadf42210f37ae50fbaf75f6235b3cf/tests/data/test.wav
```

## 4. Create two audio clips

The target processes 2.5 seconds of audio. Copy this snippet once to create a calibration clip and a separate validation clip:

```bash
python3 - <<'PY'
import wave
from pathlib import Path

source_path = Path("silero-vad-work/assets/test.wav")
clips = (("calibration.wav", 0.0), ("validation.wav", 2.5))

with wave.open(str(source_path), "rb") as source:
    parameters = source.getparams()
    if (
        parameters.nchannels,
        parameters.sampwidth,
        parameters.framerate,
        parameters.comptype,
    ) != (1, 2, 16000, "NONE"):
        raise SystemExit("test.wav must be mono, 16 kHz, 16-bit PCM")
    if source.getnframes() < 5 * parameters.framerate:
        raise SystemExit("test.wav does not contain five seconds of audio")
    for name, start_seconds in clips:
        source.setpos(int(start_seconds * parameters.framerate))
        frames = source.readframes(int(2.5 * parameters.framerate))
        if len(frames) != 40000 * parameters.sampwidth:
            raise SystemExit(f"Could not create a 2.5-second {name} clip")
        with wave.open(str(source_path.with_name(name)), "wb") as target:
            target.setparams(parameters)
            target.writeframes(frames)
PY
```

Use `calibration.wav` to calibrate quantization. The FVP will process the separate `validation.wav` clip.

## What you've accomplished and what's next

You have installed the pinned ExecuTorch source, prepared the Arm tools, and created the model inputs.

Next, export the model as a quantized ExecuTorch program for Ethos-U85.

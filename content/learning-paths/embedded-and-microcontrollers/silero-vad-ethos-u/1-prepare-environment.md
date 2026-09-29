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

Use ExecuTorch `v1.5.1` for the Python package, example, and native runtime. Clone the matching source:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 3b60683923245cf472b7323426920e15623ba361
git submodule sync --recursive
git submodule update --init --recursive
```

Confirm the checked-out revision:

```bash
git rev-parse --short=12 HEAD
```

The expected output is:

```output
3b6068392324
```

Create and activate a Python virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## Install the Arm backend tools

The Arm setup script downloads the Arm GNU Toolchain, Ethos-U Vela compiler, and supporting Python packages. On Linux, the script also installs the Corstone FVPs. Review the license terms presented by the script before using its EULA acceptance option.

{{% notice macOS %}}
Before you run the Arm setup command on macOS, install [Docker Desktop](/install-guides/docker/docker-desktop/) and follow the [AVH FVPs on macOS install guide](/install-guides/fvps-on-macos/). Add the FVPs-on-Mac `bin` directory to `PATH`. Confirm that Docker is running and that `FVP_Corstone_SSE-320` resolves to the wrapper:

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

The second command adds the downloaded cross-compiler and, on Linux, FVP binaries to the current shell environment. If you start a new shell, you'll need to run the command again.

Check that the two target tools are available:

```bash
command -v arm-none-eabi-g++
command -v FVP_Corstone_SSE-320
```

The compiler resolves under `examples/arm/arm-scratch/`. On Linux, the FVP also resolves under this directory. On macOS, the FVP resolves under the FVPs-on-Mac wrapper directory. If the compiler is missing, source `examples/arm/arm-scratch/setup_path.sh` again. If the FVP is missing on macOS, add the wrapper directory to `PATH`.

## Install ExecuTorch

Remove the unused model-viewing and test packages installed by Arm setup:

```bash
python -m pip uninstall --yes \
  tosa-adapter-model-explorer ai-edge-model-explorer \
  pytest-timeout pte-adapter-model-explorer
```

Install the released packages for your host. Linux uses CPU wheels; macOS uses Apple silicon wheels. Keep this step after Arm setup to resolve its older FlatBuffers dependency:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash" >}}
python -m pip install \
  --index-url https://pypi.org/simple \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  "executorch[ethos-u]==1.5.1" \
  "torch==2.14.0+cpu" "torchvision==0.29.0+cpu" "torchao==0.18.0+cpu" \
  "cmake==3.31.10" "zstd==1.5.7.2"
  {{< /tab >}}
  {{< tab header="macOS" language="bash" >}}
python -m pip install \
  --index-url https://pypi.org/simple \
  "executorch[ethos-u]==1.5.1" \
  "torch==2.14.0" "torchvision==0.29.0" "torchao==0.18.0" \
  "cmake==3.31.10" "zstd==1.5.7.2"
  {{< /tab >}}
{{< /tabpane >}}

Check dependency consistency and the imports used by export and CMake code generation:

```bash
python -m pip check
python - <<'PY'
import executorch.codegen.tools.selective_build
from executorch.backends.arm.ethosu import EthosUPartitioner
from executorch.backends.arm.quantizer import EthosUQuantizer

print("ExecuTorch installation verified")
PY
```

The checks should report `No broken requirements found.` and `ExecuTorch installation verified`. These commands replace `install_executorch.sh`, which uses nightly and test indexes. If you rerun Arm setup, repeat this section before continuing.

## Download the model and sample audio

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

## Create two audio clips

The target processes 2.5 seconds of audio. Copy the following snippet once to create a calibration clip and a separate validation clip:

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

You've installed the pinned ExecuTorch source, prepared the Arm tools, and created the model inputs.

Next, you'll export the model as a quantized ExecuTorch program for Ethos-U85.

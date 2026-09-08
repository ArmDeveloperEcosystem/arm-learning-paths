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

## 1. Create an isolated ExecuTorch environment

The public development branch contains the Silero VAD Ethos-U example while maintainers upstream it. Use the tested commit so that the commands and generated artifacts match this Learning Path.

Clone the ExecuTorch fork and check out the tested revision:

```bash
git clone --branch codex/mletorch-2112-silero-vad-ethos-u \
  --single-branch https://github.com/usamahz/executorch.git
cd executorch
git checkout 4af907b2192d89369440a1dc0488c1792781a82d
```

Confirm the checked-out revision:

```bash
git rev-parse --short=12 HEAD
```

The expected output is:

```output
4af907b2192d
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install ExecuTorch and its Python dependencies:

```bash
./install_executorch.sh
```

The installation script initializes the Git submodules needed by the build and installs the matching PyTorch and ExecuTorch packages.

## 2. Install the Arm backend tools

The Arm setup script downloads the Arm GNU Toolchain, Ethos-U Vela compiler, Corstone FVPs, and supporting Python packages. Review the license terms presented by the script before using its EULA acceptance option.

Run the setup script from the ExecuTorch repository root:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```

The second command adds the downloaded cross-compiler and FVP binaries to the current shell environment. Run it again when you start a new shell.

Check that the two target tools are available:

```bash
command -v arm-none-eabi-g++
command -v FVP_Corstone_SSE-320
```

Each command prints an executable under `examples/arm/arm-scratch/`. If either command produces no path, source `examples/arm/arm-scratch/setup_path.sh` again.

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
    for name, start_seconds in clips:
        source.setpos(int(start_seconds * parameters.framerate))
        frames = source.readframes(int(2.5 * parameters.framerate))
        with wave.open(str(source_path.with_name(name)), "wb") as target:
            target.setparams(parameters)
            target.writeframes(frames)
PY
```

Use `calibration.wav` to calibrate quantization. The FVP will process the separate `validation.wav` clip.

## What you've accomplished and what's next

You have installed the pinned ExecuTorch source, prepared the Arm tools, and created the model inputs.

Next, export the model as a quantized ExecuTorch program for Ethos-U85.

---
title: Run a local speech translation pipeline
description: Build Compute Flow on your Mac and connect three Python bricks to translate an English recording into French speech.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare your Mac

You'll install three model packages, build Compute Flow for your Mac, and create a Python application.

First, check your  CPU architecture:

```bash
uname -m
```

You should see `arm64`.

If `uv` isn't installed, use the [uv standalone installer](https://docs.astral.sh/uv/getting-started/installation/) with the following command.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


Next, if Apple's developer tools aren't installed, follow [Apple's instructions for installing the Xcode Command Line Tools](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools/). The package includes Git, Clang, and the macOS SDK. If you already have Xcode or the Command Line Tools installed, use those tools.

Finish with a quick check that the tools are available:

```bash
uv --version
git --version
command -v cc
command -v c++
```

## Set up Compute Flow

{{% notice Note %}}
The public repository URL in this draft is a placeholder. Until it is available, use the Compute Flow checkout supplied through your project access. You also need access to its native dependency bundles. Run the remaining commands from that checkout's root directory.
{{% /notice %}}

When the public repository is available, obtain it with:

```bash
git clone https://github.com/ARM-software/compute-flow.git
cd compute-flow
```

Create and activate the Python environment, then check the required system dependencies:

```bash
uv sync && source .venv/bin/activate
compute-flow check
```

```output
╭───────────────────────────────────────── OK Environment Ready ─────────────────────────────────────────╮
│  All required system dependencies are available.                                                       │
│  ─────────────────────────────────────────── Dependencies ───────────────────────────────────────────  │
│                                                                                                        │
│    Dependency      Executable     Status     Path                                                      │
│   ──────────────────────────────────────────────────────────────────────────────────────────────────   │
│    Git             git            found      /Library/Developer/CommandLineTools/usr/bin/git           │
│                                                                                                        │
│  ───────────────────────────────────────── Native Toolchain ─────────────────────────────────────────  │
│                                                                                                        │
│    Compiler       Toolchain     Version   Status   Path                                                │
│   ──────────────────────────────────────────────────────────────────────────────────────────────────   │
│    C compiler     Clang (cc)    21.0.0    found    /Library/Developer/CommandLineTools/usr/bin/cc      │
│    C++ compiler   Clang (c++)   21.0.0    found    /Library/Developer/CommandLineTools/usr/bin/c++     │
│                                                                                                        │
│  ────────────────────────────────────────────── Tools ───────────────────────────────────────────────  │
│                                                                                                        │
│    Name              Version   Provided by       Status            Path                                │
│   ──────────────────────────────────────────────────────────────────────────────────────────────────   │
│    CMake             4.0.2     Brick Manager     will be           -                                   │
│                                                  downloaded when                                       │
│                                                  needed                                                │
│    Git LFS           3.6.1     Brick Manager     will be           -                                   │
│                                                  downloaded when                                       │
│                                                  needed                                                │
│                                                                                                        │
│  ──────────────────────────────────────────── Toolchains ────────────────────────────────────────────  │
│                                                                                                        │
│    Name              Version     Provided by       Status            Path                              │
│   ──────────────────────────────────────────────────────────────────────────────────────────────────   │
│    Android™ NDK      r27c        Brick Manager     will be           -                                 │
│                                                    downloaded when                                     │
│                                                    needed                                              │
│    Linux® Arm®       14.2.rel1   Brick Manager     will be           -                                 │
│    64-bit                                          downloaded when                                     │
│    toolchain                                       needed                                              │
│                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

Compute Flow requires Python 3.11 or later. `uv sync` installs the project's Python dependencies into the virtual environment. With its default settings, [uv also downloads a compatible Python interpreter](https://docs.astral.sh/uv/concepts/python-versions/) if it can't find one locally.

`compute-flow check` reports missing system dependencies and suggests installation commands. It doesn't install them or test whether the compiler can compile and link a program. If it reports a missing native compiler or Git installation, follow the suggested action and run the check again.

Brick Manager automatically downloads managed tools, such as CMake and Git LFS, when a command needs them. The check reports these as `will be downloaded when needed`; you don't need to install them manually. For example, `compute-flow build native` downloads its managed CMake version if it isn't already available.


## Install the three model packages

Update Brick Manager's registry cache and install the models used by your pipeline:

{{% notice Tip %}}
For higher rate limits and faster downloads from Hugging Face, set the optional `HF_TOKEN` environment variable to your Hugging Face access token before installing the models. You can [create a Hugging Face access token](https://huggingface.co/settings/tokens) in account settings.
{{% /notice %}}

```bash
compute-flow update
compute-flow model install stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic
compute-flow model install lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation
compute-flow model install tts:qwen3-tts qwen3-tts-0-6b-custom-voice
```

Each `model install` command installs the brick source, if needed, and its model package. The identifiers select these implementations:

| Brick | Model package | Pipeline role |
| --- | --- | --- |
| `stt:parakeet-tdt` | Parakeet TDT 0.6B v3, dynamic INT8 | Recognize the English recording |
| `lm_text:lm-text-generic` | Hy-MT2 1.8B, 2-bit | Translate the transcription into French |
| `tts:qwen3-tts` | Qwen3-TTS 0.6B Custom Voice | Generate French speech |

Models are downloaded to the `~/.compute-flow` directory by default.

```bash
compute-flow model info stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic
compute-flow model info lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation
compute-flow model info tts:qwen3-tts qwen3-tts-0-6b-custom-voice
```

## Build for your Mac

Build the installed bricks and the native Python bindings:

```bash
compute-flow build native
```

If successful, you should see output similar to the following. 

```output
╭────────────────────────────── OK Build Complete ──────────────────────────────╮
│  Build directory  /Users/kiehej01/compute_flow/compute_flow/build_native      │
│  Application SDK  /Users/kiehej01/compute_flow/compute_flow/build_native/sdk  │
╰───────────────────────────────────────────────────────────────────────────────╯
```

{{% notice Troubleshooting Tip %}}

Compute Flow uses prebuilt, optimized dependency binaries where available. Some dependencies, such as llama.cpp, are first checked on your local machine. A preinstalled version may be incompatible with Compute Flow and cause build errors.

In the first instance, **either update the dependency causing the error to a compatible version or uninstall the local version** to allow Compute Flow to build just the missing depencencies from source.

As a fallback, you can build the supported runtime dependencies from their pinned source revisions with the following command, although this will take up to 1 hour so we strongly recommend attempting the steps above before building from source:

```bash
compute-flow build native --from-source
```

{{% /notice %}}

The build downloads optimized macOS Arm64 runtimes such as LiteRT, ExecuTorch, and ONNX Runtime with support for KleidiAI, packages them with your installed brick implementations in an application SDK for C++ applications, and installs Python bindings so you can use the same native functionality from Python.

```output
├── CMakeLists.txt
├── force_load_libraries.txt
├── include
│   └── compute_flow
│       ├── accelerator.h
│       ├── bindings
│       ├── bricks
│       ├── check.h
│       ├── compute_flow.h
│       ├── lm_params.h
│       ├── lm_runners
│       ├── manifest.h
│       ├── memory_planner.h
│       ├── model_data.h
│       ├── profiler
│       ├── runners
│       ├── runtime.h
│       └── tensor_dict.h
├── lib
│   ├── libcompute_flow_brick_factory.a
│   ├── libcompute_flow_core.a
│   ├── libcompute_flow.a
│   ├── libexecutorch.a
│   ├── liblm_text_core.a
│   ├── liboptimized_native_cpu_ops_lib.a
│   ├── libstt_core.a
│   ├── libtts_core.a
│   └── libxnnpack_backend.a
├── README.md
└── share
    └── compute_flow
        └── bricks
```

The second command confirms that your active environment can load the native module. If the import fails, check that the build completed successfully and that the same virtual environment is active. A dependency download error needs to be resolved before the bindings can be built.

## Create the Python application

Create a directory for your application:

```bash
mkdir -p audio_translation_example
```

Save the following code as `audio_translation_example/audio_translation.py`. It loads each manifest, configures the languages, and connects the three bricks. The sample-rate check prevents passing incompatible audio to the speech recognition model.

```python
# SPDX-FileCopyrightText: Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
# SPDX-License-Identifier: Apache-2.0

"""Translate an English recording with three local Compute Flow bricks."""

import argparse
from pathlib import Path

import compute_flow_py as cf
import numpy as np
import soundfile as sf


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stt-manifest", required=True)
    parser.add_argument("--translation-manifest", required=True)
    parser.add_argument("--tts-manifest", required=True)
    parser.add_argument("--input", required=True, dest="input_audio")
    parser.add_argument("--source-language", required=True)
    parser.add_argument("--destination-language", required=True)
    parser.add_argument("--output", default="translated_french.wav")
    args = parser.parse_args()

    # Both speech recognition variants in this tutorial expect 16 kHz audio.
    audio, input_rate = sf.read(args.input_audio, dtype="float32", always_2d=True)
    if input_rate != 16000 or audio.shape[0] == 0:
        raise ValueError("Use a nonempty 16 kHz recording, such as beckett.wav")
    mono = np.mean(audio, axis=1, dtype=np.float32)
    raw_wav = np.ascontiguousarray(mono.reshape(1, -1), dtype=np.float32)
    sample_rate = np.asarray([input_rate], dtype=np.int64)

    stt_manifest = cf.load_manifest(args.stt_manifest)
    translation_manifest = cf.load_manifest(args.translation_manifest)
    tts_manifest = cf.load_manifest(args.tts_manifest)
    translation_manifest.set_config("src_lang", args.source_language)
    translation_manifest.set_config("dst_lang", args.destination_language)
    tts_manifest.set_config("language", args.destination_language.lower())

    options = cf.BrickOptions()
    options.runtime.enable_warmup = True
    stt = cf.load_brick(stt_manifest)
    translation = cf.load_brick(translation_manifest)
    tts = cf.load_brick(tts_manifest)
    stt.setup(stt_manifest, options)
    translation.setup(translation_manifest, options)
    tts.setup(tts_manifest, options)

    # Keep the waveform and sample-rate tensors alive throughout recognition.
    stt.reset_states()
    stt_input = {"raw_wav": raw_wav, "sample_rate": sample_rate}
    transcription_chunks = []
    while not stt.is_generation_complete():
        result = stt.run(stt_input)
        transcription_chunks.append(str(np.asarray(result["text"]).item()))
    transcription = "".join(transcription_chunks)
    if not transcription.strip():
        raise RuntimeError("Speech recognition returned no text")
    print(f"Transcription: {transcription}", flush=True)

    # Pass the complete transcription to the translation brick.
    translation.reset_states()
    translation_input = {"text_prompt": transcription}
    translation_chunks = []
    while not translation.is_generation_complete():
        result = translation.run(translation_input)
        translation_chunks.append(str(np.asarray(result["text"]).item()))
    translated_text = "".join(translation_chunks)
    if not translated_text.strip():
        raise RuntimeError("Translation returned no text")
    print(f"Translation: {translated_text}", flush=True)

    # Copy each audio chunk before the brick reuses its output buffers.
    tts.reset_states()
    tts_input = {"text_prompt": translated_text}
    audio_chunks = []
    output_rate = 0
    while not tts.is_generation_complete():
        result = tts.run(tts_input)
        left = np.asarray(result["left_channel"], dtype=np.float32).reshape(-1)
        right = np.asarray(result["right_channel"], dtype=np.float32).reshape(-1)
        output_rate = int(np.asarray(result["sample_rate"]).reshape(-1)[0])
        if left.size:
            audio_chunks.append(np.column_stack((left, right)))

    stt.reset_states()
    translation.reset_states()
    tts.reset_states()
    if not audio_chunks or output_rate <= 0:
        raise RuntimeError("Speech synthesis returned no audio")
    output_audio = np.concatenate(audio_chunks, axis=0)
    sf.write(args.output, output_audio, output_rate, subtype="FLOAT")
    print(f"Saved: {Path(args.output).resolve()}")


if __name__ == "__main__":
    main()
```

The input waveform has shape `(1, number_of_samples)` and uses `float32`; its sample rate uses `int64`. Each input dictionary remains alive until its generation loop completes. `np.column_stack()` copies the left and right audio channels into a stereo chunk before another call can reuse the brick's buffers.

`load_manifest()` reads the model configuration, `load_brick()` selects the implementation, and `setup()` prepares it for inference. Warmup happens during setup, so the first printed transcription can take time to appear. Each `run()` call returns the next output from a brick; the loop continues until `is_generation_complete()` returns `True`. `reset_states()` clears the request state while retaining the loaded models.

All three bricks share these execution methods, documented in [Brick Runtime Interface V1](https://github.com/ARM-software/ComputeFlow/blob/main/docs/design/brick_runtime_interface_v1.md).

The Qwen3-TTS manifest filename includes `en`, but the script sets its `language` configuration to `french` before setup. The selected Custom Voice model supports French synthesis. The translation configuration similarly sets English as the source language and French as the destination.

## Translate the packaged recording

Resolve the package locations through Brick Manager instead of hard-coding cache paths. Then run your application using the sample supplied with Parakeet:

```bash
PARAKEET_PACKAGE="$(compute-flow model path stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic)"
HY_MT2_PACKAGE="$(compute-flow model path lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation)"
QWEN3_TTS_PACKAGE="$(compute-flow model path tts:qwen3-tts qwen3-tts-0-6b-custom-voice)"

python audio_translation_example/audio_translation.py \
  --stt-manifest "$PARAKEET_PACKAGE/parakeet_tdt_0_6b_v3_manifest.json" \
  --translation-manifest "$HY_MT2_PACKAGE/hy_mt2_1_8b_manifest.json" \
  --tts-manifest "$QWEN3_TTS_PACKAGE/qwen3_tts_custom_voice_en_manifest.json" \
  --input "$PARAKEET_PACKAGE/samples/beckett.wav" \
  --source-language English \
  --destination-language French \
  --output translated_french.wav
```

The application prints `Transcription:`, `Translation:`, and `Saved:` lines alongside the runtime logs. The output from one run is shown here, with the checkout path shortened:

```output
Transcription: Ever tried, ever failed. No matter. Try again. Fail again. Fail better.
Translation: Avez-vous déjà essayé, avez-vous déjà échoué. Peu importe. Essayez à nouveau. Écheclez encore. Échouez mieux.
Saved: <checkout>/translated_french.wav
```

Check that the transcription matches the English recording and that the translation preserves its meaning. Generated wording and punctuation can vary and can contain errors: this run produced the incorrect word "Écheclez". Completing the pipeline verifies the integration; review the generated text and speech separately for translation quality.


## What you've accomplished

You've installed three model packages, built Compute Flow, and connected their brick interfaces in a Python application. Your application now turns an English recording into a local French WAV file. Next, you'll replace the speech recognition model and run the same application again.

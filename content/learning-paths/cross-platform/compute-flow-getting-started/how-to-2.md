---
title: Run a local speech translation pipeline
description: Build Compute Flow on your Mac and connect three Compute Flow bricks to translate an English recording into French speech.
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

Finally, remove any previously installed `llama.cpp` versions. For example if installed with the `brew` package manager, run the following command:

```bash
brew uninstall llama.cpp
```

## Set up Compute Flow

Run the following command.

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
| `stt:parakeet-tdt` | Parakeet TDT 0.6B v3, dynamic INT8 | Transcribe the English recording |
| `lm_text:lm-text-generic` | Hy-MT2 1.8B, 2-bit | Translate English text into French |
| `tts:qwen3-tts` | Qwen3-TTS 0.6B Custom Voice | Synthesize French speech |

Models are downloaded to the `~/.compute-flow` directory by default.The `compute-flow model info` command displays details about a specified model

```bash
compute-flow model info stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic
compute-flow model info lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation
compute-flow model info tts:qwen3-tts qwen3-tts-0-6b-custom-voice
```

## Build for your Mac

Build the installed bricks:

```bash
compute-flow build native
```

If successful, you should see output similar to the following. 

```output
╭────────────────────────────── OK Build Complete ──────────────────────────────╮
│  Build directory  /Users/user/compute_flow/compute_flow/build_native      │
│  Application SDK  /Users/user/compute_flow/compute_flow/build_native/sdk  │
╰───────────────────────────────────────────────────────────────────────────────╯
```

The build command downloads inference runtimes optimized for your deployment platform and packages them with your installed brick implementations into an application SDK available at `build_native/sdk`. 

## Create the Python application

Create a directory for your application:

```bash
mkdir -p audio_translation_example
```

Save the following code as `audio_translation_example/audio_translation.py`. The below code provides everything you need to run the audio-to-audio translation pipeline. You will see that the code first load and configure each of the three bricks required for our application, then execute each brick, with the output from the previous brick being pass to the next one, and finally, save the output of our pipeline.

```python
"""Translate speech between languages with three Compute Flow bricks."""

from __future__ import annotations

import argparse
from pathlib import Path

import compute_flow_py as cf
import numpy as np
import soundfile as sf


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stt-manifest", required=True)
    parser.add_argument("--translation-manifest", required=True)
    parser.add_argument("--tts-manifest", required=True)
    parser.add_argument("--input", required=True, dest="input_audio")
    parser.add_argument("--source-language", required=True)
    parser.add_argument("--destination-language", required=True)
    parser.add_argument(
        "--output", default="translated_french.wav", dest="output_audio"
    )
    args = parser.parse_args(argv)

    # Load the input as a batch containing one mono float32 waveform.
    input_audio, input_sample_rate = sf.read(
        args.input_audio, dtype="float32", always_2d=True
    )
    mono_audio = np.mean(input_audio, axis=1, dtype=np.float32)
    raw_wav = np.ascontiguousarray(mono_audio.reshape(1, -1), dtype=np.float32)
    sample_rate = np.asarray([input_sample_rate], dtype=np.int64)

    options = cf.BrickOptions()
    options.runtime.enable_warmup = True

    # Load the manifests.
    stt_manifest = cf.load_manifest(args.stt_manifest)
    translation_manifest = cf.load_manifest(args.translation_manifest)
    tts_manifest = cf.load_manifest(args.tts_manifest)

    # Configure the requested translation and text-to-speech languages.
    translation_manifest.set_config("src_lang", args.source_language)
    translation_manifest.set_config("dst_lang", args.destination_language)
    tts_manifest.set_config("language", args.destination_language.lower())

    # Load the bricks.
    stt_brick = cf.load_brick(stt_manifest)
    translation_brick = cf.load_brick(translation_manifest)
    tts_brick = cf.load_brick(tts_manifest)

    # Set up the bricks.
    stt_brick.setup(stt_manifest, options)
    translation_brick.setup(translation_manifest, options)
    tts_brick.setup(tts_manifest, options)

    #################################
    # Run speech-to-text brick
    #################################
    stt_brick.reset_states()

    stt_input = {"raw_wav": raw_wav, "sample_rate": sample_rate}
    transcription_chunks = []
    while not stt_brick.is_generation_complete():
        stt_output = stt_brick.run(stt_input)
        transcription_chunks.append(str(np.asarray(stt_output["text"]).item()))

    #################################
    # Run translation brick
    #################################
    translation_brick.reset_states()

    translation_input = {"text_prompt": "".join(transcription_chunks)}
    translation_chunks = []
    while not translation_brick.is_generation_complete():
        translation_output = translation_brick.run(translation_input)
        translation_text = np.asarray(translation_output["text"]).item()
        translation_chunks.append(str(translation_text))

    tts_input = {"text_prompt": "".join(translation_chunks)}
    left_chunks = []
    right_chunks = []
    output_sample_rate = 0

    #################################
    # Run text-to-speech brick
    #################################
    tts_brick.reset_states()

    while not tts_brick.is_generation_complete():
        tts_output = tts_brick.run(tts_input)
        left = np.asarray(tts_output["left_channel"], dtype=np.float32).reshape(-1)
        right = np.asarray(tts_output["right_channel"], dtype=np.float32).reshape(-1)
        sample_rate_tensor = np.asarray(tts_output["sample_rate"])
        output_sample_rate = int(sample_rate_tensor.reshape(-1)[0])

        if left.size:
            left_chunks.append(left.copy())
            right_chunks.append(right.copy())

    tts_brick.reset_states()

    if not left_chunks or output_sample_rate == 0:
        raise RuntimeError("Qwen3-TTS did not generate audio")

    left_audio = np.concatenate(left_chunks)
    right_audio = np.concatenate(right_chunks)
    output_audio = np.column_stack((left_audio, right_audio))

    sf.write(
        args.output_audio,
        output_audio,
        output_sample_rate,
        subtype="FLOAT",
    )

    print(f"Transcription: {''.join(transcription_chunks)}")
    print(f"Translation: {''.join(translation_chunks)}")
    print(f"Saved: {Path(args.output_audio).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

All three bricks share these execution methods, documented in [Brick Runtime Interface V1](https://github.com/ARM-software/ComputeFlow/blob/main/docs/design/brick_runtime_interface_v1.md).


## Translate a pre-recorded sample

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

The expected output is:

```output
Transcription: Ever tried, ever failed. No matter. Try again. Fail again. Fail better.
Translation: Avez-vous déjà essayé, avez-vous déjà échoué. Peu importe. Essayez à nouveau. Écheclez encore. Échouez mieux.
```

Check that the transcription matches the English recording and that the translation preserves its meaning. An accurate translation is, ""Déjà essayé, déjà échoué. Peu importe. Essaie encore. Échoue encore. Échoue mieux.". We will later demonstrate how to select alternative models with different performance and accuracy tradeoffs. 


## What you've accomplished

You've installed three Compute Flow brick types, using three of their model variants to build and audio-to-audio pipeline. Your application now turns an English recording into a local French WAV file. Next, you'll replace the speech recognition model and run the same application again.

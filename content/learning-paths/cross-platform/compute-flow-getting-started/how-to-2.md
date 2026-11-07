---
title: Run a local speech translation pipeline
description: Build Compute Flow on your device and connect three Compute Flow bricks to translate an English recording into French speech.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare your host device

You'll install three model packages, build Compute Flow for your device, and create an application. 

First, check the CPU architecture of your device:

```bash
uname -m
```

The expected output is `arm64` or `aarch64`.

If `uv` isn't installed, use the [uv standalone installer](https://docs.astral.sh/uv/getting-started/installation/) with the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Next, [install Xcode Command Line Tools](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools/) if you're compiling natively for MacOS on Apple® silicon. The package includes Git, Clang, and the macOS SDK. If you already have Xcode or the Command Line Tools installed, use those tools.

Check that the tools are available:

```bash
uv --version
git --version
command -v cc
command -v c++
```

If you're targeting an Android device with cross compilation, [install the Android Platform Tools](https://developer.android.com/tools/releases/platform-tools) with the `adb` utility. 

Finally, remove any previously installed `llama.cpp` versions. 

For example, if `llama.cpp` was previously installed using `brew` package manager, run the following command:

```bash
brew uninstall llama.cpp
```

## Set up Compute Flow

Clone the Compute Flow repository:

```bash
git clone https://github.com/ARM-software/compute-flow.git
cd compute-flow
```

Create and activate the Python environment, then check the required system dependencies:

```bash
uv sync && source .venv/bin/activate
compute-flow check
```

The environment check reports the available dependencies and native toolchain:

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

Compute Flow requires Python 3.11 or later. `uv sync` installs the project Python dependencies into the virtual environment. With its default settings, [uv also downloads a compatible Python interpreter](https://docs.astral.sh/uv/concepts/python-versions/) if it can't find one locally.

`compute-flow check` reports missing system dependencies and suggests installation commands. It doesn't install dependencies or test whether the compiler can compile and link a program. If it reports a missing native compiler or Git installation, follow the suggested action and run the check again.

Brick Manager automatically downloads managed tools, such as CMake and Git Large File Storage (LFS), when a command needs them. The check reports these as `will be downloaded when needed`, so you don't need to install them manually. For example, `compute-flow build native` downloads its managed CMake version if it isn't already available.

## Install the three model packages

Update the Brick Manager registry cache and install the models that will be used by your pipeline:

{{% notice Note %}}
For faster Hugging Face downloads and higher rate limits, set the optional `HF_TOKEN` environment variable before installing the models. You can [create a Hugging Face access token](https://huggingface.co/settings/tokens) in account settings.
{{% /notice %}}

```bash
compute-flow update
compute-flow model install stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic
compute-flow model install lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation
compute-flow model install tts:qwen3-tts qwen3-tts-0-6b-custom-voice
```

Each `model install` command installs the brick source, if needed, and its model package. 

The identifiers select the following implementations:

| Brick | Model package | Pipeline role |
| --- | --- | --- |
| `stt:parakeet-tdt` | Parakeet TDT 0.6B v3, dynamic INT8 | Transcribe the English recording |
| `lm_text:lm-text-generic` | Hy-MT2 1.8B, 2-bit | Translate English text into French |
| `tts:qwen3-tts` | Qwen3-TTS 0.6B Custom Voice | Synthesize French speech |

Models are downloaded to the `~/.compute-flow` directory by default. The `compute-flow model info` command displays details about a specified model:

```bash
compute-flow model info stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic
compute-flow model info lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation
compute-flow model info tts:qwen3-tts qwen3-tts-0-6b-custom-voice
```

## Build for your device

Build the installed bricks:

{{< tabpane-normal >}}
{{< tab header="Native Arm64" >}}
```bash
compute-flow build native
```
{{< /tab >}}
{{< tab header="Cross-compile for Android Arm64" >}}

```bash
compute-flow build android_arm64
```

Note that as of November 2026, the Android NDK doesn't support cross-compilation from Linux Arm64 hosts. Instead, use a macOS or Linux x86-64 host system.

{{< /tab >}}
{{< /tabpane-normal >}}

If successful, the output is similar to: 

```output
╭────────────────────────────── OK Build Complete ──────────────────────────────╮
│  Build directory  /Users/user/compute_flow/compute_flow/build_native      │
│  Application SDK  /Users/user/compute_flow/compute_flow/build_native/sdk  │
╰───────────────────────────────────────────────────────────────────────────────╯
```

The build command downloads inference runtimes that are optimized for your deployment platform. It packages them with your installed brick implementations into an application SDK available at `build_native/sdk`. 

## Create the application

Create a directory for your application:

```bash
mkdir -p audio_translation_example
```

Follow the instructions for your target device.

{{< tabpane-normal >}}
{{< tab header="Native Arm64" >}}

Save the following code as `audio_translation_example/audio_translation.py`:

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
{{< /tab >}}
{{< tab header="Cross-compile for Android Arm64" >}}

Save the following code as `audio_translation_example/audio_translation.cpp`:

```cpp
//Translate speech between languages with three Compute Flow bricks.

#include <getopt.h>

#include <algorithm>
#include <cctype>
#include <cstdint>
#include <cstdlib>
#include <exception>
#include <filesystem>
#include <iostream>
#include <string>
#include <vector>

#include "compute_flow/cli_examples/internal/wav.h"
#include "compute_flow/compute_flow.h"

namespace bricks = compute_flow::bricks;

namespace {

void print_usage(const char* name) {
    std::cout << "Usage: " << name
              << " --stt-manifest <path> --translation-manifest <path> --tts-manifest <path>\n"
                 "       --input <mono.wav> --source-language <language> --destination-language <language>\n"
                 "       [--output <path>] [--help]\n\n"
                 "Translate speech between languages with three Compute Flow bricks.\n"
                 "The output defaults to translated_french.wav.\n";
}

int32_t run(int32_t argc, char** argv) {
    std::string stt_manifest_path;
    std::string translation_manifest_path;
    std::string tts_manifest_path;
    std::string input_path;
    std::string source_language;
    std::string destination_language;
    std::string output_path     = "translated_french.wav";
    const option long_options[] = {
        {"stt-manifest", required_argument, nullptr, 's'},
        {"translation-manifest", required_argument, nullptr, 't'},
        {"tts-manifest", required_argument, nullptr, 'v'},
        {"input", required_argument, nullptr, 'i'},
        {"source-language", required_argument, nullptr, 'l'},
        {"destination-language", required_argument, nullptr, 'd'},
        {"output", required_argument, nullptr, 'o'},
        {"help", no_argument, nullptr, 'h'},
        {nullptr, 0, nullptr, 0},
    };
    int32_t option_value = 0;
    while ((option_value = getopt_long(argc, argv, "h", long_options, nullptr)) != -1) {
        switch (option_value) {
            case 's':
                stt_manifest_path = optarg;
                break;
            case 't':
                translation_manifest_path = optarg;
                break;
            case 'v':
                tts_manifest_path = optarg;
                break;
            case 'i':
                input_path = optarg;
                break;
            case 'l':
                source_language = optarg;
                break;
            case 'd':
                destination_language = optarg;
                break;
            case 'o':
                output_path = optarg;
                break;
            case 'h':
                print_usage(argv[0]);
                return EXIT_SUCCESS;
            default:
                print_usage(argv[0]);
                return EXIT_FAILURE;
        }
    }

    if (stt_manifest_path.empty() || translation_manifest_path.empty() || tts_manifest_path.empty() ||
        input_path.empty() || source_language.empty() || destination_language.empty() || output_path.empty() ||
        optind != argc) {
        std::cerr << "Error: provide all required arguments and no positional arguments.\n";
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }

    // Load the input as a batch containing one mono float32 waveform.
    std::vector<float> audio;
    int64_t input_sample_rate = bricks::internal::read_mono_wav(input_path, audio);

    COMPUTE_FLOW_CHECK(!audio.empty());

    bricks::BrickOptions options;
    options.runtime.enable_warmup = true;

    // Load the manifests and configure the requested languages before setup.
    auto stt_manifest         = bricks::load_manifest(stt_manifest_path);
    auto translation_manifest = bricks::load_manifest(translation_manifest_path);
    auto tts_manifest         = bricks::load_manifest(tts_manifest_path);
    std::string tts_language  = destination_language;

    std::transform(tts_language.begin(), tts_language.end(), tts_language.begin(),
                   [](unsigned char value) { return static_cast<char>(std::tolower(value)); });
    translation_manifest.set_config("src_lang", source_language);
    translation_manifest.set_config("dst_lang", destination_language);
    tts_manifest.set_config("language", tts_language);

    auto stt_brick         = bricks::load_brick(stt_manifest);
    auto translation_brick = bricks::load_brick(translation_manifest);
    auto tts_brick         = bricks::load_brick(tts_manifest);

    stt_brick->setup(stt_manifest, options);
    translation_brick->setup(translation_manifest, options);
    tts_brick->setup(tts_manifest, options);

    // Run speech-to-text, keeping the input buffers alive for every generation call.
    stt_brick->reset_states();

    compute_flow::TensorDict stt_input;

    stt_input.declare_tensor("raw_wav");
    stt_input.declare_tensor("sample_rate");

    stt_input["raw_wav"].data             = audio.data();
    stt_input["raw_wav"].format.dt        = compute_flow::DataType::F32;
    stt_input["raw_wav"].format.shape     = {1, static_cast<int64_t>(audio.size())};
    stt_input["sample_rate"].data         = &input_sample_rate;
    stt_input["sample_rate"].format.dt    = compute_flow::DataType::I64;
    stt_input["sample_rate"].format.shape = {1};
    std::string transcription;

    while (!stt_brick->is_generation_complete()) {
        const auto output       = stt_brick->run(stt_input);
        const auto& text        = output["text"];
        const int64_t num_bytes = text.format.get_nbytes();

        if (num_bytes > 0) {
            transcription.append(static_cast<const char*>(text.data), static_cast<uint64_t>(num_bytes));
        }
    }

    std::cout << "Transcription: " << transcription << std::endl;

    // Translate the complete transcription.
    translation_brick->reset_states();

    compute_flow::TensorDict translation_input;

    translation_input.declare_tensor("text_prompt");

    translation_input["text_prompt"].data         = transcription.data();
    translation_input["text_prompt"].format.dt    = compute_flow::DataType::String;
    translation_input["text_prompt"].format.shape = {static_cast<int64_t>(transcription.size())};
    std::string translation;

    while (!translation_brick->is_generation_complete()) {
        const auto output       = translation_brick->run(translation_input);
        const auto& text        = output["text"];
        const int64_t num_bytes = text.format.get_nbytes();

        if (num_bytes > 0) {
            translation.append(static_cast<const char*>(text.data), static_cast<uint64_t>(num_bytes));
        }
    }

    std::cout << "Translation: " << translation << std::endl;

    // Synthesize the translation, copying chunks before the brick reuses its buffers.
    tts_brick->reset_states();

    compute_flow::TensorDict tts_input;

    tts_input.declare_tensor("text_prompt");

    tts_input["text_prompt"].data         = translation.data();
    tts_input["text_prompt"].format.dt    = compute_flow::DataType::String;
    tts_input["text_prompt"].format.shape = {static_cast<int64_t>(translation.size())};
    std::vector<float> left_audio;
    std::vector<float> right_audio;
    int64_t output_sample_rate = 0;

    while (!tts_brick->is_generation_complete()) {
        const auto output         = tts_brick->run(tts_input);
        const int64_t num_samples = output["left_channel"].format.shape[0];
        output_sample_rate        = *static_cast<const int64_t*>(output["sample_rate"].data);

        COMPUTE_FLOW_CHECK(num_samples == output["right_channel"].format.shape[0]);

        if (num_samples > 0) {
            const auto* left  = static_cast<const float*>(output["left_channel"].data);
            const auto* right = static_cast<const float*>(output["right_channel"].data);

            left_audio.insert(left_audio.end(), left, left + num_samples);
            right_audio.insert(right_audio.end(), right, right + num_samples);
        }
    }

    tts_brick->reset_states();

    COMPUTE_FLOW_CHECK(!left_audio.empty() && output_sample_rate > 0);

    bricks::internal::write_stereo_wav(output_path, left_audio.data(), right_audio.data(),
                                       static_cast<int64_t>(left_audio.size()), output_sample_rate);

    std::cout << "Saved: " << std::filesystem::absolute(output_path).string() << std::endl;
    return EXIT_SUCCESS;
}

}  // namespace

int32_t main(int32_t argc, char** argv) {
    try {
        return run(argc, argv);
    } catch (const std::exception& error) {
        std::cerr << "Error: " << error.what() << std::endl;
        return EXIT_FAILURE;
    }
}
```

Then, create a `CMakeLists.txt` file in the same directory.

```cmake
cmake_minimum_required(VERSION 3.24)
project(audio_translation LANGUAGES CXX)

add_subdirectory("${COMPUTE_FLOW_SDK_DIR}" compute_flow_sdk)

add_executable(audio_translation audio_translation.cpp ../compute_flow/cli_examples/internal/wav.cpp)
target_include_directories(audio_translation PRIVATE ..)
target_link_libraries(audio_translation PRIVATE compute_flow::sdk)

target_link_options(
    audio_translation
    PRIVATE -fopenmp -static-openmp "LINKER:-z,max-page-size=16384" "LINKER:-z,common-page-size=16384"
)
```

{{< /tab >}}
{{< /tabpane-normal >}}

The code provides everything that you need to run the audio-to-audio translation pipeline. The code first loads and configures each of the three bricks required for the application. It then runs each brick, with the output from the previous brick being passed to the next one. Finally, it saves the pipeline output.

All three bricks share these deployment methods, documented in [Brick Runtime Interface V1](https://github.com/ARM-software/ComputeFlow/blob/main/docs/design/brick_runtime_interface_v1.md).


## Translate a pre-recorded sample

Resolve the package locations through Brick Manager instead of hard-coding cache paths. Then, run your application using the sample supplied with Parakeet.

{{< tabpane-normal >}}
{{< tab header="Native Arm64" >}}

Run the application: 

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
{{< /tab >}}
{{< tab header="Cross-compile for Android Arm64" >}}
Compile the application:
```bash
cmake -S audio_translation_example -B build_audio_translation_android \
  -DCOMPUTE_FLOW_SDK_DIR="$PWD/build_android_arm64/sdk" \
  -DCMAKE_TOOLCHAIN_FILE="$(sed -n 's/^CMAKE_TOOLCHAIN_FILE:[^=]*=//p' build_android_arm64/CMakeCache.txt)" \
  -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-28 -DCMAKE_BUILD_TYPE=Release
cmake --build build_audio_translation_android --parallel
```
Connect your Android device using `adb` and push the model files to the device:

```bash
adb shell mkdir -p /data/local/tmp/compute-flow/audio-translation/stt \
  /data/local/tmp/compute-flow/audio-translation/translation \
  /data/local/tmp/compute-flow/audio-translation/tts
adb push --sync "$(compute-flow model path stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic)"/. \
  /data/local/tmp/compute-flow/audio-translation/stt/
adb push --sync "$(compute-flow model path lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation)"/. \
  /data/local/tmp/compute-flow/audio-translation/translation/
adb push --sync "$(compute-flow model path tts:qwen3-tts qwen3-tts-0-6b-custom-voice)"/. \
  /data/local/tmp/compute-flow/audio-translation/tts/
```

Next, push the binary to the device:

```bash
adb push --sync build_audio_translation_android/audio_translation /data/local/tmp/compute-flow/audio-translation/
```
Finally, run the application and retrieve the French translation:

```bash
adb shell 'cd /data/local/tmp/compute-flow/audio-translation &&
  chmod +x audio_translation &&
  ./audio_translation \
    --stt-manifest stt/parakeet_tdt_0_6b_v3_manifest.json \
    --translation-manifest translation/hy_mt2_1_8b_manifest.json \
    --tts-manifest tts/qwen3_tts_custom_voice_en_manifest.json \
    --input stt/samples/beckett.wav \
    --source-language English --destination-language French \
    --output translated_french.wav'
adb pull /data/local/tmp/compute-flow/audio-translation/translated_french.wav audio_translation_example/
```

{{< /tab >}}
{{< /tabpane-normal >}}

The expected output is:

```output
Transcription: Ever tried, ever failed. No matter. Try again. Fail again. Fail better.
Translation: Avez-vous déjà essayé, avez-vous déjà échoué. Peu importe. Essayez à nouveau. Échouez encore. Échouez mieux.
```

Check that the transcription matches the English recording and that the translation preserves its meaning. 

An accurate translation in the polite form is as follows:

```text
Avez-vous déjà essayé, avez-vous déjà échoué. Peu importe. Essayez à nouveau. Échouez encore. Échouez mieux.
```

You'll later learn how to select alternative models with different performance and accuracy tradeoffs. 

## What you've accomplished and what's next

You've installed three Compute Flow brick types and used three of their model variants to build an audio-to-audio pipeline. Your application now turns an English recording into a local French `.wav` file. 

Next, you'll replace the speech recognition model and run the same application again.

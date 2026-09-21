---
title: Understand the Vision Chat Android application
description: Review how the application imports Qwen3-VL, prepares an image and prompt, runs llama.cpp, and displays generated text.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Vision Chat works

`MainActivity.java` connects the Android document pickers, selected image, prompt, model package, and result views. It moves model import and inference off the main Android user-interface thread so the screen remains responsive while files are copied or the model runs.

Vision Chat supports one model package ZIP. The archive contains two GGUF files
because llama.cpp separates the language model from the vision encoder and
projector:

- `Qwen__Qwen3-VL-2B-Instruct_llamacpp_optimized.gguf` contains the Q4_K_M language model
- `Qwen__Qwen3-VL-2B-Instruct_llamacpp_optimized_mmproj.gguf` contains the Q8_0 vision encoder and projector

The application needs both files to answer a prompt about an image. The
language-model file can generate text, but it can't process an image without
the matching `mmproj` file. A `model-package.json` manifest in the ZIP records
the model identifier, filenames, sizes, and SHA-256 hashes.

### How Vision Chat resolves and validates the model package

The `model_catalog.json` file contains one descriptor for the supported Qwen3-VL package. The descriptor records the following:

- Expected package, model, and projector filenames
- Context size
- Maximum image edge
- Output-token limit
- Thread count
- Sampling settings

The descriptor is:

```json
{
  "id": "qwen3-vl-2b-instruct-q4-k-m",
  "title": "Qwen3-VL 2B Instruct",
  "repository": "Arm/qwen3-vl-2b-instruct-q4-k-m-ggml-llama-cpp-vivo-x300",
  "packageFile": "Qwen__Qwen3-VL-2B-Instruct_llamacpp_optimized.zip",
  "modelFile": "Qwen__Qwen3-VL-2B-Instruct_llamacpp_optimized.gguf",
  "projectorFile": "Qwen__Qwen3-VL-2B-Instruct_llamacpp_optimized_mmproj.gguf",
  "contextSize": 4096,
  "maximumImageEdge": 1280,
  "maximumOutputTokens": 128,
  "threads": 4,
  "temperature": 0.7,
  "topK": 20,
  "topP": 0.8
}
```

`ModelPackageImporter.java` receives one URI from Android's document picker. It
checks the ZIP filename and rejects nested, compressed, duplicate, or unexpected
entries. During extraction it verifies each file's size and SHA-256 hash against
the manifest, then checks the `GGUF` magic bytes.

The importer writes the files to temporary application-private storage. It
activates the package only after extraction and validation complete, so an
interrupted import doesn't replace an existing package with a partial one.

This validation detects an incomplete or corrupted package. It isn't an
accuracy test or a signature proving who published the files. Use the package
created by the application's downloader.

### How Vision Chat prepares the image and prompt

`LlamaCppVisionRunner.java` keeps the loaded model available between prompts. It limits the longest image edge to 1280 pixels, preserves the image's aspect ratio, and reads the resized Android bitmap into an ARGB pixel array.

The runner passes the pixels and prompt to `NativeVisionBridge.generate()`. This Java Native Interface (JNI) call enters `app/src/main/cpp/vision_chat.cpp` on the application's inference worker thread.

The native code converts the ARGB pixels to the RGB byte layout used by `libmtmd`. It also applies the chat template embedded in the language-model GGUF. The template adds the role and generation markers expected by Qwen3-VL.

### How Vision Chat evaluates the image and generates text

The native runner performs the multimodal request in the following order:

1. Insert the image marker before the text prompt.
2. Use `mtmd_tokenize_from_parts()` to create text and image chunks.
3. Use `mtmd_helper_eval_chunks()` to encode the image and evaluate the prompt.
4. Sample one output token from the language model.
5. Feed the token back to llama.cpp and continue until the end token or 128-token limit.

`libmtmd` reads the vision configuration from the matching projector GGUF. The Java code doesn't reproduce the model's image normalization, patch size, or projector tensor details.

The sampler uses the values stored in `model_catalog.json`: top-k 20, top-p 0.8, and temperature 0.7. These values match the package's sampling defaults.

### How Vision Chat reports timing

The result card separates the run into measurements that describe different work:

| Measurement | Work included |
| --- | --- |
| Model load | Open both GGUF files and initialize the llama.cpp and `libmtmd` contexts |
| Image and prompt | Resize and encode the image, format and tokenize the prompt, and evaluate both inputs |
| Output | Count generated tokens before the end token |
| Tokens per second | Divide generated tokens by token-generation time |

Separating image evaluation from token generation makes results easier to compare between prompts on the same phone. These application measurements don't reproduce the text-only MMLU benchmark from the model card.

### How Vision Chat uses optimized Arm CPU kernels

Open `app/src/main/cpp/CMakeLists.txt`. The Android build sets the same Arm instruction target used for the published model evaluation and enables KleidiAI in ggml's CPU backend:

```cmake
set(GGML_SYSTEM_ARCH "ARM" CACHE STRING "" FORCE)
set(GGML_CPU_ARM_ARCH "armv8.6-a+dotprod+i8mm" CACHE STRING "" FORCE)
set(GGML_CPU_KLEIDIAI ON CACHE BOOL "" FORCE)
```

The compile-time target allows ggml to use Dot Product and Int8 Matrix Multiplication instructions. This APK therefore needs a phone that reports `asimddp` and `i8mm` CPU features.

KleidiAI builds its SME2, SME, I8MM, and Dot Product microkernels as separate
implementations in the same APK. When the model loads, llama.cpp reads the CPU
features reported by Android and selects the most capable compatible
implementation. On an SME2-enabled phone, the Q8_0 matrix multiplications in
the vision encoder and projector use KleidiAI SME2 kernels.

The Q4_K_M language model contains Q4_K and Q6_K matrices. These use llama.cpp's
optimized Arm repack kernels rather than the KleidiAI Q8_0 path. For this model,
SME2 primarily accelerates image encoding and projection; it doesn't replace
every kernel used during token generation.

The application sends llama.cpp's kernel-selection messages to Android's log.
After running the model, display the relevant messages:

```console
adb logcat -d -s VisionChatNative:I llama.cpp:I '*:S'
```

On an SME2-enabled phone, the output includes lines similar to:

```output
I VisionChatNative: CPU features: dotprod=1 i8mm=1 sme=1 sme2=1; KleidiAI Q8_0 preference=SME2
I llama.cpp: kleidiai: primary q8 kernel feature SME2
```

On a supported phone without SME2, the same messages may name `I8MM`.

## What you've learned

You can now trace the supported Qwen3-VL package from Android file import through image encoding, prompt evaluation, and token generation. You can also distinguish model-load, multimodal-evaluation, and decode measurements.

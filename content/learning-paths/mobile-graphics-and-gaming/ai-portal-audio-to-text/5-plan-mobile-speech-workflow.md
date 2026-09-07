---
title: (Optional) Use a model not currently supported by Whisper Journal
description: Register a compatible mobile speech recognition model or generate and validate support for a model that needs another adapter.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose an implementation route

Whisper Journal already supports the LiteRT and ExecuTorch models listed in the supported model table on [Run and compare registered speech recognition models](/learning-paths/mobile-graphics-and-gaming/ai-portal-audio-to-text/3-run-model/). You don't need to change the application to use those models.

You can try one of two hands-on routes to use a model that Whisper Journal doesn't currently support:

- Register the model directly when it matches a supplied adapter
- Use the coding-agent workflow to generate another adapter

Record the following information for the model and compare it with the two supplied adapters before changing code:

- Runtime and package files
- Callable methods
- Input and output tensors
- Audio sample rate, channels, framing, padding, and duration
- Feature extraction
- Tokenizer and vocabulary
- Prompt tokens, suppression rules, and stopping conditions
- Output decoding

| Model compatibility | Hands-on workflow |
| --- | --- |
| Matches a supplied adapter's methods, tensors, audio preprocessing, tokenizer, decoder profile, and required assets | Register another compatible model |
| Differs in any required contract element | Generate another adapter using a coding agent |

Sharing a runtime doesn't make speech model packages interchangeable. Two `.pte` programs can expose different methods, and two `.tflite` models can use different cache layouts, tokenizer files, or decoding rules.

### Register another compatible model

Reuse a supplied adapter when another model has the same complete execution contract as one of the supported packages.

Download and package the model using its repository ID:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
printf 'Arm model repository ID: '
read -r MODEL_ID
export MODEL_ID

export MODEL_PACKAGE="$(.hf-venv/bin/python download_model.py \
  --repo-id "$MODEL_ID" \
  --print-path)"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_ID = Read-Host "Arm model repository ID"

$MODEL_PACKAGE = .\.hf-venv\Scripts\python.exe download_model.py `
  --repo-id "$MODEL_ID" `
  --print-path
  {{< /tab >}}
{{< /tabpane >}}

If the repository contains more than one primary `.tflite` or `.pte` model file, rerun the downloader with `--filename` followed by the exact repository-relative model filename.

Add one descriptor to the list returned by `CompatibleModelRegistry.models()`. The following example registers a LiteRT package that uses the same complete decoder profile as Whisper Base:

```java
static List<WhisperModelDescriptor> models() {
    return List.of(
            new WhisperModelDescriptor(
                    "my-whisper-base-litert",
                    "My Whisper model · LiteRT",
                    AdapterRegistry.LITERT_ID,
                    "Arm/my-whisper-base-litert",
                    "my-whisper-base-litert.zip",
                    80,
                    51865,
                    LiteRtWhisperAdapter.CONFIG_WHISPER_BASE
            )
    );
}
```

Import `org.arm.learningpath.whisper.litert.LiteRtWhisperAdapter` in `CompatibleModelRegistry.java` when you use this LiteRT configuration constant.

The package filename must match the ZIP created by the downloader. Select the supplied adapter and configuration that match the complete model package, then rebuild and install the APK. Importing the package automatically activates its registered adapter.

Don't register a speech model based only on its file extension or family name. A different export can keep a similar repository name but change the following: 

- Callable methods
- Tensors
- Tokenizer
- Prompt tokens
- Decoder behavior

### Determine when the supplied adapter doesn't fit

Add a decoder profile inside the supplied LiteRT adapter when the model:

- Uses the same `encode` and `decode` signatures
- Uses the same tensor layout and feature input
- Uses the same tokenizer behavior and decoding algorithm
- Uses different documented dimensions or token IDs

Reference the new configuration ID from the model descriptor.

The profile must validate the following:

- Model signatures
- Tensor shapes and data types
- Mel-bin count
- Vocabulary size
- Cache layout
- Prompt tokens
- Suppression rules
- Stopping conditions

Don't change profile values to make an incompatible package load.

Use a separate adapter when the runtime or callable methods change, but the model still accepts one complete mono recording and returns a transcript through `TranscriptionResult`. For example, a model with another Android runtime can reuse the supplied recorder and transcript UI while implementing its own model loading, preprocessing, inference, tokenization, and decoding.

A separate adapter isn't enough when the workflow no longer fits those shared interfaces. Streaming needs persistent decoder state and audio scheduling. Language selection, translation, timestamps, or speaker diarization can need different controls and result types. Extend `SpeechToTextAdapter.java`, `TranscriptionResult.java`, `AudioRecorder.java`, and `MainActivity.java` before adding such a workflow.

Keep recording, model execution, and transcript presentation separate where possible. The supplied recording path produces 16 kHz mono audio, so another model can reuse it only when that's the documented input contract.

### Generate another adapter using a coding agent

Use this workflow when the model doesn't match every part of a supplied adapter's contract. A coding agent can inspect the model package and prepare a build-time adapter for its preprocessing, task, runtime, and model format.

{{% notice Note %}}
Use an advanced coding agent that supports long-context, multi-file editing, and terminal tools. The agent needs to be able to trace Java interfaces and reason about audio preprocessing, tensor, tokenizer, and decoder contracts. It needs to be able to update Gradle configuration and interpret build errors. Lightweight autocomplete or chat-only tools are unlikely to complete this workflow reliably.

Treat generated code as a starting point that needs developer review and device validation.
{{% /notice %}}

Run the platform-specific project and Android SDK checks from the cloned project directory:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
if [ ! -f "settings.gradle.kts" ] || [ ! -x "gradlew" ]; then
    printf 'Run this command from the cloned project directory.\n' >&2
    exit 1
fi
if [ -z "${ANDROID_HOME:-}" ] || \
   [ ! -d "$ANDROID_HOME/platforms/android-35" ] || \
   [ ! -d "$ANDROID_HOME/build-tools/34.0.0" ]; then
    printf 'Android SDK Platform 35 or Build-Tools 34.0.0 is unavailable.\n' >&2
    exit 1
fi
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
if (-not (Test-Path "settings.gradle.kts") -or
    -not (Test-Path "gradlew.bat")) {
    throw "Run this command from the cloned project directory."
}
if (-not $env:ANDROID_HOME -or
    -not (Test-Path "$env:ANDROID_HOME\platforms\android-35") -or
    -not (Test-Path "$env:ANDROID_HOME\build-tools\34.0.0")) {
    throw "Android SDK Platform 35 or Build-Tools 34.0.0 is unavailable."
}
  {{< /tab >}}
{{< /tabpane >}}

Verify the project root, Java, and connected phone:

```console
git rev-parse --show-toplevel
java -version
adb get-state
```

Check the `huggingface_hub` package with the Python executable for your operating system:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
.hf-venv/bin/python -c \
    'import huggingface_hub; print(huggingface_hub.__version__)'
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\.hf-venv\Scripts\python.exe -c `
    "import huggingface_hub; print(huggingface_hub.__version__)"
  {{< /tab >}}
{{< /tabpane >}}

The output includes the project root, Java version, `device`, and the installed `huggingface_hub` version. Resolve any error before continuing.

Also make sure:

- Your coding agent is installed, authenticated if needed, and allowed to read, edit, and run commands in the project workspace
- You have access to the model repository
- You have access to an approved account and access token if you're using a gated or private repository
- You know the model runtime, tensor contract, and audio preprocessing from authoritative model documentation
- You know the tokenizer and decoding behavior from authoritative model documentation
- You have enough disk space for the complete model package and representative recordings with trusted reference transcripts

Generated code might need review and iteration. Compatibility depends on the following factors:

- The model package
- The Android runtime library
- Native operators
- Device ABI
- Preprocessing information
- Available backend support

Set the repository ID and runtime specified by the model package:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
printf 'Arm model repository ID: '
read -r MODEL_ID
printf 'Model runtime: '
read -r MODEL_RUNTIME
export MODEL_ID MODEL_RUNTIME

export MODEL_FILE="$(.hf-venv/bin/python adapter-generation/download_model_package.py \
  --repo-id "$MODEL_ID" \
  --print-model-path)"
export MODEL_DIR="$(dirname "$MODEL_FILE")"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_ID = Read-Host "Arm model repository ID"
$MODEL_RUNTIME = Read-Host "Model runtime"

$MODEL_FILE = .\.hf-venv\Scripts\python.exe adapter-generation/download_model_package.py `
  --repo-id "$MODEL_ID" `
  --print-model-path
$MODEL_DIR = Split-Path -Parent "$MODEL_FILE"
  {{< /tab >}}
{{< /tabpane >}}

The download script retrieves the complete repository because the coding agent might need configuration, tokenizer files, preprocessing programs, or other package assets in addition to the primary model file.

The command stores the primary model binary in `MODEL_FILE` and the package directory in `MODEL_DIR`.

Inspect the package and create `model-summary.json`:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
.hf-venv/bin/python adapter-generation/inspect_model_package.py \
  --model-dir "$MODEL_DIR" \
  --model-id "$MODEL_ID" \
  --runtime "$MODEL_RUNTIME"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\.hf-venv\Scripts\python.exe adapter-generation/inspect_model_package.py `
  --model-dir "$MODEL_DIR" `
  --model-id "$MODEL_ID" `
  --runtime "$MODEL_RUNTIME"
  {{< /tab >}}
{{< /tabpane >}}

Give your coding agent the following files from the project:

- `model-summary.json`
- `adapter-generation/generate_mobile_adapter_prompt.txt`
- `SpeechToTextAdapter.java`, `WhisperModelDescriptor.java`, `TranscriptionResult.java`, and `ProgressListener.java`
- `AudioRecorder.java`, `ModelPackageImporter.java`, and `download_model.py`
- `AdapterRegistry.java`, `GeneratedAdapterRegistry.java`, and `app/generated-runtime-dependencies.gradle.kts`
- `ExecuTorchWhisperAdapter.java` and `LiteRtWhisperAdapter.java` as examples
- `WhisperFeatureExtractor.java` and both `WhisperTokenizer.java` implementations

The prompt tells the coding agent to preserve the supplied contracts when they fit. The agent can add a documented LiteRT profile or create a runtime-specific adapter. It can register the adapter and model in `GeneratedAdapterRegistry.java`, update package handling, and add a required runtime dependency to `app/generated-runtime-dependencies.gradle.kts`.

The agent should report that the application contracts need to be extended when the package needs any of the following:

- Streaming or multi-recording input
- Language, translation, timestamp, or diarization controls
- Multiple model files selected at run time
- Another result type

The agent shouldn't force the model into the supplied interface.

Review the generated source. The coding agent should run the included file check and report the exact command using the files it created. To run the check yourself, replace `YourGeneratedSpeechAdapter.java` with the generated class name:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
.hf-venv/bin/python adapter-generation/validate_generated_adapter.py \
  --adapter "app/src/main/java/org/arm/learningpath/whisper/YourGeneratedSpeechAdapter.java"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\.hf-venv\Scripts\python.exe adapter-generation/validate_generated_adapter.py `
  --adapter "app/src/main/java/org/arm/learningpath/whisper/YourGeneratedSpeechAdapter.java"
  {{< /tab >}}
{{< /tabpane >}}

Create the ZIP package after reviewing the generated downloader and importer changes:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export MODEL_PACKAGE="$(.hf-venv/bin/python download_model.py \
  --repo-id "$MODEL_ID" \
  --print-path)"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_PACKAGE = .\.hf-venv\Scripts\python.exe download_model.py `
  --repo-id "$MODEL_ID" `
  --print-path
  {{< /tab >}}
{{< /tabpane >}}

Rebuild the application after reviewing the generated files:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
./gradlew :app:assembleDebug :app:lintDebug
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:assembleDebug :app:lintDebug
  {{< /tab >}}
{{< /tabpane >}}

Install the application and copy the package with the commands used on every operating system:

```console
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb push "$MODEL_PACKAGE" /sdcard/Download/
```

Select the model added by the generated adapter and import the copied ZIP package. A successful build confirms that the source compiles. However, it doesn't prove that audio preprocessing, tensor values, tokenization, or decoding are correct. Record representative utterances on the target phone and compare the transcripts with trusted references for the model package. Repeat one test in airplane mode to confirm that transcription remains on-device.

## What you've accomplished

You've learned how you can extend Whisper Journal to use a speech recognition model that's not currently supported.

You can now register a compatible model with a supplied adapter or generate, build, and validate another adapter for a model with a different contract.

---
title: (Optional) Use a model not currently supported by Photo Insight
description: Register a compatible mobile image classification model or generate and validate support for a model that needs another adapter.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose an implementation route

Photo Insight already supports the LiteRT, ExecuTorch, and ExecuTorch CLIP models listed in the supported model table on [Import and run Arm AI Portal models](/learning-paths/mobile-graphics-and-gaming/ai-portal-mobile-image-classification/3-run-model/). You don't need to change the application to use those models.

You can try one of two hands-on routes to use a model that Photo Insight doesn't currently support:

- Register the model directly when it matches a supplied adapter
- Use the coding-agent workflow to generate another adapter

Compare the following attributes of the model with the three supplied adapters to decide what workflow to complete:

- Task
- Runtime
- Tensors
- Preprocessing
- Outputs
- Required assets

| Model compatibility | Hands-on workflow |
| --- | --- |
| Matches a supplied adapter's methods, tensors, preprocessing, labels or tokenizer, and required assets | Register another compatible model |
| Differs in any required contract element | Generate another adapter using a coding agent |

Sharing a runtime doesn't make model packages interchangeable. For example, a different ExecuTorch task can expose different methods, tensors, preprocessing, assets, and output decoding from either supplied ExecuTorch adapter.

### Register another compatible model

Reuse a supplied adapter when another model has the same task, input and output tensors, labels or tokenizer, and one of the adapter's existing preprocessing configurations.

Download the model using its repository ID:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
printf 'Arm model repository ID: '
read -r MODEL_ID
export MODEL_ID

export MODEL_FILE="$(.hf-venv/bin/python download_model.py \
  --repo-id "$MODEL_ID" \
  --print-path)"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_ID = Read-Host "Arm model repository ID"

$MODEL_FILE = .\.hf-venv\Scripts\python.exe download_model.py `
  --repo-id "$MODEL_ID" `
  --print-path
  {{< /tab >}}
{{< /tabpane >}}

If the repository contains more than one `.tflite` or `.pte` file, rerun the downloader with `--filename` followed by the exact model filename.

Add one descriptor to the list returned by `CompatibleModelRegistry.models()`. The following example registers a LiteRT ImageNet classifier that uses the same preprocessing as MobileNetV3 Small:

```java
static List<ModelDescriptor> models() {
    return List.of(
            new ModelDescriptor(
                    "my-litert-classifier",
                    "My LiteRT classifier",
                    LiteRtImageClassificationAdapter.ID,
                    "LiteRT",
                    "my-classifier.tflite",
                    LiteRtImageClassificationAdapter.PROFILE_IMAGENET_CROP_256
            )
    );
}
```

The filename must match the downloaded model file. Select the supplied adapter and configuration that match the model package, then rebuild and install the APK. Importing the model automatically activates its registered adapter and updates the model-specific controls.

### Generate another adapter using a coding agent

Use this workflow when the model doesn't match every part of a supplied adapter's contract. A coding agent can inspect the model package and prepare a build-time adapter for its preprocessing, task, runtime, and model format.

{{% notice Note %}}
Use an AI coding agent that supports long-context, multi-file editing, and terminal tools. The agent needs to be able to trace Java interfaces and reason about tensor and preprocessing contracts. It needs to be able to update Gradle configuration and interpret build errors. Lightweight autocomplete or chat-only tools are unlikely to complete this workflow reliably. 

Treat generated code as a starting point that you need to review and validate on the target device.
{{% /notice %}}

Run these checks from the cloned project directory:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
if [ ! -f "settings.gradle.kts" ] || [ ! -x "gradlew" ]; then
    printf 'Run this command from the cloned project directory.\n' >&2
elif [ -z "${ANDROID_HOME:-}" ] || \
     [ ! -d "$ANDROID_HOME/platforms/android-35" ] || \
     [ ! -d "$ANDROID_HOME/build-tools/35.0.0" ]; then
    printf 'Android SDK Platform 35 or Build-Tools 35.0.0 is unavailable.\n' >&2
else
    git rev-parse --show-toplevel
    java -version
    adb get-state
    .hf-venv/bin/python -c \
        'import huggingface_hub; print(huggingface_hub.__version__)'
fi
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
if (-not (Test-Path "settings.gradle.kts") -or
    -not (Test-Path "gradlew.bat")) {
    throw "Run this command from the cloned project directory."
}
if (-not $env:ANDROID_HOME -or
    -not (Test-Path "$env:ANDROID_HOME\platforms\android-35") -or
    -not (Test-Path "$env:ANDROID_HOME\build-tools\35.0.0")) {
    throw "Android SDK Platform 35 or Build-Tools 35.0.0 is unavailable."
}

git rev-parse --show-toplevel
java -version
adb get-state
.\.hf-venv\Scripts\python.exe -c `
    "import huggingface_hub; print(huggingface_hub.__version__)"
  {{< /tab >}}
{{< /tabpane >}}

The checks verify the project files, Java and Android SDK versions, and the connected phone, They also verify the Python virtual environment and `huggingface_hub` package.

The output includes the project root, Java version, `device`, and the installed `huggingface_hub` version. Resolve any error before continuing.

Also make sure:

- Your coding agent is installed, authenticated if needed, and allowed to read, edit, and run commands in the project workspace
- You have access to the model repository
- You have access to an approved account and access token if you're using a gated or private repository
- You know the model runtime, tensor contract, and preprocessing from authoritative model documentation 
- You know the output decoding and required assets from authoritative model documentation
- You have enough disk space for the complete model package and a representative input with a known reference output

Generated code might need review and iteration. Compatibility depends on the following factors: 

- Model package
- Android runtime library
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

The download script retrieves the complete repository because the agent might need configuration, labels, tokenizer files, or other assets in addition to the primary model file.

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
- `VisionAdapter.java`, `AdapterDefinition.java`, and `AdapterInput.java`
- `ModelRunner.java` and `ModelDescriptor.java`
- `GeneratedAdapterRegistry.java` and `app/generated-runtime-dependencies.gradle.kts`
- `LiteRtImageClassificationAdapter.java`, `ExecuTorchImageClassificationAdapter.java`, and `ExecuTorchClipAdapter.java` as examples

The prompt tells the agent to keep the supplied adapters unchanged. The agent can create a model-specific adapter and layout and register them in `GeneratedAdapterRegistry.java`. It can add a required runtime dependency to `app/generated-runtime-dependencies.gradle.kts`.

Review every generated source and build-file change. Ask the coding agent to run `adapter-generation/validate_generated_adapter.py` with the exact adapter and layout paths it created, then review the command and its output. The layout argument isn't needed when the adapter doesn't add a layout.

Rebuild the application, install it on the connected phone, and copy the model:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
./gradlew :app:assembleDebug :app:lintDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb push "$MODEL_FILE" /sdcard/Download/
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:assembleDebug :app:lintDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb push "$MODEL_FILE" /sdcard/Download/
  {{< /tab >}}
{{< /tabpane >}}

Open the mode added by the generated adapter and import the copied model. A successful build confirms that the source compiles. However, it doesn't prove that preprocessing, tensor values, labels, tokenization, or output decoding are correct. Test representative inputs on the target phone and compare the results with a known reference for the model package.

## What you've accomplished

You've learned how to extend Photo Insight to use models not currently supported by the application.

You can now register a compatible model with a supplied adapter or generate, build, and validate another adapter for a model with a different contract.

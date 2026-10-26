---
title: (Optional) Use an image-generation model not currently supported by TinySD Studio
description: Register a compatible mobile image-generation model or generate and validate support for a model that needs another adapter.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose an implementation route

TinySD Studio already supports the model listed in the supported model table on [Run and compare TinySD image generation results](/learning-paths/mobile-graphics-and-gaming/ai-portal-tinysd-android/3-run-model/). You don't need to change the application to use that package.

You can try one of two hands-on routes to use a model that TinySD Studio doesn't currently support:

- Register the model directly when it matches the supplied adapter
- Use the coding-agent workflow to generate another adapter

Record the following information for the model and compare it with the supplied adapter before changing code:

- Runtime and package files
- Callable methods
- Input and output tensors
- Tokenizer and text-encoder requirements
- Latent shape, denoising schedule, and guidance calculation
- Image dimensions, channel layout, value range, and decoding
- Memory requirement and required user controls

| Model compatibility | Hands-on workflow |
| --- | --- |
| Matches the supplied adapter's methods, tensors, tokenizer, scheduler, denoising behavior, output decoding, and required assets | Register another compatible model |
| Differs in any required contract element | Generate another adapter using a coding agent |

Sharing a runtime doesn't make image-generation packages interchangeable. Two `.pte` programs can expose different methods, tensor layouts, tokenizers, denoising schedules, operators, or output decoders.

### Register another compatible model

You can reuse the supplied adapter when another model package has the same complete execution contract as the supported package. TinySD Studio currently activates one model descriptor, so this route replaces that descriptor rather than adding a model selector.

The supplied downloader expects the same three repository-relative files as the registered package. If the compatible repository uses different source filenames, update the source paths in `ARTIFACTS` while preserving the archive entry names required by `ModelImporter`.

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

Replace the descriptor in `CompatibleModelRegistry.models()`. The following example keeps the complete supplied adapter contract:

```java
private static final List<ModelDescriptor> MODELS = Collections.singletonList(
        new ModelDescriptor(
                "my-compatible-tinysd",
                "My compatible TinySD",
                TinySdImageGenerationAdapter.ADAPTER_ID,
                "tinysd_vivo_executorch.zip",
                "my-compatible-tinysd",
                "512 × 512",
                "ExecuTorch + XNNPACK",
                7L * 1024 * 1024 * 1024,
                Arrays.asList("optimized.pte", "schedule_data.json", "tokenizer.json")
        )
);
```

The package filename must match the ZIP created by `download_model.py`. Keep the adapter ID and required imported filenames unchanged. Use the supplied adapter only when it matches the complete model package, then rebuild and install the APK. Importing the package automatically activates the adapter referenced by the descriptor.

Don't register a model based only on its `.pte` extension, family name, or output dimensions. A different export can change callable methods, tensor shapes, tokenizer data, schedule values, operators, or output behavior while keeping a similar repository name.

### Determine when the supplied adapter doesn't fit

Keep the supplied adapter when only the repository metadata or source filenames change and the complete runtime execution contract remains identical. For example, `download_model.py` can package a renamed repository file under the same canonical ZIP entry.

Use the model package as the source of truth. A model can load and execute while producing poor or corrupted images because any of the following are wrong:

- Tokenization
- Tensor shapes or data types
- Denoising schedule
- Guidance calculation
- Latent scaling
- Image decoding

Use a separate adapter when the package still accepts one text prompt and seed, and returns one bitmap through `ImageGenerationAdapter.GenerationResult`, but there are differences in execution. Differences can include changes in any of the following: 

- Runtime
- Callable methods
- Tokenizer
- Tensor layout
- Denoising algorithm
- Guidance behavior
- Image decoder

The new adapter can reuse the supplied activity and document-picker workflows while owning its model-specific import and inference code.

A separate adapter isn't enough when the workflow no longer fits the shared interface. Image-to-image generation needs an input image. Negative prompts, adjustable step counts, guidance controls, multiple output images, or safety results need new inputs or result types. Extend `ImageGenerationAdapter.java`, `GenerationResult`, `ModelDescriptor.java`, the layout, and `MainActivity.java` before adding such a workflow.

Keep model execution and image presentation separate where possible. The current interface can be reused only when a model accepts the documented prompt and seed inputs, and produces a complete Android bitmap without additional interaction.

### Generate another adapter using a coding agent

Use this workflow when the model doesn't match every part of the supplied adapter's contract. A coding agent can inspect the model package and prepare a build-time adapter for its tokenization, preprocessing, runtime, denoising, and output format.

{{% notice Note %}}
Use an advanced coding agent that supports long-context, multi-file editing, and terminal tools. The agent needs to be able to trace Java interfaces and reason about tokenization, tensor and scheduler contracts It needs to be able to update the Gradle configuration and interpret build errors. Lightweight autocomplete or chat-only tools are unlikely to complete this workflow reliably.

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
   [ ! -d "$ANDROID_HOME/build-tools/35.0.0" ]; then
    printf 'Android SDK Platform 35 or Build-Tools 35.0.0 is unavailable.\n' >&2
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
    -not (Test-Path "$env:ANDROID_HOME\build-tools\35.0.0")) {
    throw "Android SDK Platform 35 or Build-Tools 35.0.0 is unavailable."
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

Also make sure that you meet the following prerequisites:

- Your coding agent is installed, authenticated if needed, and allowed to read, edit, and run commands in the project workspace
- You have access to the model repository and any gated or private assets
- You know the model runtime, tensor contract, and tokenizer from authoritative model documentation
- You know the scheduler, denoising behavior, and output decoding from authoritative model documentation
- You have enough disk space for the complete model package and generated build artifacts

Generated code might need review and iteration. Compatibility depends on the following factors: 

- Model package
- Android runtime library
- Native operators
- Device ABI
- Package metadata
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

The download script retrieves the complete repository because, in addition to the primary model file, the coding agent might need the following information:

- Configuration
- Tokenizer files
- Scheduler data
- Preprocessing programs
- Custom runtime information

The script uses `metadata.yaml` to identify the primary model when possible. If the metadata is missing or stale, or the package contains multiple model binaries, rerun the command with `--filename` followed by the repository-relative model path documented for the package.

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
- `ImageGenerationAdapter.java`, `ModelDescriptor.java`, and `MainActivity.java`
- `ModelImporter.java` and `download_model.py`
- `AdapterRegistry.java`, `GeneratedAdapterRegistry.java`, and `app/generated-runtime-dependencies.gradle.kts`
- `TinySdImageGenerationAdapter.java`, `TinySdRunner.java`, `ClipTokenizer.java`, and `ScheduleData.java` as examples

The prompt tells the coding agent to preserve the supplied application contract when it fits. The agent can create a runtime-specific adapter and register the adapter and one active model in `GeneratedAdapterRegistry.java`. It can update package handling and add a required runtime dependency to `app/generated-runtime-dependencies.gradle.kts`.

The agent should report that the application contracts need to be extended when the package needs any of the following:

- An input image
- Negative prompts
- Adjustable generation controls
- Multiple generated images
- Another result type

The agent shouldn't force the model into the supplied interface.

Review the generated source. The coding agent should run the included file check and report the exact command using the class it created. To run the check yourself, replace `YourGeneratedImageAdapter.java` with that generated class name:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
.hf-venv/bin/python adapter-generation/validate_generated_adapter.py \
  --adapter "app/src/main/java/org/arm/learningpath/tinysdstudio/YourGeneratedImageAdapter.java"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\.hf-venv\Scripts\python.exe adapter-generation/validate_generated_adapter.py `
  --adapter "app/src/main/java/org/arm/learningpath/tinysdstudio/YourGeneratedImageAdapter.java"
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

When `GeneratedAdapterRegistry.models()` returns one descriptor, TinySD Studio activates it instead of the built-in descriptor. Import the copied ZIP package and run representative prompts with recorded seeds. 

A successful build confirms that the source compiles. However, it doesn't prove that tokenization, tensor values, denoising, or image decoding are correct. 

Inspect the generated images for corruption and repeat the same prompt and seed. Compare the result with a trusted reference for the model package when one is available. Repeat one test in airplane mode to confirm that generation remains on-device.

## What you've accomplished

You've learned how you can extend TinySD Studio to use an image-generation model that isn't currently supported.

You can now register a compatible package with the supplied adapter or generate, build, and validate another adapter for a model with a different contract.

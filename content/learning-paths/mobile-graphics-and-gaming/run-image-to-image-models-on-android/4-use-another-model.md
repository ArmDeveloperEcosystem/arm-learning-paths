---
title: (Optional) Use an Arm AI Portal model without a validated adapter
description: Inspect another image model package and give a capable coding agent the local evidence needed to implement and validate its Android adapter.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use a coding agent to implement and validate an adapter

Use this advanced workflow only when the model doesn't match the validated MobileSAM example. A different model might need another runtime dependency, tensor mapping, and preprocessing pipeline. It might also need a different prompt control, output decoder, or result visualization.

The included LiteRT and ONNX adapter files are implementation stubs. They show where runtime-specific code belongs, but they aren't ready-made alternatives that can execute an arbitrary `.tflite` or `.onnx` model.

{{% notice Note %}}
Use an advanced coding agent that supports long-context, multi-file editing, image-model reasoning, and terminal tools. The agent needs to be able to trace Kotlin interfaces and determine tensor and preprocessing contracts from evidence. It also needs to update Gradle dependencies and interpret Android build errors. Lightweight autocomplete or chat-only tools are unlikely to complete this workflow reliably. 

Treat generated code as a starting point that needs developer review and device validation.
{{% /notice %}}

### Check the project and tools

Return to the cloned application directory and check the files and tools used by the workflow:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
cd "$HOME/image-to-image-android/ai-portal-android-app-image-to-image"
test -f scripts/inspect_android_model.py
test -x gradlew
java -version
adb get-state
.hf-venv/bin/python -c \
    'import huggingface_hub; print(huggingface_hub.__version__)'
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$IMAGE_MODEL_WORKSPACE = Join-Path $env:USERPROFILE "image-to-image-android"
Set-Location (Join-Path $IMAGE_MODEL_WORKSPACE "ai-portal-android-app-image-to-image")
Test-Path scripts\inspect_android_model.py
Test-Path gradlew.bat
java -version
adb get-state
.\.hf-venv\Scripts\python.exe -c `
    "import huggingface_hub; print(huggingface_hub.__version__)"
  {{< /tab >}}
{{< /tabpane >}}

Both Windows path checks should return `True`. The other commands identify the Java version, connected device, and `huggingface_hub` version.

### Download and inspect the model package

Run the following commands to download and inspect the model package:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
printf 'Arm model repository ID: '
read -r MODEL_SOURCE
printf 'Runtime: '
read -r MODEL_RUNTIME
printf 'Workload: '
read -r MODEL_WORKLOAD

export MODEL_ID="${MODEL_SOURCE##*/}"
export MODEL_DIR="model/custom-$MODEL_ID"
.hf-venv/bin/hf download "$MODEL_SOURCE" --local-dir "$MODEL_DIR"

.hf-venv/bin/python scripts/inspect_android_model.py \
    --model-id "$MODEL_ID" \
    --model-source "https://huggingface.co/$MODEL_SOURCE" \
    --runtime "$MODEL_RUNTIME" \
    --workload "$MODEL_WORKLOAD" \
    --local-model-dir "$MODEL_DIR"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_SOURCE = Read-Host "Arm model repository ID"
$MODEL_RUNTIME = Read-Host "Runtime"
$MODEL_WORKLOAD = Read-Host "Workload"

$MODEL_ID = Split-Path -Leaf $MODEL_SOURCE
$MODEL_DIR = Join-Path "model" "custom-$MODEL_ID"
.\.hf-venv\Scripts\hf.exe download $MODEL_SOURCE --local-dir $MODEL_DIR

.\.hf-venv\Scripts\python.exe scripts\inspect_android_model.py `
    --model-id $MODEL_ID `
    --model-source "https://huggingface.co/$MODEL_SOURCE" `
    --runtime $MODEL_RUNTIME `
    --workload $MODEL_WORKLOAD `
    --local-model-dir $MODEL_DIR
  {{< /tab >}}
{{< /tabpane >}}

Enter the complete Arm Hugging Face repository ID, runtime, and workload when prompted. Use `executorch`, `litert`, or `onnxruntime` for the runtime. Use `image-segmentation` or `image-to-image` for the workload.

The script creates `android_model_config.json`, `model-context/model-summary.json`, and copied metadata under `model-context/metadata/`. Review the summary and confirm that it identifies the intended Android artifact and its supporting files. If the summary lists several candidates, identify the correct artifact from the model card before continuing.

### Give the coding agent local evidence

Open the coding agent in the application project and ask it to:

1. Read `android_model_config.json`, `model-context/model-summary.json`, copied metadata, and the model card.
2. Read `model_catalog.json` and the closest model adapter.
3. Read `RuntimeRunner.kt`, `RuntimeRunnerFactory.kt`, `ImageLoader.kt`, and `MainActivity.kt`.
4. State the documented model inputs and outputs, preprocessing, runtime dependency, Android requirements, and artifact layout before editing code.
5. Update one catalog entry and implement only the model-specific adapter and factory wiring selected by the runtime.
6. Add a pinned official Android runtime dependency.
7. Report any required AAR or native library instead of inventing its package name or location.
8. Validate every required file under `filesDir/models/<model-id>/`, and keep resolved paths inside that directory.
9. Implement the documented image resizing, color conversion, normalization, and prompt encoding.
10. Implement the documented tensor order, runtime call, output decoding, and result rendering.
11. Update the UI only when the new model needs different input controls or an output other than a segmentation mask.
12. Build and lint the debug APK, then report the exact model files to copy to the phone and any facts that remain unresolved.

The agent must not embed access tokens, download models from the Android application, or silently change runtimes. It must not infer tensor order from names alone, or claim success while a dependency or model contract is unknown.

### Review and validate the result

Review every generated source and build-file change. After review, build the application:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
./gradlew :app:assembleDebug :app:lintDebug
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:assembleDebug :app:lintDebug
  {{< /tab >}}
{{< /tabpane >}}

Copy the exact files reported by the agent into the catalog's application-private model directory. Test representative images against a documented reference implementation or known-good result. A successful build proves that the source compiles. However, it doesn't prove that preprocessing, tensor mapping, or output decoding is correct.

## What you've accomplished

You've inspected another Arm AI Portal image model, supplied a coding agent with local model evidence, and identified the build and device checks needed to validate its adapter.

You can use these steps to run Arm AI Portal image models that don't have a validated adapter.

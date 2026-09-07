---
title: (Optional) Use an object-detection model not currently supported by Scene Detector
description: Register a compatible mobile object detector or generate and validate support for a model that needs another adapter.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose an implementation route

Scene Detector already supports the YOLO models listed in the supported model table on [Import and run an Arm AI Portal object-detection model](/learning-paths/mobile-graphics-and-gaming/ai-portal-mobile-object-detection/3-run-model/). You don't need to change the application to use those models.

You can try one of two hands-on routes to use a model that Scene Detector doesn't currently support:

- Register the model directly when it matches a supplied detector strategy
- Use the coding-agent workflow to generate another adapter.

Record the following information for the model and compare them with the supplied strategies before changing code:

- Runtime
- Callable method
- Input shape
- Layout
- Data type
- Resize method
- Normalization
- Output tensors
- Label set
- Box format
- Postprocessing requirements

| Model compatibility | Hands-on workflow |
| --- | --- |
| Matches a supplied strategy's methods, tensors, preprocessing, labels, box format, and postprocessing | Register another compatible model |
| Differs in any of those areas | Generate another adapter using a coding agent |

Sharing a runtime doesn't make detector packages interchangeable. Two ExecuTorch detector packages can expose different tensors, box formats, preprocessing, and output decoding.

### Register another compatible model

You can reuse a supplied strategy when another model has the same complete execution contract as one of the supported packages.

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

If the repository contains more than one `.pte` file, rerun the downloader with `--filename` followed by the exact model filename.

Add one descriptor to the list returned by `CompatibleModelRegistry.models()`. This example registers another detector that matches the supplied YOLOv8 strategy:

```java
static List<ModelDescriptor> models() {
    return List.of(
            new ModelDescriptor(
                    "my-yolov8-detector",
                    "My YOLOv8 detector",
                    ExecuTorchObjectDetectionAdapter.ID,
                    "ExecuTorch",
                    "my-yolov8-detector.pte",
                    ExecuTorchObjectDetectionAdapter.CONFIG_YOLO_V8,
                    75
            )
    );
}
```

The filename must match the downloaded file. Select the configuration that matches the complete model package, then rebuild and install the APK. Importing the model automatically activates the supplied ExecuTorch adapter and its confidence control.

Don't register a detector based only on its `.pte` extension or family name. A different export can change tensor ordering, box encoding, label mapping, or postprocessing while keeping a similar repository name.

### Determine when the supplied adapter doesn't fit

Add a strategy inside the supplied ExecuTorch adapter when the model keeps the same single-image or camera workflow but needs different preprocessing or output decoding.

The strategy must validate the model methods and tensor shapes and prepare the `640 × 640` input expected by the package. It must also decode boxes and class scores, scale coordinates back to the source image, and apply the documented confidence filtering and non-maximum suppression. Add a configuration constant to `ExecuTorchObjectDetectionAdapter.java` and reference it from the model descriptor.

Use the model package as the source of truth. A detector can load and execute while producing misplaced boxes or incorrect labels because any of the following are wrong:

- Resize
- Padding
- Coordinate system
- Class mapping
- Box decoder 

Use a separate adapter when the runtime or callable methods change but the model still performs independent object detection on one bitmap at a time. The adapter can reuse the supplied confidence control and return bounding boxes through `DetectionResult`.

For example, a LiteRT object detector could use the same `DetectionAdapter` interface and reuse the supplied image input, camera input, confidence control, and overlay UI. Implement it as a separate LiteRT adapter with the LiteRT dependency, `.tflite` validation, preprocessing, model runner, and output decoder. The supplied application doesn't include a tested LiteRT adapter, and you shouldn't pass a `.tflite` model to its ExecuTorch adapter.

A separate adapter isn't enough when the workflow no longer fits those shared interfaces. Tracking needs persistent state across frames. A multi-frame model needs frame scheduling and model inputs that preserve temporal order. Instance segmentation, pose estimation, or another task can need different result types, controls, and overlays. Extend `DetectionAdapter.java`, `DetectionRunner.java`, and `MainActivity.java` before adding such a workflow.

Keep image acquisition, model execution, and overlay rendering separate where possible. The supplied camera and document-picker paths both produce bitmaps, so another per-image detector can normally reuse them.

### Generate another adapter using a coding agent

Use this workflow when the model doesn't match every part of a supplied detector strategy's contract. A coding agent can inspect the model package and prepare a build-time adapter for its preprocessing, task, runtime, and model format.

{{% notice Note %}}
Use an advanced coding agent that supports long-context, multi-file editing and terminal tools. The agent needs to be able to trace Java interfaces and reason about tensor, preprocessing, and box-decoding contracts. It needs to be able to update Gradle configuration and interpret build errors. 

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

Also make sure:

- Your coding agent is installed, authenticated if needed, and allowed to read, edit, and run commands in the project workspace
- You have access to the model repository
- You have access to an approved account and access token if you're using a gated or private repository 
- You know the model runtime, tensor contract, preprocessing, box decoding, label mapping, and postprocessing from authoritative model documentation
- You have enough disk space for the complete model package and representative images with known reference detections

Generated code might need review and iteration. Results depend on whether the coding agent can inspect files, edit multiple files, and run Android build commands.

Compatibility depends on the following factors:

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

The download script retrieves the complete repository because the coding agent might need configuration, labels, anchors, or other package assets in addition to the primary model file.

If the package metadata references a missing file and the repository contains more than one optimized model, add `--filename "<model-file>"` to the download command.

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
- `DetectionAdapter.java`, `AdapterDefinition.java`, `DetectionRunner.java`, `Detection.java`, and `DetectionResult.java`
- `ModelDescriptor.java`, `GeneratedAdapterRegistry.java`, and `app/generated-runtime-dependencies.gradle.kts`
- `ExecuTorchObjectDetectionAdapter.java`
- `ExecuTorchYoloDetector.java`, `ExecuTorchDetrDetector.java`, and `ExecuTorchSsdDetector.java` as strategy examples

The prompt tells the coding agent to keep the supplied ExecuTorch adapter unchanged. It can create a detector strategy or a runtime-specific adapter and register the adapter and model in `GeneratedAdapterRegistry.java`. It can also add reviewed resources and a required runtime dependency to `app/generated-runtime-dependencies.gradle.kts`.

The agent should report that the application contracts need to be extended when the package needs the following:

- Tracking
- Multi-frame input
- Different controls
- Multiple model files selected at run time
- Another result type

The agent shouldn't force the model into the supplied interface.

Review the generated source. The coding agent should run the included file check and report the exact command using the files it created. To run the check yourself, replace `YourGeneratedAdapter.java` with the generated class name:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
.hf-venv/bin/python adapter-generation/validate_generated_adapter.py \
  --adapter "app/src/main/java/org/arm/learningpath/objectdetection/YourGeneratedAdapter.java"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\.hf-venv\Scripts\python.exe adapter-generation/validate_generated_adapter.py `
  --adapter "app/src/main/java/org/arm/learningpath/objectdetection/YourGeneratedAdapter.java"
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

Install the application and copy the model with the commands used on every operating system:

```console
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb push "$MODEL_FILE" /sdcard/Download/
```

Open the mode added by the generated adapter, import the copied model file, and follow its controls. A successful build confirms that the source compiles. However, it doesn't prove that preprocessing, tensor values, labels, box decoding, or coordinate scaling are correct. Test images similar to what the application will receive on the target device, and compare the results with a known reference for the model package.

## What you've accomplished

You've learned how you can extend Scene Detector to use an object-detection model that's not currently supported.

You can now register a compatible detector with a supplied strategy or generate, build, and validate another adapter for a model with a different contract.

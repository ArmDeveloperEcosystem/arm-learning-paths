---
title: Build and run the default Android text-generation application
description: Connect an Arm-based Android phone, download SmolLM2, apply the validated ExecuTorch adapter, and install the application.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect an Android phone

Enable **Developer options** and **USB debugging** on the phone. Connect it with a data-capable USB cable, unlock it, and accept the debugging authorization prompt.

Verify the connection:

```console
adb devices -l
```

The output must list the phone's serial with the status `device`. Don't continue if the list is empty or the status is `unauthorized` or `offline`. Unlock the phone and accept the debugging prompt if authorization is pending. Windows might also need the phone manufacturer's USB driver. If the phone doesn't appear, see [Run apps on a hardware device](https://developer.android.com/studio/run/device).

## Prepare the workspace and model downloader

Create the workspace used by the remaining pages:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
mkdir -p "$HOME/text-to-text-android"
cd "$HOME/text-to-text-android"
python3 -m venv .hf-venv
.hf-venv/bin/python -m pip install --upgrade pip huggingface_hub
.hf-venv/bin/hf auth login
.hf-venv/bin/hf auth whoami
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$TEXT_MODEL_WORKSPACE = Join-Path $env:USERPROFILE "text-to-text-android"
New-Item -ItemType Directory -Force -Path $TEXT_MODEL_WORKSPACE | Out-Null
Set-Location $TEXT_MODEL_WORKSPACE
python -m venv .hf-venv
.\.hf-venv\Scripts\python.exe -m pip install --upgrade pip huggingface_hub
.\.hf-venv\Scripts\hf.exe auth login
.\.hf-venv\Scripts\hf.exe auth whoami
  {{< /tab >}}
{{< /tabpane >}}

The Arm AI Portal model packages that you'll use are published by Arm and hosted in Arm's Hugging Face repositories. Sign in with a Hugging Face account that has access to the model repositories and use a read token when prompted.

## Download SmolLM2

Start with SmolLM2 360M Instruct through ExecuTorch. It's the smallest validated text-generation example supplied with the Android application and provides the shortest path to a working result.

Run the command from the `text-to-text-android` workspace to download the complete optimized model package, including the `.pte` program, configuration, tokenizer, and chat template:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export MODEL_ID="smollm2-360m-instruct-8da4w-xnnpack-executorch"
.hf-venv/bin/hf download "Arm/$MODEL_ID" --local-dir ./model
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_ID = "smollm2-360m-instruct-8da4w-xnnpack-executorch"
.\.hf-venv\Scripts\hf.exe download "Arm/$MODEL_ID" --local-dir .\model
  {{< /tab >}}
{{< /tabpane >}}

The `model` directory contains `HuggingFaceTB__SmolLM2-360M-Instruct_executorch_optimized.pte`, `config.yaml`, and the tokenizer directory. Keep the filenames and directory structure unchanged because the validated adapter checks those paths when it loads the model.

Model repositories can change over time. After downloading a model, compare the files in `./model` with the model file expected by the selected validated example and with the inspection output. 

{{% notice Note %}}
If the expected artifact filename isn't present, don't rename files or continue with a catalog entry that points to a missing `.pte`, `.tflite`, `.litertlm`, `.onnx`, or external data file. Update the validated example or catalog to the current artifact confirmed by the model card, or pin the model download to a known working revision.
{{% /notice %}}

## Check the model package

The [SmolLM2 ExecuTorch model card](https://huggingface.co/Arm/smollm2-360m-instruct-8da4w-xnnpack-executorch) identifies the runtime, quantization, intended target, and required files. Before deploying another model, use its model card to confirm the same information, together with its Android and memory requirements.

The model package is a pre-exported runtime artifact. You don't need to export, quantize, or tune the model.

## Validated model examples

The starter application contains one validated adapter example for each model. Complete the SmolLM2 workflow first. 

When you want to try another runtime or workload, return to the following table:

| Model | Runtime | Workload | Validated example |
| --- | --- | --- | --- |
| [SmolLM2 360M Instruct](https://huggingface.co/Arm/smollm2-360m-instruct-8da4w-xnnpack-executorch) | ExecuTorch 1.1.0 | Text generation | `smollm2-executorch` |
| [BGE Base English v1.5](https://huggingface.co/Arm/bge-base-en-v1.5-int8-litert) | LiteRT 1.4.2 | Text embedding | `bge-base-litert` |
| [TinyLlama 1.1B Chat](https://huggingface.co/Arm/tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-vivo-x300) | ONNX Runtime GenAI | Text generation | `tinyllama-onnx-genai` |

The model and runtime change together in these examples, so their results and timings aren't controlled runtime benchmarks.

## Clone the starter application

The starter application provides the shared model selector, text input, and **Load** and **Run** actions. The application also provides result display, model catalog, and an adapter interface. 

Clone the starter application into the workspace:

```console
git clone https://github.com/arm-education/ai-portal-android-app-text-to-text.git
cd ai-portal-android-app-text-to-text
```

Run the remaining commands from the repository root.

## Apply the validated SmolLM2 adapter

The base project keeps its runtime dependencies and adapters minimal. Apply the supplied example that contains the SmolLM2 catalog entry, ExecuTorch adapter, and pinned ExecuTorch Android dependency:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
cp -R adapter-examples/smollm2-executorch/app/. app/
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
Copy-Item -Path "adapter-examples\smollm2-executorch\app\*" `
    -Destination "app" -Recurse -Force
  {{< /tab >}}
{{< /tabpane >}}

The example adds `org.pytorch:executorch-android:1.1.0` to the build and registers the expected model and tokenizer files in `model_catalog.json`.

## Build and install the application

Before building, confirm that Gradle is running with JDK 17:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
./gradlew --version
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat --version
  {{< /tab >}}
{{< /tabpane >}}

The `Launcher JVM` line should report version 17. The `Daemon JVM` line should point to the JDK 17 installation or state that it uses the current Java home. If either JVM uses another version, set `JAVA_HOME` to your JDK 17 installation and stop the existing Gradle daemon before trying again:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
./gradlew --stop
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat --stop
  {{< /tab >}}
{{< /tabpane >}}

{{% notice Note %}}
If `:app:lintAnalyzeDebug` fails and the nested error contains only a Java version number, such as `25`, Gradle is using an unvalidated JDK. Set `JAVA_HOME` to JDK 17, stop the Gradle daemon, and run the build again.
{{% /notice %}}

Build and lint the debug APK:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
chmod +x gradlew
./gradlew :app:assembleDebug :app:lintDebug
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:assembleDebug :app:lintDebug
  {{< /tab >}}
{{< /tabpane >}}

Continue only when the Gradle output ends with `BUILD SUCCESSFUL`. A message that Gradle can't strip a prebuilt `.so` library is a packaging warning and doesn't cause the build to fail.

Confirm that the phone is still connected before installing the application:

```console
adb devices -l
```

Continue only if the phone is listed with the status `device`. Then install the APK and start the main activity:

```console
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.arm.learningpath.texttotext/.ui.MainActivity
```

The application opens with SmolLM2 selected. Its status shows that the required model file is missing because the model package hasn't been copied into the application's private storage yet.

## Understand the example files

The validated example changes only the model-specific parts of the application:

| File | Purpose |
| --- | --- |
| `app/src/main/assets/model_catalog.json` | Maps SmolLM2 to its files, task, limits, and `executorch` runtime. |
| `app/src/main/java/com/arm/learningpath/texttotext/inference/models/smollm2/ExecuTorchTextGenerationAdapter.kt` | Validates the package, tokenizes the prompt, calls the `.pte` program, and decodes the completion. |
| `app/src/main/java/com/arm/learningpath/texttotext/inference/RuntimeRunnerFactory.kt` | Registers the adapter selected by the catalog's runtime value. |
| `app/build.gradle.kts` | Packages the pinned ExecuTorch Android runtime in the APK. |

The downloaded model files remain outside the APK. This keeps the application build smaller, so you can replace the model package without embedding its weights in the application.

## What you've accomplished and what's next

You've now connected an Arm-based Android phone, downloaded the default model, applied its validated adapter, and installed an application ready to load SmolLM2. 

Next, you'll run the model on the Android phone.

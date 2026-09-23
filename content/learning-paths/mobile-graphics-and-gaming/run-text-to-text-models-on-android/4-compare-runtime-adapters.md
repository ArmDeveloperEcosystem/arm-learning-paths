---
title: Compare validated text-generation adapters
description: Understand the default ExecuTorch adapter and optionally run the same Android workflow with ONNX Runtime GenAI.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the default adapter

The unmodified starter application uses a mock runner so that its interface can build without a model runtime. When you applied the SmolLM2 example, you replaced that mock setup with `ExecuTorchTextGenerationAdapter` with SmolLM2 360M Instruct.

An adapter is the application code between the shared Android interface and a particular model runtime. `ui/MainActivity.kt` reads the selected entry from `model_catalog.json`. `inference/RuntimeRunnerFactory.kt` creates the adapter named by its `runtime` value.

The adapter then:

- Checks that the expected model, tokenizer, configuration, and template files are present
- Converts the prompt into the inputs required by the runtime
- Calls the runtime packaged in the APK
- Decodes and cleans the generated tokens for display

The downloaded model package isn't an Android executable. Gradle packages the runtime's Java and native libraries in the APK. The adapter uses those libraries to load and execute the model artifact stored in the application's private directory.

## Choose a text-generation path

The application includes three validated text-generation examples that share the interface and deployment flow. However, each needs an adapter because its runtime API, model format, tokenizer handling, and output contract differ.

The following table describes the paths:

| Path | Catalog runtime | Adapter | Model package | What it demonstrates |
| --- | --- | --- | --- | --- |
| SmolLM2 with ExecuTorch | `executorch` | `inference/models/smollm2/ExecuTorchTextGenerationAdapter` | `.pte`, configuration, tokenizer, and chat template | The recommended default and smallest validated generation example. |
| TinyLlama with ONNX Runtime GenAI | `onnxruntime` | `inference/models/tinyllama/OnnxTextGenerationAdapter` | ONNX model directory, configuration, tokenizer, and chat template | A directory-based GenAI package with an additional Android AAR dependency. |
| Llama 3.2 with ONNX Runtime GenAI | `onnxruntime` | `inference/models/llama32/OnnxTextGenerationAdapter` | ONNX model directory, configuration, tokenizer, and chat template | The same GenAI runtime flow with the Llama 3.2 package. |

The repository also contains `inference/models/bge/LiteRtEmbeddingAdapter` for the catalog runtime `litert`. That adapter runs the BGE text-embedding workload and returns vectors rather than generated text, so it is listed separately from the text-generation paths.

You've already completed the recommended ExecuTorch path. Choose one of the alternative paths only if you want to compare the integration process with another runtime. The model changes with the runtime, so this isn't a controlled performance comparison.

### Keep the default ExecuTorch path

No additional setup is needed. The SmolLM2 example adds `org.pytorch:executorch-android:1.1.0`, registers the `executorch` catalog entry, and supplies the adapter that loads the `.pte` program.

During **Load**, the adapter:
 
 - Checks the package paths
 - Creates the tokenizer
 - Loads the program
 - Makes a probe call to confirm that the output matches the expected vocabulary
 
This checks compatibility with the adapter and doesn't evaluate the model's language quality or accuracy.


### Prepare the ONNX Runtime GenAI path

The ONNX Runtime GenAI examples use `com.microsoft.onnxruntime:onnxruntime-android:1.27.0` and the official ONNX Runtime GenAI Android AAR. Build the AAR from the official ONNX Runtime GenAI source before you apply an ONNX Runtime GenAI adapter.

Set `ANDROID_HOME` to your Android SDK location. Set `ANDROID_NDK_HOME` to the installed Android NDK directory, or replace it in the commands below. Android Studio installs the SDK and NDK from **Tools > SDK Manager > SDK Tools**.

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export WORK_DIR="$HOME/text-to-text-android"
mkdir -p "$WORK_DIR"
cd "$WORK_DIR"

git clone --recursive https://github.com/microsoft/onnxruntime-genai.git
cd onnxruntime-genai

python3 -m pip install -r requirements-dev.txt
if ! command -v cmake >/dev/null 2>&1; then
    if ! ls -d "$ANDROID_HOME"/cmake/*/bin >/dev/null 2>&1; then
        "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" \
            --sdk_root="$ANDROID_HOME" \
            "cmake;3.22.1"
    fi
    export PATH="$(ls -d "$ANDROID_HOME"/cmake/*/bin | tail -n 1):$PATH"
fi
cmake --version

python3 build.py --skip_wheel --build_java --android \
    --android_home "$ANDROID_HOME" \
    --android_ndk_path "$ANDROID_NDK_HOME" \
    --android_abi arm64-v8a \
    --config Release

export ONNX_GENAI_AAR="$PWD/build/Android/Release/src/java/build/android/outputs/aar/onnxruntime-genai-release.aar"
test -f "$ONNX_GENAI_AAR"
cd "$WORK_DIR"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$WORK_DIR = Join-Path $HOME "text-to-text-android"
New-Item -ItemType Directory -Force -Path $WORK_DIR
Set-Location $WORK_DIR

git clone --recursive https://github.com/microsoft/onnxruntime-genai.git
Set-Location onnxruntime-genai

python -m pip install -r requirements-dev.txt
if (-not (Get-Command cmake -ErrorAction SilentlyContinue)) {
    if (-not (Test-Path "$env:ANDROID_HOME\cmake")) {
        & "$env:ANDROID_HOME\cmdline-tools\latest\bin\sdkmanager.bat" `
            --sdk_root="$env:ANDROID_HOME" `
            "cmake;3.22.1"
    }
    $CMAKE_DIR = Get-ChildItem "$env:ANDROID_HOME\cmake" -Directory | Sort-Object Name | Select-Object -Last 1
    $env:PATH = "$($CMAKE_DIR.FullName)\bin;$env:PATH"
}
cmake --version

python build.py --skip_wheel --build_java --android `
    --android_home "$env:ANDROID_HOME" `
    --android_ndk_path "$env:ANDROID_NDK_HOME" `
    --android_abi arm64-v8a `
    --config Release

$ONNX_GENAI_AAR = Join-Path $PWD "build\Android\Release\src\java\build\android\outputs\aar\onnxruntime-genai-release.aar"
Test-Path $ONNX_GENAI_AAR
Set-Location $WORK_DIR
  {{< /tab >}}
{{< /tabpane >}}

Create a separate project and select one ONNX Runtime GenAI example:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
cd "$WORK_DIR"
git clone https://github.com/arm-education/ai-portal-android-app-text-to-text.git \
    ai-portal-android-app-text-to-text-onnx
cd ai-portal-android-app-text-to-text-onnx

# Choose one validated ONNX Runtime GenAI example.
export ONNX_EXAMPLE="tinyllama-onnx-genai"
export MODEL_ID="tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-vivo-x300"
# Or use Llama 3.2 instead:
# export ONNX_EXAMPLE="llama-3-2-onnx-genai"
# export MODEL_ID="llama-3-2-1b-instruct-onnx-genai-int4-kquantlast-emb-int8-vivo-x300"

cp -R "adapter-examples/$ONNX_EXAMPLE/app/." app/
mkdir -p app/libs
cp "$ONNX_GENAI_AAR" app/libs/onnxruntime-genai-release.aar

export MODEL_DIR="../model-onnx"
../.hf-venv/bin/hf download "Arm/$MODEL_ID" --local-dir "$MODEL_DIR"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
Set-Location $WORK_DIR
git clone https://github.com/arm-education/ai-portal-android-app-text-to-text.git `
    ai-portal-android-app-text-to-text-onnx
Set-Location ai-portal-android-app-text-to-text-onnx

# Choose one validated ONNX Runtime GenAI example.
$ONNX_EXAMPLE = "tinyllama-onnx-genai"
$MODEL_ID = "tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-vivo-x300"
# Or use Llama 3.2 instead:
# $ONNX_EXAMPLE = "llama-3-2-onnx-genai"
# $MODEL_ID = "llama-3-2-1b-instruct-onnx-genai-int4-kquantlast-emb-int8-vivo-x300"

Copy-Item -Path "adapter-examples\$ONNX_EXAMPLE\app\*" `
    -Destination "app" -Recurse -Force
New-Item -ItemType Directory -Force -Path "app\libs"
Copy-Item -Path $ONNX_GENAI_AAR -Destination "app\libs\onnxruntime-genai-release.aar" -Force

$MODEL_DIR = "..\model-onnx"
..\.hf-venv\Scripts\hf.exe download "Arm/$MODEL_ID" --local-dir $MODEL_DIR
  {{< /tab >}}
{{< /tabpane >}}

The commands above copy the generated AAR to `app/libs/onnxruntime-genai-release.aar`. Keep every file in the downloaded ONNX model directory together, including external model data, `genai_config.json`, tokenizer files, and the chat template.

## Build and run the selected alternative

The selected ONNX Runtime GenAI alternative now follows the same workflow: build the APK, install the APK, copy the chosen model package to the directory named by its catalog ID, and start the application.

Continue in the same terminal so that `MODEL_ID` and `MODEL_DIR` remain set:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export ANDROID_PACKAGE="com.arm.learningpath.texttotext"

chmod +x gradlew
./gradlew :app:assembleDebug :app:lintDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk

adb shell "mkdir -p /data/local/tmp/text-to-text-models/$MODEL_ID"
adb push "$MODEL_DIR/." "/data/local/tmp/text-to-text-models/$MODEL_ID/"
adb shell "run-as $ANDROID_PACKAGE mkdir -p files/models/$MODEL_ID"
adb shell "run-as $ANDROID_PACKAGE cp -r /data/local/tmp/text-to-text-models/$MODEL_ID/. files/models/$MODEL_ID/"
adb shell "run-as $ANDROID_PACKAGE find files/models/$MODEL_ID -maxdepth 4 -type f"
adb shell am start -n "$ANDROID_PACKAGE/.ui.MainActivity"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$ANDROID_PACKAGE = "com.arm.learningpath.texttotext"

.\gradlew.bat :app:assembleDebug :app:lintDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk

adb shell "mkdir -p /data/local/tmp/text-to-text-models/$MODEL_ID"
adb push "$MODEL_DIR\." "/data/local/tmp/text-to-text-models/$MODEL_ID/"
adb shell "run-as $ANDROID_PACKAGE mkdir -p files/models/$MODEL_ID"
adb shell "run-as $ANDROID_PACKAGE cp -r /data/local/tmp/text-to-text-models/$MODEL_ID/. files/models/$MODEL_ID/"
adb shell "run-as $ANDROID_PACKAGE find files/models/$MODEL_ID -maxdepth 4 -type f"
adb shell am start -n "$ANDROID_PACKAGE/.ui.MainActivity"
  {{< /tab >}}
{{< /tabpane >}}

In the application, do the following:

1. Select the model from the catalog.
2. Select **Load**.
3. Enter the same privacy prompt used for SmolLM2.
4. Select **Run**. 

A successful result is a relevant completion without prompt echoes, control tokens, or runtime diagnostic text.

## What you've accomplished and what's next

You've now identified the default real adapter and distinguished the validated text-generation integrations. You also optionally repeated the common Android deployment workflow with ONNX Runtime GenAI.

Next, you'll verify on-device text generation.

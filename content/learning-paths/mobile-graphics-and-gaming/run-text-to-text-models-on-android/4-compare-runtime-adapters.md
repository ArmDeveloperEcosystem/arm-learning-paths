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

The application includes two validated text-generation paths that share the interface and deployment flow. However, each needs an adapter because its runtime API, model format, tokenizer handling, and output contract differ.

The following table describes the paths:

| Path | Catalog runtime | Adapter | Model package | What it demonstrates |
| --- | --- | --- | --- | --- |
| SmolLM2 with ExecuTorch | `executorch` | `inference/models/smollm2/ExecuTorchTextGenerationAdapter` | `.pte`, configuration, tokenizer, and chat template | The recommended default and smallest validated generation example. |
| TinyLlama with ONNX Runtime GenAI | `onnxruntime` | `inference/models/tinyllama/OnnxTextGenerationAdapter` | ONNX model directory, configuration, tokenizer, and chat template | A directory-based GenAI package with an additional Android AAR dependency. |

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

The TinyLlama example uses `com.microsoft.onnxruntime:onnxruntime-android:1.27.0` and the official ONNX Runtime GenAI Android AAR. First, complete the [ONNX Runtime GenAI Android Learning Path](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-android-chat-app-using-onnxruntime/) to build `onnxruntime-genai-release.aar`.

Create a separate project and download the complete model directory:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
cd ..
git clone https://github.com/arm-education/ai-portal-android-app-text-to-text.git \
    ai-portal-android-app-text-to-text-onnx
cd ai-portal-android-app-text-to-text-onnx

cp -R adapter-examples/tinyllama-onnx-genai/app/. app/

export MODEL_ID="tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-vivo-x300"
export MODEL_DIR="../model-onnx"
../.hf-venv/bin/hf download "Arm/$MODEL_ID" --local-dir "$MODEL_DIR"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
Set-Location ..
git clone https://github.com/arm-education/ai-portal-android-app-text-to-text.git `
    ai-portal-android-app-text-to-text-onnx
Set-Location ai-portal-android-app-text-to-text-onnx

Copy-Item -Path "adapter-examples\tinyllama-onnx-genai\app\*" `
    -Destination "app" -Recurse -Force

$MODEL_ID = "tinyllama-1-1b-chat-onnx-genai-int4-kquantlast-emb-int8-vivo-x300"
$MODEL_DIR = "..\model-onnx"
..\.hf-venv\Scripts\hf.exe download "Arm/$MODEL_ID" --local-dir $MODEL_DIR
  {{< /tab >}}
{{< /tabpane >}}

Copy the generated AAR to `app/libs/onnxruntime-genai-release.aar` before continuing. Keep every file in the downloaded ONNX model directory together, including external model data, `genai_config.json`, tokenizer files, and the chat template.

## Build and run the selected alternative

The ONNX Runtime GenAI alternative now follows the same workflow: build the APK, install the APK, copy the chosen model package to the directory named by its catalog ID, and start the application.

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

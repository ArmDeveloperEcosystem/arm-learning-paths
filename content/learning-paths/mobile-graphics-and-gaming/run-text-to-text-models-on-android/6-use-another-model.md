---
title: (Optional) Use an Arm AI Portal model without a validated example
description: Inspect another model package and give a capable coding agent the local evidence needed to implement and validate one runtime adapter.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the project and tools

Use this advanced workflow only when the model doesn't match one of the validated examples. The model might need different files, tokenization, or prompt formatting. It might also need different tensor mapping, runtime APIs, or output decoding.

{{% notice Note %}}
Use an advanced coding agent that supports long-context, multi-file editing and terminal tools. The agent needs to be able to trace Kotlin interfaces and reason about tokenizer and tensor contracts. It needs to update Gradle dependencies and interpret Android build errors. Lightweight autocomplete or chat-only tools are unlikely to complete this workflow reliably. 

Treat generated code as a starting point that needs developer review and device validation.
{{% /notice %}}

Start by returning to the original starter project and verifying the files and tools used by the workflow:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
cd "$HOME/text-to-text-android/ai-portal-android-app-text-to-text"
test -f scripts/inspect_android_model.py
test -x gradlew
git rev-parse --show-toplevel
java -version
adb get-state
../.hf-venv/bin/python -c \
    'import huggingface_hub; print(huggingface_hub.__version__)'
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$TEXT_MODEL_WORKSPACE = Join-Path $env:USERPROFILE "text-to-text-android"
Set-Location (Join-Path $TEXT_MODEL_WORKSPACE "ai-portal-android-app-text-to-text")
Test-Path scripts\inspect_android_model.py
Test-Path gradlew.bat
git rev-parse --show-toplevel
java -version
adb get-state
..\.hf-venv\Scripts\python.exe -c `
    "import huggingface_hub; print(huggingface_hub.__version__)"
  {{< /tab >}}
{{< /tabpane >}}

The output identifies the project root, Java version, connected device, and `huggingface_hub` version. Both Windows path checks should return `True`.

## Download and inspect the model package

Run the following commands to download and install the model package:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
printf 'Arm model repository ID: '
read -r MODEL_SOURCE
printf 'Runtime: '
read -r MODEL_RUNTIME
printf 'Workload: '
read -r MODEL_WORKLOAD

export MODEL_ID="${MODEL_SOURCE##*/}"
export MODEL_DIR="../model-custom-$MODEL_ID"
../.hf-venv/bin/hf download "$MODEL_SOURCE" --local-dir "$MODEL_DIR"

../.hf-venv/bin/python scripts/inspect_android_model.py \
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
$MODEL_DIR = Join-Path .. "model-custom-$MODEL_ID"
..\.hf-venv\Scripts\hf.exe download $MODEL_SOURCE `
    --local-dir $MODEL_DIR

..\.hf-venv\Scripts\python.exe scripts\inspect_android_model.py `
    --model-id $MODEL_ID `
    --model-source "https://huggingface.co/$MODEL_SOURCE" `
    --runtime $MODEL_RUNTIME `
    --workload $MODEL_WORKLOAD `
    --local-model-dir $MODEL_DIR
  {{< /tab >}}
{{< /tabpane >}}

Enter the complete Arm Hugging Face repository ID, runtime value, and workload when prompted. 
Use `executorch`, `litert-lm`, `litert`, or `onnxruntime` for the runtime. Use `text-generation` or `text-embedding` for the workload.

The script creates `android_model_config.json`, `model-context/model-summary.json`, and a directory of copied metadata. Review the summary and confirm that it identifies the intended Android artifact, tokenizer, configuration, and template files.

## Give the coding agent local evidence

Open the coding agent in the starter project and ask it to do the following:

1. Read `android_model_config.json`, `model-context/model-summary.json`, copied metadata, and the model card.
2. Read `inference/RuntimeRunner.kt`, the task-specific runner interface, and `inference/RuntimeRunnerFactory.kt`.
3. Read `model_catalog.json` and the matching adapter stub.
4. Update one catalog entry, the matching adapter, and the factory registration needed for the selected runtime value.
5. Add a pinned official Android runtime dependency. 
6. Report any required local AAR or native library before assuming its location.
7. Validate all required package files under `filesDir/models/<model-id>/` and keep all resolved paths inside that directory.
8. Implement tokenization, prompt formatting, and runtime invocation. 
9. Implement output decoding, stop-token handling, and timing based on the documented model evidence.
10. Build the debug APK and report the exact model files and application-private directory needed on the phone.

The agent must not embed access tokens or silently select another runtime. It must not invent dependency coordinates or claim success while a required AAR or native library is missing.

## Review and validate the result

Review every generated source and build-file change. After review, run the build commands from the application repository:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
./gradlew :app:assembleDebug :app:lintDebug
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:assembleDebug :app:lintDebug
  {{< /tab >}}
{{< /tabpane >}}

Copy the exact files reported by the agent into the catalog's application-private model directory. After copying the files, test representative inputs against a known reference for the package. 

A successful build proves that the source compiles. However, it doesn't prove that tokenization, tensor mapping, or decoding is correct.

## What you've accomplished

You've inspected another Arm AI Portal package, supplied a coding agent with local model evidence, and identified the build and device checks needed to validate a generated adapter.

You can now extend the workflow to use models without a validated example.

---
title: Download and stage Depth Anything V2 Small
description: Download the optimized ExecuTorch artifact and copy it into the application's private model directory.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the model artifact

Return to the cloned application directory. Download the exact Arm-optimized `.pte` file from Hugging Face:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export MODEL_ID="depth-anything-v2-small-int8-xnnpack-executorch-vivo-x300"
export MODEL_FILE="depth_anything_v2_small_executorch_optimized.pte"
export MODEL_DIR="model/$MODEL_ID"

.hf-venv/bin/hf download "Arm/$MODEL_ID" "$MODEL_FILE" \
    --local-dir "$MODEL_DIR"
test -f "$MODEL_DIR/$MODEL_FILE"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_ID = "depth-anything-v2-small-int8-xnnpack-executorch-vivo-x300"
$MODEL_FILE = "depth_anything_v2_small_executorch_optimized.pte"
$MODEL_DIR = "model\$MODEL_ID"

.\.hf-venv\Scripts\hf.exe download "Arm/$MODEL_ID" $MODEL_FILE `
    --local-dir $MODEL_DIR
Test-Path "$MODEL_DIR\$MODEL_FILE"
  {{< /tab >}}
{{< /tabpane >}}

The final check has no output on macOS or Linux when the file exists. It returns `True` on Windows. If Hugging Face requests authentication, sign in with the virtual-environment executable:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
.hf-venv/bin/hf auth login
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\.hf-venv\Scripts\hf.exe auth login
  {{< /tab >}}
{{< /tabpane >}}

Use a read token when prompted, then rerun the download command.

The artifact is an INT8 ExecuTorch program. It doesn't contain an Android executable. The application APK contains the ExecuTorch 1.3.1 runtime and its arm64 native libraries.

## Copy the model into application-private storage

Copy the file through `/data/local/tmp`, then remove that temporary device copy:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export ANDROID_PACKAGE="com.arm.learningpath.imagetoimage"

adb push "$MODEL_DIR/$MODEL_FILE" "/data/local/tmp/$MODEL_FILE"
adb shell "run-as $ANDROID_PACKAGE mkdir -p files/models/$MODEL_ID"
adb shell "run-as $ANDROID_PACKAGE cp /data/local/tmp/$MODEL_FILE files/models/$MODEL_ID/$MODEL_FILE"
adb shell "run-as $ANDROID_PACKAGE ls -l files/models/$MODEL_ID/$MODEL_FILE"
adb shell rm "/data/local/tmp/$MODEL_FILE"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$ANDROID_PACKAGE = "com.arm.learningpath.imagetoimage"

adb push "$MODEL_DIR\$MODEL_FILE" "/data/local/tmp/$MODEL_FILE"
adb shell "run-as $ANDROID_PACKAGE mkdir -p files/models/$MODEL_ID"
adb shell "run-as $ANDROID_PACKAGE cp /data/local/tmp/$MODEL_FILE files/models/$MODEL_ID/$MODEL_FILE"
adb shell "run-as $ANDROID_PACKAGE ls -l files/models/$MODEL_ID/$MODEL_FILE"
adb shell rm "/data/local/tmp/$MODEL_FILE"
  {{< /tab >}}
{{< /tabpane >}}

The `ls` output shows the model in `files/models/depth-anything-v2-small-int8-xnnpack-executorch-vivo-x300/`. The application has no Internet permission and can't access your Hugging Face credentials.

## What you've accomplished and what's next

You've downloaded the exact model and placed it in application-private storage. Next, you'll generate and validate relative-disparity maps.

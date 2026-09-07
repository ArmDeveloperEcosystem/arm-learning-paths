---
title: Run SmolLM2 on Android
description: Copy the model package into application-private storage and generate text locally with ExecuTorch.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Copy the model package to application-private storage

The application loads each model from `filesDir/models/<model-id>/`. For development, stage the downloaded package under `/data/local/tmp`, then use Android's `run-as` command to copy it into the debuggable application's private directory.

Run the following commands from the starter application repository:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export ANDROID_PACKAGE="com.arm.learningpath.texttotext"
export MODEL_ID="smollm2-360m-instruct-8da4w-xnnpack-executorch"

adb shell "mkdir -p /data/local/tmp/text-to-text-models/$MODEL_ID"
adb push ../model/. "/data/local/tmp/text-to-text-models/$MODEL_ID/"

adb shell "run-as $ANDROID_PACKAGE mkdir -p files/models/$MODEL_ID"
adb shell "run-as $ANDROID_PACKAGE cp -r /data/local/tmp/text-to-text-models/$MODEL_ID/. files/models/$MODEL_ID/"
adb shell "run-as $ANDROID_PACKAGE find files/models/$MODEL_ID -maxdepth 4 -type f"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$ANDROID_PACKAGE = "com.arm.learningpath.texttotext"
$MODEL_ID = "smollm2-360m-instruct-8da4w-xnnpack-executorch"

adb shell "mkdir -p /data/local/tmp/text-to-text-models/$MODEL_ID"
adb push ..\model\. "/data/local/tmp/text-to-text-models/$MODEL_ID/"

adb shell "run-as $ANDROID_PACKAGE mkdir -p files/models/$MODEL_ID"
adb shell "run-as $ANDROID_PACKAGE cp -r /data/local/tmp/text-to-text-models/$MODEL_ID/. files/models/$MODEL_ID/"
adb shell "run-as $ANDROID_PACKAGE find files/models/$MODEL_ID -maxdepth 4 -type f"
  {{< /tab >}}
{{< /tabpane >}}

The final command lists the `.pte` program, `config.yaml`, and tokenizer files under the model ID directory. That directory name must match the `id` field in `model_catalog.json`.

## Generate text

Start or return to the application:

```console
adb shell am start -n com.arm.learningpath.texttotext/.ui.MainActivity
```

To run the model:

1. Select **SmolLM2 360M Instruct 8da4w**.
2. Select **Load** and wait for the status to report the model load time.
3. Enter the following prompt:

   ```text
   Write one sentence explaining why on-device AI is more private than cloud AI.
   ```

4. Select **Run**.

The result area displays a generated completion together with model load and run times. The wording can vary because this is a generative model, but it should answer the prompt and shouldn't contain chat-template markers or tokenizer control tokens.

The timing is illustrative rather than a benchmark. Measure the model on your target phone before making deployment choices.

## What you've accomplished and what's next

You've now copied the complete SmolLM2 package into application-private storage and generated text locally with the packaged ExecuTorch runtime. 

Next, you'll compare the validated text-generation adapters.

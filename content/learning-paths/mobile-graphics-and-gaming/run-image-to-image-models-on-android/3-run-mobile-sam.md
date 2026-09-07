---
title: Run MobileSAM with ExecuTorch on Android
description: Download the validated MobileSAM package, copy it into application-private storage, and generate a segmentation mask with ExecuTorch.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the validated model

MobileSAM with ExecuTorch is the only validated model path for this Learning Path. The application already contains its catalog entry, adapter, preprocessing, and mask rendering.

Run the download from the cloned application directory:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export MODEL_ID="mobile-sam-int8-xnnpack-executorch"
export MODEL_FILE="mobile_sam_raspberry_executorch_optimized.pte"
export MODEL_DIR="model/$MODEL_ID"

.hf-venv/bin/hf download "Arm/$MODEL_ID" "$MODEL_FILE" \
    --local-dir "$MODEL_DIR"
test -f "$MODEL_DIR/$MODEL_FILE"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_ID = "mobile-sam-int8-xnnpack-executorch"
$MODEL_FILE = "mobile_sam_raspberry_executorch_optimized.pte"
$MODEL_DIR = "model\$MODEL_ID"

.\.hf-venv\Scripts\hf.exe download "Arm/$MODEL_ID" $MODEL_FILE `
    --local-dir $MODEL_DIR
Test-Path "$MODEL_DIR\$MODEL_FILE"
  {{< /tab >}}
{{< /tabpane >}}

The final check returns no output on macOS or Linux when the file exists. On Windows, it returns `True`.

The `.pte` file is a pre-exported model program and its parameters. The file isn't an Android executable. The application APK already contains ExecuTorch 1.3.1 and its native runtime libraries, which load and execute this model program.

## Copy the model to application-private storage

The catalog tells the application to load the model from `filesDir/models/mobile-sam-int8-xnnpack-executorch/`. Stage the downloaded file under `/data/local/tmp`, then use `run-as` to copy it into the debuggable application's private directory:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export ANDROID_PACKAGE="com.arm.learningpath.imagetoimage"

adb push "$MODEL_DIR/$MODEL_FILE" "/data/local/tmp/$MODEL_FILE"
adb shell "run-as $ANDROID_PACKAGE mkdir -p files/models/$MODEL_ID"
adb shell "run-as $ANDROID_PACKAGE cp /data/local/tmp/$MODEL_FILE files/models/$MODEL_ID/$MODEL_FILE"
adb shell "run-as $ANDROID_PACKAGE ls -l files/models/$MODEL_ID/$MODEL_FILE"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$ANDROID_PACKAGE = "com.arm.learningpath.imagetoimage"

adb push "$MODEL_DIR\$MODEL_FILE" "/data/local/tmp/$MODEL_FILE"
adb shell "run-as $ANDROID_PACKAGE mkdir -p files/models/$MODEL_ID"
adb shell "run-as $ANDROID_PACKAGE cp /data/local/tmp/$MODEL_FILE files/models/$MODEL_ID/$MODEL_FILE"
adb shell "run-as $ANDROID_PACKAGE ls -l files/models/$MODEL_ID/$MODEL_FILE"
  {{< /tab >}}
{{< /tabpane >}}

The final command displays the copied file and its size. The model directory must match the `id` in `app/src/main/assets/model_catalog.json`.

## Generate a segmentation mask

Start the application:

```console
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
```

For the first run, choose a JPEG or PNG image with one distinct object near the center. Then:

1. Confirm that **MobileSAM INT8 Segmentation** is selected.
2. Select **Load model**.
3. Select **Choose image** and choose the image from the phone.
4. Confirm that the dashed prompt box covers the object that you want to segment.
5. Select **Run segmentation**.

The fixed box covers the center 80 percent of the image after it's resized to `1024 x 1024`. Keeping the prompt fixed makes the first run repeatable. This example doesn't include controls for moving or resizing the box.

The result should show a translucent cyan mask over an object within the box. The result panel reports the following:

- Selected mask
- Predicted intersection over union (IoU)
- Mask coverage
- Mask logit range
- Model load time
- Run time

## Understand what the adapter validates

`model_catalog.json` selects `MobileSamExecuTorchAdapter` through the `mobile-sam-executorch` adapter ID. The adapter isolates MobileSAM's model-specific contract from the shared Android screen.

When you select **Load model**, the adapter checks that the configured `.pte` file exists inside the application-private model directory. The adapter loads the program, confirms that it exposes a `forward` method, and checks that the method declares the XNNPACK backend.

When you select **Run segmentation**, the application corrects the image orientation, resizes the image, and creates the image and box-prompt tensors. After ExecuTorch runs `forward`, the postprocessor checks for two `float32` outputs with shapes `[1, 3, 256, 256]` and `[1, 3]`. The postprocessor then selects the mask with the highest predicted IoU and renders the cyan overlay.

These checks confirm that the artifact matches the supplied adapter. They don't measure segmentation accuracy or guarantee that every operation uses the same optimized kernel on every phone.

## Verify local inference

Run a second image with a distinct central object and confirm that the mask changes with the input. Generated masks don't have a fixed textual output, so check that the overlay follows a plausible object boundary. Also ensure that the result panel contains finite IoU, coverage, and logit values.

Enable airplane mode or otherwise disconnect the phone from the network, then run segmentation again. The result should still appear because the APK and model artifact execute locally. Re-enable the network afterward if you need it for other applications.

Record the following information:

- The model file
- The ExecuTorch version
- The Android phone model and Android version
- The input image
- Load time
- Run time
- The result

Treat the timing as illustrative rather than a benchmark.

## What you've accomplished and what's next

You've now downloaded the validated MobileSAM program and copied it into application-private storage. You've generated and checked segmentation masks, and traced the adapter's compatibility checks and output rendering.

Next, you'll learn how to extend the application to use an Arm AI Portal model without a validated adapter.

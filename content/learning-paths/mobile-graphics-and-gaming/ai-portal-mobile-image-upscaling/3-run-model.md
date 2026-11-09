---
title: Import and run Arm AI Portal upscaling models on Android
description: Import QuickSRNetSmall, upscale a saved photo, inspect detail, and save the output before trying alternatives.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Photo Upscale adapters

An adapter is application code that connects the shared Android interface to a model task and runtime. Photo Upscale supplies an ExecuTorch adapter and three model profiles. Each profile identifies one inspected package and its tile size, scale factor, and overlap.

The model runs locally on the Android CPU. The application doesn't upload the selected photo to a server. The imported model stays in application-private storage; no model weights are included in the APK.

Start with QuickSRNetSmall because it has a small model package and low reported per-tile cost. You can use another supported model after completing the default workflow. Run the commands from the project directory in the same terminal session that you used during setup.

{{% notice Note %}}
Arm AI Portal models are hosted on Hugging Face. The `download_model.py` script uses `huggingface_hub` and connects to `https://huggingface.co` by default.
{{% /notice %}}

## Run QuickSRNetSmall with ExecuTorch

Set `MODEL_ID` to the repository ID for the default QuickSRNetSmall model:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export MODEL_ID="Arm/qai-quicksrnetsmall-int8-xnnpack-executorch-vivo-x300"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_ID = "Arm/qai-quicksrnetsmall-int8-xnnpack-executorch-vivo-x300"
  {{< /tab >}}
{{< /tabpane >}}

Download the model:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
export MODEL_FILE="$(.hf-venv/bin/python download_model.py \
  --repo-id "$MODEL_ID" \
  --print-path)"

printf 'Model file: %s\n' "$MODEL_FILE"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$MODEL_FILE = .\.hf-venv\Scripts\python.exe download_model.py `
  --repo-id "$MODEL_ID" `
  --print-path

Write-Output "Model file: $MODEL_FILE"
  {{< /tab >}}
{{< /tabpane >}}

The downloader retrieves the pinned `model.pte`, verifies its SHA-256 checksum, and copies it to `quicksr.pte`. The upstream QuickSRNetSmall and SESR-M5 programs are both named `model.pte`, so the downloader gives them distinct filenames. The application validates the selected profile by file content, not filename.

Copy the model to the phone's **Downloads** directory:

```console
adb push "$MODEL_FILE" /sdcard/Download/
```

## Copy the sample image to Android

The application repository includes `samples/photo.jpg`, a 96 × 64 copy of the RealESR-general-x4v3 package's sample street photo. It contains traffic signals, vehicle edges, poles, and road texture to inspect. The source is [Rue Bouvier, Quebec City (17)](https://commons.wikimedia.org/wiki/File:Rue_Bouvier,_Quebec_City_(17).jpg) by Wilfredor, licensed under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Attribution and the pinned source are recorded in `samples/README.md`.

Copy the image to the phone:

```console
adb push samples/photo.jpg /sdcard/Download/
```

To use a different JPEG or PNG image, replace `samples/photo.jpg` in the `adb push` command with its path. You can also skip the copy command and select an image already stored on the phone or emulator. Use a photo at most 512 × 512 pixels.

## Run photo upscaling

In Photo Upscale:

1. Keep **QuickSRNetSmall** selected.
2. Select **Add or change model** and choose `quicksr.pte` from **Downloads**.
3. Keep the application open until it reports **QuickSRNetSmall ready · ExecuTorch CPU**.
4. Select **Choose a photo** and choose `photo.jpg` from **Downloads**.
5. Select **Upscale photo**.

The importer checks the model's checksum and copies it to application-specific storage. You can delete the `.pte` from **Downloads** after import. The imported file remains until you uninstall the application or clear its storage.

The application reports tile progress, then displays the original and upscaled image, input/output dimensions, model name, runtime, and processing time. The sample must produce **96 × 64 → 384 × 256**. Four times the width and height means sixteen times as many pixels. Smaller photos are replicate-padded to one 128 × 128 tile, then cropped to the correct output size. Larger photos use overlapping tiles.

**Processing time** covers RGB preparation, every tile's inference, blending, and conversion to the output bitmap. It excludes model import, loading and the validation warm-up, photo decoding, screen rendering, and saving. It is a full-image measurement, not the Portal's per-tile latency. Treat emulator timings as functional observations, not phone benchmarks.

![Photo Upscale on an ASUS ROG Phone 6D showing the QuickSRNetSmall street-photo output, 96 by 64 input and 384 by 256 output dimensions, and a concise processing-time note in the results card.#center](images/photo-upscale-result.png "Actual phone result; 184.4 ms is one functional-test observation, not a controlled benchmark")

## Inspect detail and save the image

Select **Inspect detail**. Pinch to zoom and drag to pan, then use **Showing upscaled · switch to original** to compare the same region at the same displayed size. **Reset zoom** returns to the fitted view. Look at traffic signals, vehicle edges, textures, and tile boundaries. More pixels don't guarantee more accurate detail: the model can smooth or invent texture.

Select **Close detail**, then **Save image**. Android opens the document picker with a suggested `.png` filename. Choose a location such as **Downloads**, change the filename if needed, and select **Save**.

Open the saved PNG in an image viewer. Verify its dimensions are **384 × 256**, its orientation and colors match the source, and its detail matches the displayed output. Choose a second, visibly different photo and run again to confirm the output follows the input. For a tiled check, use a 249 × 133 input and verify a 996 × 532 output. Also check a narrow input such as 63 × 257, which must produce 252 × 1028.

If loading fails, confirm the model selector matches the downloaded repository. A checksum error means the file isn't the pinned artifact for that profile. A native-runtime error can indicate an incompatible runtime or device; record the error and device details rather than assuming support. If a photo is too large or memory is insufficient, choose a smaller photo.

## Use another supported model

Photo Upscale also supports the following Arm AI Portal model packages:

| Model | Runtime | Repository ID | Import this file | Processing profile |
| --- | --- | --- | --- | --- |
| [QuickSRNetSmall INT8](https://developer.arm.com/ai/models/hugging-face/Arm/qai-quicksrnetsmall-int8-xnnpack-executorch-vivo-x300/quicksrnetsmall-int8-pte) (default) | ExecuTorch CPU / XNNPACK | `Arm/qai-quicksrnetsmall-int8-xnnpack-executorch-vivo-x300` | `quicksr.pte` | RGB `[0,1]`, 128 × 128 → 512 × 512, 4×, 8-pixel overlap |
| [SESR-M5 INT8](https://developer.arm.com/ai/models/hugging-face/Arm/sesr-m5-int8-xnnpack-executorch-vivo-x300/sesr-m5-int8-pte) | ExecuTorch CPU / XNNPACK | `Arm/sesr-m5-int8-xnnpack-executorch-vivo-x300` | `sesr.pte` | RGB `[0,1]`, 128 × 128 → 512 × 512, 4×; app chooses 8-pixel overlap |
| [RealESR-general-x4v3 INT8](https://developer.arm.com/ai/models/hugging-face/Arm/realesr-general-x4v3-int8-xnnpack-executorch-vivo-x300/realesr-general-x4v3-int8-pte) | ExecuTorch CPU / XNNPACK | `Arm/realesr-general-x4v3-int8-xnnpack-executorch-vivo-x300` | `realesr.pte` | RGB `[0,1]`, 128 × 128 → 512 × 512, 4×, 8-pixel overlap |

To use one of these models, set `MODEL_ID` to a repository ID from the table and repeat the download and import workflow. Select its card in the horizontal model selector before importing. Swipe the selector to reveal RealESR-general-x4v3. The saved photo remains selected; the previous result is cleared. Select **Upscale photo**, inspect the result, and save it under a different filename. Switching releases the previous runtime. Returning to an imported model reloads its private copy.

The supplied profiles don't require tokenizers, projectors, or other runtime assets. They validate float32 outputs, clamp RGB values to `[0,1]`, and convert them to 8-bit RGB. INT8 describes the internal quantized computation, not the Java input/output tensor type. SESR's package doesn't document a tiling algorithm; its profile uses the app's feathered tiler. Compare seams and image quality on your own photos.

## What you've accomplished and what's next

You've imported QuickSRNetSmall, upscaled a saved photo locally on Android, inspected its detail, and saved a PNG. You can use the same workflow with SESR-M5 and RealESR-general-x4v3.

Next, you'll understand how Photo Upscale works.

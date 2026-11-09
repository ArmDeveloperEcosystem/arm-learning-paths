---
title: Understand the Photo Upscale Android application
description: Trace model profiles, checked imports, RGB tiling, ExecuTorch CPU execution, blending, detail comparison, and PNG saving.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Photo Upscale works

The screen derives from Photo Insight and retains its theme, card layouts, model selector, shared buttons, and status/results styling. `MainActivity.java` connects the Android document picker, model selector, saved photo, progress, original and output images, detail view, and save action. It moves model import, loading, image decoding, upscaling, and saving off the main Android user-interface thread so the screen remains responsive.

An adapter is the application-side integration layer between the shared Android screen and one model workflow. `ExecuTorchUpscaleAdapter.java` provides CPU photo upscaling through `UpscaleAdapter.java`. The screen supplies a bitmap and displays the returned bitmap; tensor preparation, inference, and decoding stay inside the adapter.

The adapter isn't a model executable. Gradle adds the ExecuTorch Android library when it builds the application, and its prebuilt `arm64-v8a` native runtime libraries are packaged in the Android application package (APK).

### How Photo Upscale resolves and validates the model

`ModelProfile.java` is the model registry. Each descriptor records its display name, storage ID, SHA-256 identity, input tile size, scale factor, and overlap. `models.json` records the matching upstream repository, immutable revision, source filename, and checksum for the downloader.

`ModelImporter.java` copies the document-picker URI to a temporary file and checks its SHA-256 against the selected descriptor. It rejects truncated files, the wrong model, unexpected revisions, and files above 16 MiB. Only a matching file replaces the private model copy. The original package filenames needn't be unique because identity comes from the checksum.

`ExecuTorchUpscaleAdapter.load` closes the previous module, memory-maps the selected program, checks for `forward` and `XnnpackBackend`, and runs a zero-valued validation tile. The returned tensor must be float32 `[1,3,512,512]`. This warm-up is outside the displayed processing time. Checksum and tensor validation establish package compatibility, not image quality.

### How Photo Upscale prepares image tiles

Android's `ImageDecoder` reads the saved photo with orientation metadata, requests software decoding and sRGB color, and rejects inputs above 512 × 512 before decoding pixel data. Transparent pixels are composited on white. No image is silently resized.

Each independently inspected program takes float32 `[1,3,128,128]` in RGB order with values divided by 255. INT8 quantization and dequantization are internal to the program. There is no ImageNet mean or standard-deviation normalization and no BGR conversion.

`TileMath.positions` starts at zero and advances by 120 input pixels: a 128-pixel tile with 8-pixel overlap. The final tile is anchored at the far edge. This can increase overlap at the edge. Dimensions smaller than 128 are replicate-padded. Both dimensions are handled independently, including narrow, tall photos.

### How Photo Upscale runs the ExecuTorch program

The adapter calls `Module.execute("forward", ...)` once per tile on a single background executor. Each tile returns float32 RGB `[1,3,512,512]`. It verifies the tensor type, shape, and finite pixel values. The loaded module is reused until the model changes or the activity is destroyed.

Progress counts completed tiles, not estimated remaining seconds. The adapter releases the module before loading another model; lifecycle cleanup runs on the same executor to avoid closing a module during inference.

The model program selects XNNPACK CPU execution. Kernel selection depends on CPU features, the model, and the runtime build. An SME2 label on a Portal model doesn't prove that this application used SME2 kernels. This workflow doesn't measure a kernel-level speedup.

### How Photo Upscale blends and converts output

Each non-edge tile has a linear 32-output-pixel ramp at its borders, corresponding to 8 input pixels at 4× scale. The app accumulates weighted RGB values and a weight sum, then divides each output pixel by its weight. Padding is cropped to exactly four times the input width and height.

After blending, it rejects non-finite values, clamps to `[0,1]`, multiplies by 255, and truncates to integer RGB channels, matching the reference image conversion. An opaque Android bitmap holds the result. The app doesn't add a second interpolation or sharpening pass.

### How Photo Upscale displays, measures, and saves images

The result summary names the model and shows input/output dimensions. `SystemClock.elapsedRealtimeNanos` measures the complete upscale call, from RGB preparation through tiled inference, blending, and bitmap creation. It excludes import, load/warm-up, photo decoding, rendering, and PNG saving.

`DetailView.java` draws the original or output in the same normalized scene coordinates. Pinch zoom and drag pan are retained when toggling, so you can inspect the same feature at the same displayed size. Comparing at fitted size alone can hide artifacts.

The **Save image** action opens Android's document picker with the `image/png` MIME type. The application writes the displayed bitmap to the location that you select without needing broad shared-storage permission.

### (Optional) Support another compatible model

Complete the supplied workflow before extending it. A new profile can reuse this adapter only after inspection confirms the same forward method, RGB range and layout, tensor types, static tile shape, scale, output decoding, and CPU backend. Add its pinned artifact to `models.json`, its identity and verified geometry to `ModelProfile.java`, and validate import, image quality, dimensions, switching, and saving on Android.

Use another adapter when preprocessing, methods, dynamic shapes, output decoding, or runtime requirements differ. Adapters and runtime libraries are compiled into the APK; importing a model doesn't add application code. The main workflow already supplies all three profiles and doesn't require generating code.

## What you've learned and what's next

You can now trace the application from model import through RGB tiling, ExecuTorch CPU inference, feathered blending, detail comparison, and PNG output. Use the same saved photo with each supported model to compare visual results, and validate on a physical Arm-based Android phone with the required `arm64-v8a` ABI before drawing performance conclusions.

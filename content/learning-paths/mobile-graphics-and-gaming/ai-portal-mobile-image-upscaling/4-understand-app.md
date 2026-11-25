---
title: Understand the Photo Upscale Android application
description: Review how Photo Upscale imports models, upscales image tiles with ExecuTorch, and displays and saves the result.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How image upscaling works

Image upscaling converts a low-resolution photo into a higher-resolution image. These models use patterns learned during training to predict finer detail from the input photo. Each model produces an image four times wider and taller—16 times as many pixels. The result might look sharper, but predicted detail might differ from the original scene.

## How Photo Upscale works

`MainActivity.java` handles photo selection, model import, and progress, as well as results, detail comparison, and saving. Time-consuming operations run on a background thread so that the screen stays responsive.

`UpscaleAdapter.java` defines how the screen loads a model and upscales a bitmap. `ExecuTorchUpscaleAdapter.java` implements those operations on the CPU. Gradle packages the ExecuTorch runtime in the APK. Model files are imported separately.

### How Photo Upscale imports and checks models

`ModelProfile.java` records the checksum, tile size, scale factor, and overlap of each model. `models.json` supplies the repository IDs, fixed revisions, filenames, and checksums of the downloader.

`ModelImporter.java` identifies the selected file by its SHA-256 checksum and stores a private copy. It rejects unsupported or modified files and files above 16 MiB. Importing another model replaces the active model without clearing the selected photo.

The adapter closes the previous module and loads the model. It checks for `forward` and `XnnpackBackend`, and runs a zero-valued test tile. This warm-up checks the output tensor and is excluded from the displayed processing time.

### How Photo Upscale prepares image tiles

Android `ImageDecoder` applies orientation metadata and requests sRGB color. The app rejects photos larger than 512 × 512 pixels and composites transparent pixels on white.

All three models take float32 RGB `[1,3,128,128]` tensors: one image, three color channels, and a height and width of 128 pixels. RGB values are divided by 255 to give a range of `[0,1]`. Quantized operations run inside the model.

The models require fixed-size input tiles, so the app divides larger photos into overlapping tiles. `TileMath.positions` places 128-pixel tiles at 120-pixel intervals, giving an 8-pixel overlap. The last tile meets the far edge, which can increase its overlap. If either dimension is smaller than 128, the app repeats edge pixels to fill the tile.

### How Photo Upscale runs the ExecuTorch program

The adapter calls `Module.execute("forward", ...)` once per tile. It checks that each output is float32 RGB `[1,3,512,512]` with no NaN or infinite values. Progress shows completed tiles.

XNNPACK selects CPU kernels according to the model, runtime build, and available CPU features on the phone. An SME2 label on an AI Portal model doesn't confirm that SME2 kernels ran on your phone.

### How Photo Upscale blends and converts output

Blending reduces visible joins where neighboring tiles predict different pixel values. The app blends overlapping tiles with linear weights across 32 output pixels. Borders at the image edge keep their full weight. It removes padding to produce exactly four times the input width and height.

RGB values are clamped to `[0,1]`, multiplied by 255, and truncated to integer channels in an opaque bitmap.

### How Photo Upscale displays, measures, and saves images

The result shows the model, input and output dimensions, and processing time. Timing includes RGB preparation, inference, blending, and bitmap creation. It excludes import, model loading and warm-up, photo decoding, display, and saving.

`DetailView.java` keeps the zoom and position when you switch between original and upscaled images. **Save image** writes the output as a PNG through the Android document picker, without broad storage permission.

## (Optional) How you can add support for another compatible model

A new model can reuse this adapter if its preprocessing, tensor shapes and types, scale factor, output conversion, and CPU backend match. Add its download entry to `models.json` and profile to `ModelProfile.java`. After adding the entry and profile, rebuild and test import, inference, image detail, dimensions, switching, and saving.

Models with different requirements need adapter changes or a separate adapter.

## What you've learned

You've learned how Photo Upscale imports models, upscales tiles, blends the output, and saves a PNG.

You can use the supplied application to compare supported upscaling models on an Arm-based Android phone.

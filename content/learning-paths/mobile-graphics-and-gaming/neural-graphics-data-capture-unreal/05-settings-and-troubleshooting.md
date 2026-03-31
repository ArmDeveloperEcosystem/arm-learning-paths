---
title: Capture settings and troubleshooting
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Useful capture settings

You can tune these in `NGDCRenderingSettings` and `NGDCExportSettings`:

- `UpscalingRatio`: Sets the ratio between jittered input and ground-truth output. Fractional values are supported.
- `SupersamplingRatio`: Controls quality/performance tradeoff while capturing.
- `FixedFrameRate`: Locks capture frame rate when greater than `0`.
- `CameraCutTranslationThreshold` and `CameraCutRotationThresholdDegrees`: Heuristics for marking camera cuts when needed.
- `DatasetDir` and `CaptureName`: Control output folder location and capture name.

## Recommended system specification

For smooth out-of-box capture, a representative spec is:

- RAM: 64 GB
- GPU: NVIDIA GeForce RTX 4080 (driver 572.96 or newer)
- OS: 64-bit Windows or Linux

## Troubleshooting

1. Plugin not detected:
   - Confirm plugin is under your project `Plugins/` directory.
   - Regenerate project files and rebuild.
2. Hotkeys do nothing:
   - Verify Level Blueprint has `C` wired to **Begin Capture** and `V` wired to **End Capture**.
3. Dataset folder is empty:
   - Confirm capture actually started and that export path is writable.
4. Stutter or instability:
   - Lower `SupersamplingRatio` and test again.
5. Unexpected output size:
   - Use **Standalone Game** mode instead of **New Editor Window (PIE)**.

## Result

You now have a UE 5.5 workflow to capture neural graphics datasets directly from gameplay, without setting up Vulkan SDK or emulation layers.

Use this as a repeatable data generation path for model experimentation and evaluation in your neural graphics pipeline.

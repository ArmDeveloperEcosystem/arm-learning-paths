---
title: Capture settings and troubleshooting
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Available capture settings

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

## Common issues and solutions

**Plugin not detected:**
- Confirm plugin is under your project `Plugins/` directory.
- Regenerate project files and rebuild.

**Hotkeys don't work:**
- Verify Level Blueprint has `C` wired to **Begin Capture** and `V` wired to **End Capture**.

**Dataset folder is empty:**
- Confirm capture started and that export path is writable.

**Stutter or instability:**
- Lower `SupersamplingRatio` and test again.

**Unexpected output size:**
- Use **Standalone Game** mode instead of **New Editor Window (PIE)**.

## What you've learned

You've successfully set up a workflow to capture neural graphics datasets directly from Unreal Engine 5.5 gameplay. You can now:

- Generate training data from your own game content without graphics API configuration
- Capture representative gameplay sequences with real motion and camera behavior
- Export frame datasets ready for use with Model Gym's NSS data generation pipeline
- Tune capture settings to match your specific quality and performance requirements

Use this repeatable workflow for model experimentation and evaluation in your neural graphics pipeline.

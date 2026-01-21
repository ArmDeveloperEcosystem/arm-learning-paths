---
title: Run the Android SME2 profiling pipeline (optional)
weight: 8
layout: "learningpathall"
---

## Android NDK setup (if not already installed)

The Android NDK is required to cross-compile runners for Android devices.

**Download:**  
https://developer.android.com/ndk/downloads

**Install and configure:**
```bash
# Extract the NDK (example for macOS/Linux)
unzip android-ndk-r26d-darwin.zip -d ~/android-sdk/

# Set environment variable (add to ~/.zshrc or ~/.bashrc to persist)
export ANDROID_NDK=~/android-sdk/android-ndk-r26d
```

Verify:
```bash
ls $ANDROID_NDK/toolchains/llvm/prebuilt/*/bin/aarch64-linux-android*-clang
```

Expected: Clang compiler paths for aarch64 (arm64).

## Quick start (hands-on)
```bash
# Device check
adb devices
adb shell getprop ro.product.cpu.abi
# Optional: confirm SME2 capability
adb shell "cat /proc/cpuinfo | grep -i sme2 || getprop ro.cpu.extensions"

# Build Android runners (requires ANDROID_NDK to be set)
export ANDROID_NDK=~/android-sdk/android-ndk-r26d  # or your path
bash scripts/build_runners.sh

# Create an Android config
cp configs/templates/android_template.json configs/android.json
# Edit configs/android.json:
# - set "model" to: "models/mobilenet_v3_small_fp16.pte"

# Run on device + pull ETDump traces back
python scripts/android_pipeline.py --config configs/android.json
```

## Detailed steps (context)
- Keep runs per variant (`runs/android_sme2_on`, `runs/android_sme2_off`).
- Ensure device is arm64 and SME2-capable; otherwise expect smaller or no speedup.
- Capture logs and ETDump outputs for comparison with Mac runs.
- If SME2 is not advertised in the capability check, expect no SME2 delta and treat the run as a workflow sanity.

## Validation
- Check logs under `runs/android_sme2_on/logs`.
- Confirm results directory contains metrics and ETDump traces.
- If SME2 gains are small, verify the device’s SME2 support and that the runner was built with SME2 enabled.

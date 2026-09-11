---
title: Build and validate the integration
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the patch series

Confirm that the patches were applied to the baseline XNNPACK revision in the expected order:

```bash
git log --oneline -4
```

The commit subjects should be:

```output
Dispatch QD8 F16 QC4W through KAI SME2
Pack QD8 LHS for KAI SME2
Support transposed KAI QC4W weights
Prepare QD8 F16 QC4W SME2 kernel
```

Regenerate the microkernel source lists. This command must complete without duplicate-microkernel messages:

```bash
python3 tools/update-microkernels.py
git diff --check
```

## Build for Android

This example uses Android NDK r29. Set the NDK path for your environment:

```bash
export ANDROID_NDK=/tools/android-ndk-r29

scripts/build-android-arm64.sh \
  -DXNNPACK_ENABLE_KLEIDIAI=ON \
  -DXNNPACK_BUILD_BENCHMARKS=OFF \
  -DXNNPACK_BUILD_TESTS=ON
```

Build the fully connected operator test:

```bash
cmake --build build/android/arm64-v8a \
  --target fully-connected-nc-test -- -j"$(nproc)"
```

## Run the correctness tests on an SME2 device

Copy the test binary to an Android device that reports SME2 support:

```bash
adb push build/android/arm64-v8a/test/operators/fully-connected-nc-test \
  /data/local/tmp/xnnpack-fc-test

adb shell "chmod 755 /data/local/tmp/xnnpack-fc-test"

adb shell "/data/local/tmp/xnnpack-fc-test \
  --gtest_filter='FULLY_CONNECTED_NC_QD8_F16_QC4W.*'"
```

Expected result:

```output
[==========] Running 15 tests from 1 test suite.
[  PASSED  ] 15 tests.
```

The suite covers normal and small batches, min/max clamp ranges, input and output stride, optional bias, transposed weights, and weights-cache reuse.

## Check the fallback build

The KAI path must not break builds where KleidiAI is disabled. On a development host, run:

```bash
bazel build //:packing --define=xnn_enable_kleidiai=false
```

This validates that the `XNN_ENABLE_KLEIDIAI` guards preserve the non-KleidiAI configuration.



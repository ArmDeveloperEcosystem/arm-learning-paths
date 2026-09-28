---
title: Build and validate the integration
description: Build the KleidiAI integration in XNNPACK for Android, run correctness tests, and check the build with KleidiAI disabled.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the patch series

With all four patches applied, run the commands from the XNNPACK checkout directory on your development host. You'll build on the host, then use `adb` to run the correctness tests on the Android device.

Confirm that the patches were applied to the baseline XNNPACK revision in the expected order:

```bash
git log --oneline -4
```

The output is similar to:

```output
Dispatch QD8 F16 QC4W through KAI SME2
Pack QD8 LHS for KAI SME2
Support transposed KAI QC4W weights
Prepare QD8 F16 QC4W SME2 kernel
```

The example output lists commit subjects. Your output will also include commit identifiers.

Regenerate the microkernel source lists:

```bash
python3 tools/update-microkernels.py
git diff --check
```

Depending on your Python version, you might see `DeprecationWarning: codecs.open() is deprecated. Use open() instead.` from the generator. This warning alone doesn't indicate a failure. Continue if the script completes successfully without duplicate microkernel messages and `git diff --check` passes.

## Build the test binary for Android

To build the test binary for Android, install the Android Native Development Kit (Android NDK) r29.

From the XNNPACK checkout, set `WORKSPACE` to its parent directory so that the NDK is installed alongside XNNPACK:

```bash
export WORKSPACE="$(dirname "$PWD")"
```

Download and extract the NDK for your development host:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash" >}}
cd "$WORKSPACE"
wget https://dl.google.com/android/repository/android-ndk-r29-linux.zip
unzip android-ndk-r29-linux.zip
  {{< /tab >}}
  {{< tab header="macOS" language="bash" >}}
cd "$WORKSPACE"
wget https://dl.google.com/android/repository/android-ndk-r29-darwin.zip
unzip android-ndk-r29-darwin.zip
  {{< /tab >}}
{{< /tabpane >}}

Both archives extract to `android-ndk-r29`. Set `ANDROID_NDK` to that directory, then return to the XNNPACK checkout and build with KleidiAI and tests enabled:

```bash
export ANDROID_NDK="$WORKSPACE/android-ndk-r29"
cd "$WORKSPACE/XNNPACK"

scripts/build-android-arm64.sh \
  -DXNNPACK_ENABLE_KLEIDIAI=ON \
  -DXNNPACK_BUILD_BENCHMARKS=OFF \
  -DXNNPACK_BUILD_TESTS=ON
```

Build the fully connected operator test:

```bash
cmake --build build/android/arm64-v8a \
  --target fully-connected-nc-test -- parallel
```

## Run the correctness tests on an SME2 device

From the development host, copy the test binary to an [Android device with SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices). Make the binary executable, and run the filtered correctness suite:

```bash
adb push build/android/arm64-v8a/test/operators/fully-connected-nc-test \
  /data/local/tmp/xnnpack-fc-test

adb shell "chmod 755 /data/local/tmp/xnnpack-fc-test"

adb shell "/data/local/tmp/xnnpack-fc-test \
  --gtest_filter='FULLY_CONNECTED_NC_QD8_F16_QC4W.*'"
```

The expected output is:

```output
[==========] Running 15 tests from 1 test suite.
[  PASSED  ] 15 tests.
```

The suite covers the following:

- Normal and small batches
- Minimum and maximum clamp ranges
- Input and output stride
- Optional bias
- Transposed weights
- Weights-cache reuse

## Check the fallback build

Ensure that the KleidiAI path doesn't break builds where KleidiAI is disabled. On a development host, run:

```bash
bazel build //:packing --define=xnn_enable_kleidiai=false
```

This validates that the `XNN_ENABLE_KLEIDIAI` guards preserve the non-KleidiAI configuration.

## What you've accomplished

You've built the patched Android test binary, passed the filtered QD8 F16 QC4W correctness suite, and built the packing target with KleidiAI disabled.

You can extend the workflow and patches to integrate a KleidiAI SME2 microkernel for your own use case into an existing AI inference framework.

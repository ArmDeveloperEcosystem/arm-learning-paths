---
title: Set up the Android build environment
description: Set up the Android SDK and NDK, verify SVE2 and SME support, and build a KleidiCV Gaussian blur example for an Arm-based Android device.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you'll build

KleidiCV is Arm's high-performance image-processing library for AArch64. It
provides a C API for operations such as color conversion, filtering, morphology,
resizing, and geometric transforms. Optimized implementations target Neon, SVE2,
SME, and SME2.

You'll explore KleidiCV's Gaussian blur filter by building a standalone SME
example and a performance explorer that calls the Neon, SVE2, and SME
implementations directly. You can verify their output and compare
performance under controlled conditions.

## Clone KleidiCV

Clone KleidiCV and check out the 26.06 release:

```bash
git clone https://gitlab.arm.com/kleidi/kleidicv.git
cd kleidicv
git checkout --detach refs/tags/26.06
```

You'll use the standalone Gaussian blur example in
`examples/extract_one_operation` from the 26.06 release, then use
a performance explorer for comparing the implementations.

## Configure the Android SDK and NDK

{{% notice Note %}}
Use an x86_64 (Intel or AMD) Ubuntu or Debian host.
Google distributes the Android SDK command-line tools and NDK only as x86_64
Linux builds, so they don't run on an Arm-based Linux machine.
{{% /notice %}}

Install the host packages that are needed to build the examples:

```bash
sudo apt update
sudo apt install openjdk-17-jdk openjdk-17-jre cmake ninja-build unzip
```

Download the Linux command line tools package and install Android SDK
Platform-Tools and Build Tools. The following commands query the current package
name from the [Android Studio downloads](https://developer.android.com/studio)
page, so they keep working as Google publishes new command-line tools:

```bash
export ANDROID_HOME="$HOME/android-sdk"

# Find the current Linux command-line tools package name, then download it
CLT_ZIP=$(curl -s https://developer.android.com/studio \
  | grep -oE 'commandlinetools-linux-[0-9]+_latest.zip' | head -1)
wget "https://dl.google.com/android/repository/$CLT_ZIP"

# Extract, then move the archive's cmdline-tools directory into place as "latest"
mkdir -p "$ANDROID_HOME/cmdline-tools"
unzip -q "$CLT_ZIP" -d "$ANDROID_HOME/cmdline-tools"
mv "$ANDROID_HOME/cmdline-tools/cmdline-tools" "$ANDROID_HOME/cmdline-tools/latest"

$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager \
  --sdk_root=$ANDROID_HOME --licenses
$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager \
  --sdk_root=$ANDROID_HOME \
  "platform-tools" "build-tools;36.0.0"
```

The archive contains a top-level `cmdline-tools` directory. Extract the directory into
`$ANDROID_HOME/cmdline-tools` and rename it to `latest` so that `sdkmanager`
resolves to `$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager`, the path the
following commands expect.

If you prefer to choose a version manually, you can instead download the
command line tools package from the
[Android Studio downloads](https://developer.android.com/studio) page in a
browser and extract the package with the same `mkdir`, `unzip`, and `mv` steps.

Accept the SDK license prompts. Next, install Android NDK r29, which is the
first NDK release with SME support. Installing the NDK with `sdkmanager` places
it under `$ANDROID_HOME/ndk/<version>` and avoids a separate manual download.

List the available `ndk;` packages, then install an r29 (or later) build:

```bash
$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --sdk_root=$ANDROID_HOME --list \
  | grep 'ndk;'
$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager \
  --sdk_root=$ANDROID_HOME "ndk;29.0.14206865"
```

The installed `platform-tools` package provides `adb`. Set
`ANDROID_NDK_HOME` to the installed NDK directory and add `adb` to your path:

```bash
export ANDROID_NDK_HOME="$(ls -d "$ANDROID_HOME"/ndk/* | sort -V | tail -1)"
export PATH="$ANDROID_HOME/platform-tools:$PATH"
echo "Using NDK: $ANDROID_NDK_HOME"
adb version
```
Resolving the directory with a glob avoids hard-coding the exact build number.

If you prefer a standalone archive, you can instead download and unzip an NDK
at r29 or later from
[Android NDK downloads](https://developer.android.com/ndk/downloads/) and point
`ANDROID_NDK_HOME` at the extracted `android-ndk-<version>` directory.

The output is similar to:

```output
Using NDK: /home/ubuntu/android-sdk/ndk/29.0.14206865
Android Debug Bridge version 1.0.41
Version 37.0.1-15733141
Installed as /home/ubuntu/android-sdk/platform-tools/adb
Running on Linux 6.8.0-137-generic (x86_64)
```

The ADB version, installation path, and host architecture vary with your
Linux distribution and installation method.

Confirm that ADB can see the target device:

```bash
adb devices
```

## Verify support for SVE2 and SME2

The test performance results in this Learning Path were collected on a
[vivo X300](https://www.vivo.com.cn/vivo/x300/) powered by the
[MediaTek Dimensity 9500](https://www.mediatek.com/products/smartphones/mediatek-dimensity-9500).

This Armv9.3 processor supports SVE2, SME, and SME2. You can use another
Arm-based Android device if it supports SVE2 and SME.

Confirm that the target device reports both SVE2 and SME:

```bash
adb shell 'grep -m1 "^Features" /proc/cpuinfo'
```

The output is similar to:

```output
Features    : fp asimd aes pmull sha1 sha2 crc32 atomics sve sve2 sme
```

Feature lists differ between devices, but this line must include both `sve2`
and `sme`. The performance explorer selects implementations explicitly, so
it doesn't use KleidiCV runtime dispatch. Run the SME binary only on a CPU
that supports SME.

## Build the Android targets

Configure CMake for 64-bit Arm Android and build the example target:

```bash
cmake -S examples/extract_one_operation \
      -B build/extract-android \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_TOOLCHAIN_FILE="$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake" \
      -DANDROID_ABI=arm64-v8a \
      -DANDROID_PLATFORM=android-21 \
      -DANDROID_STL=c++_static

cmake --build build/extract-android --target example_usage -j"$(nproc)"
```

The output is `build/extract-android/example_usage`.

## What you've accomplished and what's next

You've created the Android environment and built a KleidiCV Gaussian blur example.

Next, you'll run the minimal Gaussian blur example on the device.

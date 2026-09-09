---
title: Set up the Android build environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get KleidiCV

Clone KleidiCV and check out the `26.06` release:

```bash
git clone https://gitlab.arm.com/kleidi/kleidicv.git
cd kleidicv
git checkout --detach refs/tags/26.06
```

Steps 1 and 2 use the standalone Gaussian blur example in
`examples/extract_one_operation` from the `26.06` release. Step 3 introduces
a performance explorer for comparing the implementations.

## Configure the Android SDK and NDK

Install the host packages needed to build the examples:

```bash
sudo apt update
sudo apt install openjdk-17-jdk openjdk-17-jre cmake ninja-build unzip
```

Download the Linux *Command line tools* package from
[Android Studio downloads](https://developer.android.com/studio), then extract
it and install Android SDK Platform-Tools and Build Tools:

```bash
export ANDROID_HOME="$HOME/android-sdk"
mkdir -p "$ANDROID_HOME/cmdline-tools/latest"
unzip commandlinetools-linux-*.zip -d "$ANDROID_HOME/cmdline-tools/latest"

"$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" \
  --sdk_root="$ANDROID_HOME" --licenses
"$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" \
  --sdk_root="$ANDROID_HOME" \
  "platform-tools" "build-tools;36.0.0"
```

Accept the SDK license prompts. Download and extract Android NDK r29, or a
later NDK with SME support, from
[Android NDK downloads](https://developer.android.com/ndk/downloads/).
The `platform-tools` package installed above provides `adb`. Set
`ANDROID_NDK_HOME` to the extracted NDK directory and add `adb` to your path:

```bash
export ANDROID_NDK_HOME=/path/to/android-ndk-r29
export PATH="$ANDROID_HOME/platform-tools:$PATH"
adb version
```

The output is similar to:

```output
Android Debug Bridge version 1.0.41
Version 34.0.4-debian
Installed as /usr/lib/android-sdk/platform-tools/adb
Running on Linux 6.8.0-137-generic (x86_64)
```

The ADB version, installation path, and host architecture vary with your
Linux distribution and installation method.

Confirm that ADB can see the target device:

```bash
adb devices
```

## Reference test device

The performance results in this Learning Path were collected on a
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
it does not use KleidiCV runtime dispatch. Run the SME binary only on a CPU
that supports SME.

## Build the Android targets

Configure CMake for 64-bit Arm Android and build both example targets:

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

Next, run the minimal Gaussian blur example on the device.

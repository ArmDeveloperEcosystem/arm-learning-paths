---
title: Set up the SME2 environment
description: Build and run the SME2 LUTI examples natively on macOS or cross-compile them for an Android device with SME2 support.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose an SME2 execution environment

You can run the examples using one of the following routes:

- Build and run natively on an arm64 macOS® device with an M4 processor or later
- Cross-compile on macOS or Linux and run on an Android™ phone with SME2 support

See the [list of devices with native SME2 support](https://learn.arm.com/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices) before selecting a target device.

The examples use recent Arm C Language Extensions (ACLE) intrinsics and SME2 assembly syntax. Use Homebrew LLVM Clang 22 or later for native macOS builds. Android builds use the Clang 21 toolchain supplied with NDK r29, or native Clang 21 on an AArch64 Linux host.

## Set up native macOS development

Confirm that the system uses the `arm64` architecture:

```bash
uname -m
```

The expected output is:

```output
arm64
```

Check that SME2 is available to applications and inspect the maximum streaming vector length (SVL):

```bash
sysctl -n hw.optional.arm.FEAT_SME2
sysctl -n hw.optional.arm.sme_max_svl_b
```

The first command must print `1`. The second command reports the maximum SVL in bytes. For example, `64` bytes corresponds to an SVL of 512 bits.

Install Homebrew LLVM and confirm its version:

```bash
brew install llvm
/opt/homebrew/opt/llvm/bin/clang --version
```

The Makefile selects Homebrew LLVM at `/opt/homebrew/opt/llvm` when it is installed.
Otherwise, it falls back to Apple Clang from the active Xcode Command Line Tools.

## Set up Android cross-compilation

The build host does not need SME2 support. The Android device that runs the
LUTI examples does. Install the compiler tools on your macOS or Linux host.

The Makefile selects the compiler and linker automatically, so the same
build commands work on AArch64 and x86-64 Linux.

To run the LUTI examples codes install Android Native Development Kit (Android NDK):
Install Android Native Development Kit (Android NDK) r29:

{{< tabpane code=true >}}
  {{< tab header="macOS host" language="bash">}}
brew install wget
mkdir -p "$HOME/Library/Android"
cd "$HOME/Library/Android"
wget https://dl.google.com/android/repository/android-ndk-r29-darwin.zip
unzip android-ndk-r29-darwin.zip
  {{< /tab >}}
  {{< tab header="Linux host" language="bash">}}
sudo apt update
sudo apt install build-essential wget unzip
cd "$HOME"
wget https://dl.google.com/android/repository/android-ndk-r29-linux.zip
unzip android-ndk-r29-linux.zip
  {{< /tab >}}
{{< /tabpane >}}

Set `NDK_PATH` and `ANDROID_NDK_HOME` so the Makefile can locate the NDK:

{{< tabpane code=true >}}
  {{< tab header="macOS host" language="bash">}}
export NDK_PATH="$HOME/Library/Android/android-ndk-r29"
export ANDROID_NDK_HOME="$NDK_PATH"
  {{< /tab >}}
  {{< tab header="Linux host" language="bash">}}
export NDK_PATH="$HOME/android-ndk-r29"
export ANDROID_NDK_HOME="$NDK_PATH"
  {{< /tab >}}
{{< /tabpane >}}

Install Android Debug Bridge (`adb`) if it isn't already available:

{{< tabpane code=true >}}
  {{< tab header="macOS host" language="bash">}}
brew install android-platform-tools
  {{< /tab >}}
  {{< tab header="Linux host" language="bash">}}
sudo apt install adb
  {{< /tab >}}
{{< /tabpane >}}

Enable developer options and USB debugging on the Android phone, connect it to the host, and accept the debugging prompt on the phone. Verify the connection:

```bash
adb devices -l
```

Confirm that the device uses the `arm64-v8a` application binary interface (ABI):

```bash
adb shell getprop ro.product.cpu.abi
```

The expected output is:

```output
arm64-v8a
```

You can also inspect the CPU feature list:

```bash
adb shell "grep -m1 '^Features' /proc/cpuinfo"
```

The executable performs the definitive runtime check. If SME2 isn't available to Android applications, it prints `SKIP: No support for SME2 on this device.` The program exits successfully without running either set of examples. You can still disassemble the executable on the build host.

## Download and explore the code examples

Download the source and build files into a new `code` directory:

```bash
BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/mobile-graphics-and-gaming/luti

mkdir code
cd code
for FILE in \
  Makefile \
  example_1_luti_sme2.c \
  luti_sme2_programming.c \
  luti_sme2_programming_test.c; do
  wget -q "$BASE_URL/code/$FILE" -O "$FILE"
done
```

The directory contains these source and build files:

```text
code/
├── Makefile
├── example_1_luti_sme2.c
├── luti_sme2_programming.c
└── luti_sme2_programming_test.c
```

## Build and run on macOS

From the `code` directory, clean previous outputs and build the native executable:

```bash
make clean
make
```

Running `make macos` performs the same native build explicitly. Both commands
use `-march=native+sme2+nosve2+nosve`. The `+nosve2+nosve` modifiers prevent
the compiler from emitting non-streaming SVE or SVE2 instructions in the
macOS executable.

Run the introductory plain C and SME2 comparison:

```bash
./sme2_luti
```

Run the additional LUTI programming examples:

```bash
./sme2_luti --learning
```

## Build and run on Android

From the `code` directory, prepare the tools and cross-compile for Android.
Use the same commands on macOS and Linux:

Run `make setup-android` once after installing the NDK. On macOS and x86-64 Linux, this checks the installed NDK compiler. On AArch64 Linux, it also installs any missing LLVM tools. Then build the executable:

```bash
make setup-android
make clean
make android
```

Connect your Android device to your development machine using a cable.
Approve the connection on your phone and use `adb` to copy the executable to `/data/local/tmp/sme2_luti_android`:

```bash
adb push sme2_luti_android /data/local/tmp/sme2_luti_android
```

Make the executable runnable and start it from the host:

```bash
adb shell chmod 755 /data/local/tmp/sme2_luti_android
adb shell /data/local/tmp/sme2_luti_android
```

Run the additional LUTI programming examples with:

```bash
adb shell /data/local/tmp/sme2_luti_android --learning
```

## What you've accomplished and what's next

You've prepared a compatible Clang compiler, verified an SME2-capable target,
and built the same executable for native macOS or AArch64 Android.

Next, you'll use `example_1_luti_sme2.c` to compare plain C shifts, masks, and scalar lookups with SME2 `LUTI2` expansion and matrix accumulation.
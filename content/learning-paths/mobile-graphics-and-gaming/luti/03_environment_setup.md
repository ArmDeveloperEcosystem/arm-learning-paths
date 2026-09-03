---
title: Set up the SME2 environment
description: Build and run the SME2 LUTI examples natively on macOS or cross-compile them for an Android device with SME2 support.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose an SME2 execution environment

You can run the examples using one of the following route:

- Build and run natively on an arm64 macOS® device with an M4 processor or later
- Cross-compile on macOS or Linux and run on an Android™ phone with SME2 support

See the [list of devices with native SME2 support](https://learn.arm.com/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices) before selecting a target device.

The examples prefer LLVM Clang 22 or later because they use recent Arm C Language Extensions (ACLE) intrinsics and SME2 assembly syntax. The Makefile checks the appropriate compiler version before building.

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

The Makefile selects Homebrew LLVM when it is installed. Otherwise, it falls
back to Apple Clang from the active Xcode Command Line Tools.

## Set up Android cross-compilation
To run the LUTI examples codes on Android, install Android Native Development Kit (Android NDK):

{{< tabpane code=true >}}
  {{< tab header="macOS host" language="bash">}}
wget https://dl.google.com/android/repository/android-ndk-r29-darwin.zip
unzip android-ndk-r29-darwin.zip
  {{< /tab >}}
  {{< tab header="Linux host" language="bash">}}
wget https://dl.google.com/android/repository/android-ndk-r29-linux.zip
unzip android-ndk-r29-darwin.zip
  {{< /tab >}}
{{< /tabpane >}}

For easier access and execution of Android NDK tools, add these to the PATH and set the NDK_PATH variable:
{{< tabpane code=true >}}
  {{< tab header="macOS host" language="bash">}}
export NDK_PATH=$HOME/Library/Android/android-ndk-r29/
export ANDROID_NDK_HOME=$NDK_PATH
  {{< /tab >}}
  {{< tab header="Linux host" language="bash">}}
export NDK_PATH=$HOME/Android/android-ndk-r29/
export ANDROID_NDK_HOME=$NDK_PATH
  {{< /tab >}}
{{< /tabpane >}}

Install Android Debug Bridge (`adb`) if it isn't already available:

{{< tabpane code=true >}}
  {{< tab header="macOS host" language="bash">}}
brew install android-platform-tools
  {{< /tab >}}
  {{< tab header="Linux host" language="bash">}}
sudo apt update
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

The executable performs the definitive runtime check. If SME2 isn't available to Android applications, it prints `SKIP: No support for SME2 on this device; SME2 tests were not run.`

## Download and explore the code examples

__[!REVIEW - ADD THE PUBLIC CODE-EXAMPLE ARCHIVE URL BEFORE PUBLISHING]__

Download and extract the published code-example archive, then change to its `code` directory.

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

From the same `code` directory, cross-compile for Android:

```bash
make clean
make android
```
Connect your Android device to your development machine using a cable. 
Approve the connection on your phone and use adb to copies the executable to `/data/local/tmp/sme2_luti_android`:

```bash
adb push sme2_luti_android /data/local/tmp/sme2_luti_android
```

Start a new shell to access the device’s system from your development machine and runs the executable:

```
adb shell
./data/local/tmp/sme2_luti_android
```

Run the additional LUTI programming examples with:

```bash
./data/local/tmp/sme2_luti_android --learning
```

## What you've accomplished and what's next

You've prepared a compatible Clang compiler, verified an SME2-capable target,
and built the same executable for native macOS or AArch64 Android.

Next, you'll use `example_1_luti_sme2.c` to compare plain C shifts, masks, and scalar lookups with SME2 `LUTI2` expansion and matrix accumulation.
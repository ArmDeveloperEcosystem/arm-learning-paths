---
title: Set up the SME2 environment
description: Set up the macOS or Android toolchain to build and run LUTI SME2 examples and verify that your device supports SME2.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose an SME2 execution environment

You can run the examples using one of the following routes:

- Build and run natively on an arm64 macOS device with an M4 processor or later
- Cross-compile on macOS or Linux and run on an Android phone with SME2 support

See the [list of devices with native SME2 support](https://learn.arm.com/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices) before selecting a target device.

The examples use recent Arm C Language Extensions (ACLE) intrinsics and SME2 assembly syntax. Use Homebrew LLVM Clang 22 or later for native macOS builds. Android cross-compilation requires host LLVM Clang 22 and Android NDK r29.

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

The output is similar to:

```output
1
64
```

The first command must print `1`. The second command reports the maximum SVL in bytes. For example, `64` bytes corresponds to an SVL of 512 bits.

If needed, install Homebrew LLVM:

```bash
brew install llvm
```

Confirm the version:

```bash
/opt/homebrew/opt/llvm/bin/clang --version
```

The output includes text similar to:

```output
Homebrew clang version 22.1.7
Target: arm64-apple-darwin27.0.0
```

The Makefile uses Homebrew LLVM at `/opt/homebrew/opt/llvm`.

## Set up Android cross-compilation

The build host does not need SME2 support. The Android device that runs the
LUTI examples does. Install the compiler tools on your macOS or Linux host.

Install LLVM 22 on the build host. On macOS, use Homebrew LLVM. The Linux commands below target Ubuntu 24.04 LTS on either x86-64 or AArch64 and use the [LLVM APT packages](https://apt.llvm.org/).

{{< tabpane code=true >}}
  {{< tab header="macOS host" language="bash">}}
brew install llvm
"$(brew --prefix llvm)/bin/clang" --version
  {{< /tab >}}
  {{< tab header="Ubuntu 24.04 host" language="bash">}}
sudo apt update
sudo apt install ca-certificates wget lsb-release software-properties-common gnupg
wget -O llvm.sh https://apt.llvm.org/llvm.sh
sudo bash llvm.sh 22
sudo apt install llvm-22
clang-22 --version
  {{< /tab >}}
{{< /tabpane >}}

Check that Clang reports version 22 or above.

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

If SME2 isn't available to the device, the examples will skip at runtime and exit successfully.

## Download and explore the code examples

Download the source and build files into a new `code` directory. Run these commands from a working directory of your choice:

```bash
BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/mobile-graphics-and-gaming/luti

mkdir code
cd code
for FILE in \
  Makefile \
  example_1_luti_decoding.c \
  example_1_luti_decoding_runner.c \
  example_2_luti_programming.c \
  example_2_luti_programming_test.c; do
  wget "$BASE_URL/code/$FILE" -O "$FILE" || exit 1
done
```

After the download completes, the `code` directory contains these source and build files:

```output
code/
├── Makefile
├── example_1_luti_decoding.c
├── example_1_luti_decoding_runner.c
├── example_2_luti_programming.c
└── example_2_luti_programming_test.c
```

## What you've accomplished and what's next

You've prepared a compatible Clang compiler, verified an SME2-capable target,
and downloaded the source files for the standalone examples.

Next, you'll use `example_1_luti_decoding.c` to compare plain C shifts, masks, and scalar lookups with SME2 `LUTI2` expansion and matrix accumulation.

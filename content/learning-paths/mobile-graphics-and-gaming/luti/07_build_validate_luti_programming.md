---
title: Build and validate the LUTI programming examples
description: Build and run the LUTI4 and two-stage LUTI examples, then validate their output against reference results.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build and validate the examples

You've inspected how the examples apply the four-step LUTI method to FP16
FMOPA and two-stage SDOT kernels. Now build both examples and validate their
results against the reference implementations.

### Build and run on macOS

Build and run the executable on an SME2-supported device:

```bash
make example_2_luti_programming
./example_2_luti_programming
```

### Cross-compile the examples and run on Android

On macOS or Linux, build the AArch64 Android executable with LLVM 22 and the NDK r29 installation selected by `ANDROID_NDK_HOME`:

```bash
make example_2_luti_programming_android
```

With an Android device connected through `adb`, push the executable to the device:

```bash
adb push example_2_luti_programming_android /data/local/tmp/example_2_luti_programming_android
```

Open an `adb` shell, make the file executable, and run it:

```bash
adb shell
cd /data/local/tmp
chmod 755 example_2_luti_programming_android
./example_2_luti_programming_android
```

After it finishes, enter `exit` to return to the build host's shell.

The executable performs the definitive runtime check. If SME2 isn't available, it prints `SKIP: No support for SME2 on this device.`
The program exits successfully without running either set of examples.
You can still disassemble the executable on the build host.

### Check the result

In the output, `SVL` is the streaming vector length in bits. `VL_b` is the
number of byte elements (`SVL / 8`), `VL_h` is the number of half-word
elements (`SVL / 16`), and `VL_s` is the number of 32-bit word elements
(`SVL / 32`).

The expected output is:

```output
FP16 LUTI4 + FMOPA test (M = VL_s, K = 2, N = 4 * VL_s)
PASS
LUTI4 -> LUTI2 -> SDOT test (M = 1, K = N = VL_b)
PASS
```

Each `PASS` confirms that the kernel matches the reference result.

## What you've accomplished and what's next

You've built the LUTI4 and two-stage LUTI examples and confirmed that both
kernels match their reference results.

Next, you'll compare the ZT0-based LUTI path with Z-register table forms and
SME2.1 strided destination groups.

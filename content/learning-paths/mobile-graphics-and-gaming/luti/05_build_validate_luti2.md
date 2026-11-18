---
title: Build and validate the LUTI2 decoding example
description: Build and run the first LUTI2 example, compare its results with plain C, and inspect the generated SME2 instructions.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build and validate the example

You've inspected how `code/example_1_luti_decoding.c` implements the same calculation in
plain C and with SME2 LUTI2. Now build the complete example and verify that both
implementations produce the same output.

Run the following commands from the `code` directory.

### Build and run on macOS

Build and run the executable on an SME2-supported device:

```bash
make example_1_luti_decoding
./example_1_luti_decoding
```

### Cross-compile and run on Android

On macOS or Linux, use LLVM 22 and the NDK r29 installation selected by `ANDROID_NDK_HOME`. The build host doesn't need SME2 support.

Build the standalone Android executable:

```bash
make example_1_luti_decoding_android
```

With an Android device connected through `adb`, push the executable to the device:

```bash
adb push example_1_luti_decoding_android /data/local/tmp/example_1_luti_decoding_android
```

Open an `adb` shell, make the file executable, and run it:

```bash
adb shell
cd /data/local/tmp
chmod 755 example_1_luti_decoding_android
./example_1_luti_decoding_android
```

After running the file, enter `exit` to return to the build host's shell.

### Check the result

On an SME2-capable device, the program prints the matrix shape, lookup table, decoded right-hand side (RHS) samples, and a matrix preview. 

For a 512-bit SVL, the output begins with:

```output
SVL = 512 bits; matrix shape M=16, K=4, N=64
2-bit LUT mapping:
bits  idx  signed  raw byte
 00   0      -3    0xFD
 01   1      -1    0xFF
 10   2       1    0x01
 11   3       3    0x03
```

The RHS decoding preview and C matrix preview follow. The final validation line is similar to:

```output
PASS: LUTI2 SME2 matches plain C matmul.
```

If SME2 is unavailable, the runner exits without performing the calculations:

```output
SKIP: No support for SME2 on this device.
```

A `SKIP` result doesn't validate the calculation. You can still inspect the generated instructions on the build host.

## Inspect the generated SME2 instructions

For the native macOS executable, run:

```bash
make disassemble-example-1
```

For the Android executable, run the following command on the macOS or Linux build host:

```bash
make disassemble-example-1-android
```

The Makefile selects the host's LLVM disassembler and displays only LUTI2 and `SMOPA` instructions. Disassembly doesn't require SME2 hardware. 

The output is similar to:

```output
100000cec: c08c8024     luti2 { z4.b - z7.b }, zt0, z1[0]
100000cf0: a0840000     smopa za0.s, p0/m, p0/m, z0.b, z4.b
100000cf4: a0850001     smopa za1.s, p0/m, p0/m, z0.b, z5.b
100000cf8: a0860002     smopa za2.s, p0/m, p0/m, z0.b, z6.b
100000cfc: a0870003     smopa za3.s, p0/m, p0/m, z0.b, z7.b
```

Addresses vary by build. Confirm that one LUTI2 is followed by four `SMOPA` instructions targeting `ZA0` through `ZA3`.

## What you've accomplished and what's next

You've built the first example, compared the plain C and SME2 results, and
confirmed that the generated code contains LUTI2 followed by four `SMOPA`
instructions.

Next, you'll learn to program LUTIs through practical SME2 examples.

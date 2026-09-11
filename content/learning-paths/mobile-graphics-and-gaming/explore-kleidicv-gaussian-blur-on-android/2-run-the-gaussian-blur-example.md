---
title: Run the standalone SME Gaussian blur example
description: Push and run the standalone SME Gaussian blur example on an Android device and confirm the filter output with Android Debug Bridge.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the Gaussian blur example

`examples/extract_one_operation/example_usage.c` creates a 20x20,
single-channel image containing a white vertical line on a black background.
It calls `sme_gaussian_blur_u8` with a 15x15 Gaussian kernel and
`KLEIDICV_BORDER_TYPE_REFLECT`, then prints the output pixel values.

The companion CMake project builds `sme_gaussian_blur` from the SME Gaussian
blur source and its small C API wrapper. It uses `-march=armv9-a+sme`, rather
than linking the full KleidiCV library or using runtime dispatch.

## Push and run the binary

Push the binary to a writable directory on the device:

```bash
adb push build/extract-android/example_usage /data/local/tmp/
adb shell chmod 755 /data/local/tmp/example_usage
adb shell /data/local/tmp/example_usage
```

Before the filter runs, every input row contains one white pixel, `255`, at
column 10 and zeros elsewhere. The 20 input rows are identical. The first
three rows are as follows:

```output
0  0  0  0  0  0  0  0  0  0  255  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0  255  0  0  0  0  0  0  0  0  0
0  0  0  0  0  0  0  0  0  0  255  0  0  0  0  0  0  0  0  0
```

The program prints 20 identical pixel rows. The first
three rows of the output are similar to:

```output
Raw pixel values for the blurred output:
0  0  0  1  3  6  12  20  30  36  40  36  30  20  12  6  3  1  0  0
0  0  0  1  3  6  12  20  30  36  40  36  30  20  12  6  3  1  0  0
0  0  0  1  3  6  12  20  30  36  40  36  30  20  12  6  3  1  0  0
```

The original white line is at column 10. The 15x15 Gaussian kernel spreads it
from columns 3 through 17, with the highest value, `40`, remaining at the
center. Every row is identical because the input is a vertical line and the
`REFLECT` border mode preserves that pattern at the top and bottom edges.

If the device uses heterogeneous CPU clusters, pin the process to a known
SME-capable CPU. For example, CPU 7 has the affinity mask `80`:

```bash
adb shell 'taskset 80 /data/local/tmp/example_usage'
```

The hexadecimal mask is device-specific. Use the CPU topology of your own
device when choosing an affinity mask.

## What you've accomplished and what's next

You've run the standalone SME Gaussian blur example and confirmed the filter
output.

Next, you'll build a performance explorer that controls the example's kernel size and
measurement count from the command line.

---
title: Benchmarking
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll benchmark matrix multiplication performance using SME2,
if your machine supports native execution of SME2 instructions.

## About benchmarking and emulation

Emulation is generally not the best way to assess the performance of a piece of
code. Emulation focuses on correctly simulating instructions and not accurate
execution timing. For example, as explained in the  [outer product
section](../5-outer-product/), improving performance involves increasing the
`macc`-to-`load` ratio.

Emulators, including the FVP, do not model in detail memory bandwidth, cache
behavior, or latency. At best, an emulator provides an instruction count for the
vanilla reference implementation versus the assembly-/intrinsic-based versions
of the matrix multiplication, which is useful for functional validation but not
for precise benchmarking.

## Benchmarking on platforms with native SME2 support or Android phones

{{% notice Note %}}
Benchmarking and profiling are complex tasks. This Learning Path provides a
*simplified* framework for observing SME2-related performance improvements.
{{% /notice %}}

If your machine natively supports SME2, or if the target Android phone supports
SMES, then benchmarking is possible. When `sme2_matmul_asm` and
`sme2_matmul_intr` were compiled with `BAREMETAL=0`, the *benchmarking mode* is
available.

*Benchmarking mode* is enabled by prepending the `M`, `K`, `N` optional
parameters with an iteration count (`I`).

## Run the intrinsic version

Now measure the execution time of `sme2_matmul_intr` for 1000 multiplications of
matrices with the default sizes:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-4">}}
./build-native/sme2_matmul_intr 1000
SME2 Matrix Multiply fp32 *intr* [benchmarking mode, 1000 iterations] with M=125, K=70, N=35
Reference implementation: min time = 101 us, max time = 438 us, avg time = 139.42 us
SME2 implementation *intr*: min time = 1 us, max time = 8 us, avg time = 1.82 us
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2,5-7">}}
adb push build-android/sme2_matmul_intr /data/local/tmp
build-android/sme2_matmul_intr: 1 file pushed, 0 skipped. 29.7 MB/s (19456 bytes in 0.001s)
adb shell chmod 755 /data/local/tmp/sme2_matmul_intr
adb shell /data/local/tmp/sme2_matmul_intr 1000
SME2 Matrix Multiply fp32 *intr* [benchmarking mode, 1000 iterations] with M=125, K=70, N=35
Reference implementation: min time = 115 us, max time = 808 us, avg time = 117.98 us
SME2 implementation *intr*: min time = 5 us, max time = 21 us, avg time = 6.56 us
{{< /tab >}}

{{< /tabpane >}}

The execution time is reported in microseconds. A wide spread between the
minimum and maximum figures can be noted and is expected as the way of doing the
benchmarking is simplified for the purpose of simplicity. You will, however,
note that the intrinsic version of the matrix multiplication brings a significant
reduction in time, from 18x to 76x depending on the device.

{{% notice Tip %}}
You can override the default values for `M` (125), `K` (25), and `N` (70) and
provide your own values on the command line. For example, you can benchmark the
`M=7`, `K=8`, and `N=9` case with:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-4">}}
./build-native/sme2_matmul_intr 1000 7 8 9
SME2 Matrix Multiply fp32 *intr* [benchmarking mode, 1000 iterations] with M=7, K=8, N=9
Reference implementation: min time = 0 us, max time = 14 us, avg time = 0.93 us
SME2 implementation *intr*: min time = 0 us, max time = 1 us, avg time = 0.61 us
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2-4">}}
adb shell /data/local/tmp/sme2_matmul_intr 1000 7 8 9
SME2 Matrix Multiply fp32 *intr* [benchmarking mode, 1000 iterations] with M=7, K=8, N=9
Reference implementation: min time = 0 us, max time = 1 us, avg time = 0.37 us
SME2 implementation *intr*: min time = 0 us, max time = 8 us, avg time = 0.32 us
{{< /tab >}}

{{< /tabpane >}}

{{% /notice %}}

Now measure the execution time of `sme2_matmul_asm` for 1000 multiplications of
matrices with the default sizes:

{{< tabpane code=true >}}

{{< tab header="Native SME2 support" language="bash" output_lines="2-4">}}
./build-native/sme2_matmul_asm 1000
SME2 Matrix Multiply fp32 *asm* [benchmarking mode, 1000 iterations] with M=125, K=70, N=35
Reference implementation: min time = 101 us, max time = 373 us, avg time = 136.49 us
SME2 implementation *asm*: min time = 1 us, max time = 8 us, avg time = 1.44 us
{{< /tab >}}

{{< tab header="Android phones with SME2 support" language="bash" output_lines="2,5-7">}}
adb push build-android/sme2_matmul_asm /data/local/tmp
build-android/sme2_matmul_asm: 1 file pushed, 0 skipped. 29.7 MB/s (19456 bytes in 0.001s)
adb shell chmod 755 /data/local/tmp/sme2_matmul_asm
adb shell /data/local/tmp/sme2_matmul_asm 1000
SME2 Matrix Multiply fp32 *asm* [benchmarking mode, 1000 iterations] with M=125, K=70, N=35
Reference implementation: min time = 114 us, max time = 754 us, avg time = 117.91 us
SME2 implementation *asm*: min time = 3 us, max time = 18 us, avg time = 4.14 us
{{< /tab >}}

{{< /tabpane >}}

You'll notice that although the vanilla reference matrix multiplication is the
same, there is some variability in the execution time.

The assembly version of the SME2 matrix multiplication runs slightly faster. However, this
should not lead you to be convinced that assembly is inherently better as this is not an
apples-to-apples comparison:
- Firstly, the assembly version has specific constraints on the `K` parameter
  that the intrinsics version does not.
- Second, the assembly version includes an optimization that the intrinsic
  version, for the sake of readability in this Learning Path, does not have (see
  the [Going further
  section](/learning-paths/cross-platform/multiplying-matrices-with-sme2/10-going-further/)
  to learn more).
- Most importantly, the intrinsics version is significantly more readable and
  maintainable. These are qualities that matter in real-world development.
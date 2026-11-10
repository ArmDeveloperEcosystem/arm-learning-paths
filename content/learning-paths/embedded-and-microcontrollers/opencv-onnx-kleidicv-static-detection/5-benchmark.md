---
title: "Evaluate KleidiCV preprocessing and pipeline performance"
description: Compare image-operation and full preprocessing latency between baseline and default KleidiCV builds, then relate the gains to overall YOLOX pipeline performance.

weight: 6

layout: "learningpathall"
---

## Prepare the board for measurement

Performance measurements on development boards can vary because of background activity, dynamic CPU frequency, and temperature. Close unnecessary applications and allow the board to cool before each run.

Keep the following components consistent for measurements:

- Board and operating system
- OpenCV source revision and compiler
- Release build configuration for both OpenCV and the application
- YOLOX model and static image
- Warm-up and measured iteration counts
- OpenCV thread count
- CPU affinity
- CPU frequency governor

The example measurements were recorded using four OpenCV threads. Change this value if your board has fewer than four available CPU cores.

Inspect the available CPUs and choose one fixed set for every run:

```bash
lscpu -e=CPU,MAXMHZ,ONLINE
```

Choose CPUs of the same core type by using the topology information of your board.
On a heterogeneous system, don't mix performance and efficiency cores.
The maximum frequency alone doesn't identify the core type. 

Set `CPU_LIST` to your chosen CPUs:

```bash
export CPU_LIST=5,6,9,11
```
The reference measurement was recorded using four Cortex-A720 CPUs.

Don't copy this value without checking your system. CPU numbering and heterogeneous core placement vary by platform.

Set the benchmark parameters:

```bash
set -o pipefail
export THREADS=4
export WARMUP=10
export ITERATIONS=100
export ROUND=1
```

Keep the CPU frequency governor unchanged across both builds and all rounds. The reference measurement was recorded using `performance`. Use the same governor if you want to compare with those results. 

Only change the frequency policy with permission, and restore the original settings afterward. On platforms without Linux CPU frequency governors, keep the platform frequency-management settings consistent instead.

## Run the benchmarks

Navigate to the application directory:

```bash
cd ~/opencv-kleidicv-lab/static-detection
```

Run the baseline benchmark:

```bash
LD_LIBRARY_PATH=$HOME/opencv-kleidicv-lab/install-baseline/lib \
    taskset -c "$CPU_LIST" ./app-build-baseline/yolox_static \
    --model=object_detection_yolox_2022nov.onnx \
    --image=input.jpg \
    --labels=coco.names \
    --output=benchmark-baseline.jpg \
    --build-name=baseline \
    --threads="$THREADS" \
    --warmup="$WARMUP" \
    --iterations="$ITERATIONS" | tee "baseline-round-$ROUND.txt"
```

Run the default KleidiCV benchmark:

```bash
LD_LIBRARY_PATH=$HOME/opencv-kleidicv-lab/install-kleidicv-default/lib \
    taskset -c "$CPU_LIST" ./app-build-kleidicv-default/yolox_static \
    --model=object_detection_yolox_2022nov.onnx \
    --image=input.jpg \
    --labels=coco.names \
    --output=benchmark-kleidicv-default.jpg \
    --build-name=kleidicv-default \
    --threads="$THREADS" \
    --warmup="$WARMUP" \
    --iterations="$ITERATIONS" | tee "kleidicv-default-round-$ROUND.txt"
```

Each run reports the mean, minimum, and standard deviation for every stage. Confirm that both builds report three detections for the supplied image before comparing their performance.

Use the image operations subtotal as your primary metric. Full preprocessing, printed as `Preprocessing`, also includes padding and tensor packing. Compare both with deep neural network (DNN) inference and end-to-end latency to assess the application-level impact.

For a more stable comparison, run six rounds, running each build once per round and alternating their order:

| Rounds | Running order |
|---|---|
| 1, 3, and 5 | Baseline, KleidiCV |
| 2, 4, and 6 | KleidiCV, baseline |

Before each new round, set `ROUND` to its number, for example `export ROUND=2`. This preserves logs for each run. Keep all other settings unchanged. If a command fails, resolve the error and repeat the affected round before comparing results.

After all six rounds, extract the detection counts and main stage timings from the logs:

```bash
grep -E \
    '^(Build label|Detections|Preprocessing|Resize|BGR to RGB|Uint8 to float32|DNN inference|End-to-end)' \
    baseline-round-*.txt kleidicv-default-round-*.txt
```

The application doesn't print the image operations subtotal directly. For each run, add the reported means for `Resize`, `BGR to RGB`, and `Uint8 to float32`. Then, take the median of those six per-run subtotals for each build. Don't add three independently calculated stage medians.

For full preprocessing and the individual stages, take the median of the six reported means. Keep all 12 logs to examine run-to-run variation.

Calculate the KleidiCV build latency reduction relative to baseline using those medians:

```text
reduction (%) = (baseline time - optimized time) / baseline time * 100
```

A positive result means that the optimized build took less time. A negative result means that it took longer. Report the measured values even when the difference is small or negative.

## Review a reference measurement

The reference measurement reports baseline and default KleidiCV results from a six-round measurement session on October 29, 2026. Both applications were built from the same source.

The reference measurement was recorded using the following components:

- Unpatched OpenCV 4.13.0 and KleidiCV 26.06
- A Radxa Orion O6 running Debian 12, with eight Cortex-A720 CPUs and four Cortex-A520 CPUs
- Linux kernel `6.12.111+deb12-arm64`, GCC `12.2.0`, and CMake `3.25.1`
- OpenCV and the application compiled in Release mode, with compiler optimizations enabled
- Four Cortex-A720 CPUs (`5,6,9,11`) with the `performance` frequency governor: 2.3 GHz for CPUs `5,6`, 2.4 GHz for CPU `9`, and 2.5 GHz for CPU `11`
- The original OpenCV `messi5.jpg` photograph provided in the Learning Path, with no segmentation overlay: `548 x 342` pixels and three channels, resized to `640 x 399` and padded to `640 x 640`
- Six rounds per configuration, with each run using four OpenCV threads, 10 warm-up iterations, and 100 measured iterations

{{% notice Note %}}
The image operations subtotal fell from 1.660 ms to 0.883 ms with default
KleidiCV dispatch, a 46.8% reduction. Full preprocessing fell from 2.494 ms
to 2.058 ms, a 17.5% reduction. The pipeline median fell by only 0.3%,
within run-to-run variation.
{{% /notice %}}

The following table includes a comparison of median latencies across six runs per build:

| Stage | Baseline | KleidiCV default | Latency reduction |
|---|---:|---:|---:|
| Image operations subtotal | 1.660 ms | 0.883 ms | 46.8% |
| Full preprocessing | 2.494 ms | 2.058 ms | 17.5% |
| Resize | 0.380 ms | 0.149 ms | 60.8% |
| Padding | 0.048 ms | 0.049 ms | -2.1% |
| BGR to RGB | 0.039 ms | 0.043 ms | -10.3% |
| Uint8 to float32 | 1.241 ms | 0.692 ms | 44.3% |
| Tensor packing | 0.761 ms | 1.244 ms | -63.5% |
| DNN inference | 309.995 ms | 309.383 ms | 0.2% |
| Postprocessing | 0.488 ms | 0.486 ms | 0.3% |
| Rendering | 0.148 ms | 0.149 ms | -1.0% |
| End-to-end | 313.206 ms | 312.152 ms | 0.3% |

Values are rounded for display. Reductions were calculated using the unrounded medians. Each median is calculated independently, so stage medians don't necessarily sum to the median total.

The six-run preprocessing means ranged from `2.337` to `3.002` ms for baseline and `1.643` to `2.267` ms for KleidiCV. Pipeline means ranged from `312.674` to `314.673` ms and `311.214` to `322.207` ms respectively.

The pipeline ranges overlap, so the small median reduction isn't evidence of a consistent pipeline-level speedup. All six runs were retained, and both builds detected three objects with equivalent classes and bounding boxes.

## Interpret the measurements

Resize and type conversion account for the image-operation gains. These API-stage timings include buffer allocation and memory access, so they don't measure kernel-only speedups. BGR-to-RGB conversion didn't improve but remains included because it's eligible for KleidiCV Hardware Acceleration Layer (HAL) acceleration.

Slower tensor packing partially offsets these gains in full preprocessing. Padding remains an OpenCV operation in this unpatched build, and the OpenCV DNN `blobFromImage()` performs tensor packing. Neither is a KleidiCV HAL operation, so don't attribute the tensor-packing timing change to a KleidiCV kernel.

DNN inference dominates the workload and isn't directly accelerated by KleidiCV. Its timer includes input setup and `net.forward()`.

The reported end-to-end value sums the timed in-memory stages, including rendering. The value excludes model loading, image-file decoding, and output-file writing, so it's not file-to-file wall-clock latency.

## Understand the resize speedup

For the reference image, you resize three-channel uint8 data from `548 x 342` to `640 x 399` with bilinear interpolation. KleidiCV 26.06 selects a Neon implementation under the default build settings. Although Scalable Vector Extension 2 (SVE2) support is enabled, `KLEIDICV_LIMIT_SVE2_TO_SELECTED_ALGORITHMS=ON` excludes this resize implementation from SVE2 dispatch. For more information, see the [KleidiCV build defaults](https://gitlab.arm.com/kleidi/kleidicv/-/blob/26.06/kleidicv/CMakeLists.txt) and [dispatch definitions](https://gitlab.arm.com/kleidi/kleidicv/-/blob/26.06/kleidicv/include/kleidicv/dispatch.h).

The [OpenCV baseline implementation](https://github.com/opencv/opencv/blob/4.13.0/modules/imgproc/src/resize.cpp) already uses Single Instruction, Multiple Data (SIMD). However, its three-channel horizontal loop advances one pixel at a time. 

The [KleidiCV Neon implementation](https://gitlab.arm.com/kleidi/kleidicv/-/blob/26.06/kleidicv/src/resize/resize_linear_generic_u8_neon.h) loads contiguous byte blocks. It uses register-table lookups to select neighboring samples for 16 channel values at a time. The implementation completes vertical and horizontal interpolation within each vector block. It avoids the intermediate 32-bit row-buffer writes and reads that are used by OpenCV.

KleidiCV also uses interpolation weights with eight fractional bits and narrower intermediate arithmetic, compared with OpenCV 11-bit coefficients. This supports compact vector calculations, but changes quantization and rounding. 

Equivalent detections don't prove pixel-identical resize output. Compare image differences and detection accuracy on representative inputs if your application needs that assurance.

These implementation differences explain how acceleration is possible, not how much each optimization contributes to the measured gain. Allocation and thread scheduling also affect the API-stage timing. You need runtime profiling and an isolated resize benchmark to separate their contributions.

## What you've accomplished

You've built and run a YOLOX detection pipeline on arm64 and compared baseline and KleidiCV performance. You can now distinguish image-operation gains from full preprocessing and overall pipeline latency.

Profile the dominant stage of your application before choosing the next optimization.

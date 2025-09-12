---
title: Performance
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark mode

The application you built earlier includes a *benchmark mode* that runs the core processing loop multiple times in a hot loop:

- `ai-camera-pipelines/bin/cinematic_mode_benchmark`
- `ai-camera-pipelines/bin/low_light_image_enhancement_benchmark`
- `ai-camera-pipelines/bin/neural_denoiser_temporal_benchmark_4K`

These benchmarks demonstrate the performance improvements enabled by KleidiCV and KleidiAI:
- KleidiCV enhances OpenCV performance with computation kernels optimized for Arm processors.
- KleidiAI accelerates LiteRT + XNNPack inference using AI-optimized micro-kernels tailored for Arm CPUs.

## Performances with KleidiCV and KleidiAI

By default, the OpenCV library is built with KleidiCV support, and LiteRT+xnnpack is built with KleidiAI support.

You can run the benchmarks using the applications you built earlier.

Run the Background Blur benchmark:

```bash
bin/cinematic_mode_benchmark 20 resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
```

The output is similar to:

```output
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 2028.745 ms
```

Run the Low Light Enhancement benchmark:

```bash
bin/low_light_image_enhancement_benchmark 20 resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l1_loss_float32.tflite
```

The output is similar to:

```output
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 58.2126 ms
```

Last, run the Neural Denoising benchmark:

```bash
bin/neural_denoiser_temporal_benchmark_4K 20
```

The output is similar to:

```output
Total run time over 10 iterations: 37.6839 ms
```

From these results, you can see that:
- `cinematic_mode_benchmark` performed 20 iterations in 2028.745 ms
- `low_light_image_enhancement_benchmark` performed 20 iterations in 58.2126 ms
- `neural_denoiser_temporal_benchmark_4K` performed 20 iterations in 37.6839 ms

## Benchmark results without KleidiCV and KleidiAI

To measure the performance without these optimizations, recompile the pipelines using the following flags in your CMake command:
```bash
-DENABLE_KLEIDICV:BOOL=OFF -DXNNPACK_ENABLE_KLEIDIAI:BOOL=OFF
```

Re-run the Background Blur benchmark:

```bash
bin/cinematic_mode_benchmark 20 resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
```

The new output is similar to:

```output
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 2030.5525 ms
```

Re-run the Low Light Enhancment benchmark:

```bash
bin/low_light_image_enhancement_benchmark 20 resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l1_loss_float32.tflite
```

The new output is similar to:

```output
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 58.0613 ms
```

Re-run the Neural Denoising benchmark:

```bash
bin/neural_denoiser_temporal_benchmark_4K 20
```

The new output is similar to:

```output
Total run time over 20 iterations: 38.0813 ms
```

## Comparison table and future performance uplift with SME2

| Benchmark                                 | Without KleidiCV+KleidiAI | With KleidiCV+KleidiAI |
|-------------------------------------------|---------------------------|------------------------|
| `cinematic_mode_benchmark`                | 2030.5525 ms              | 2028.745 ms (-0.09%)   |
| `low_light_image_enhancement_benchmark`   | 58.0613 ms                | 58.2126 ms (0.26%)     |
| `neural_denoiser_temporal_benchmark_4K`   | 38.0813 ms                | 37.6839 ms (-1.04%)    |

As shown, the Background Blur (`cinematic_mode_benchmark`) and Neural Denoising
pipelines gains only a minor improvement, while the low-light enhancement pipeline
sees a minor performance degradation (0.26%) when KleidiCV and KleidiAI are
enabled.

A major benefit of using KleidiCV and KleidiAI though is that they can
automatically leverage new Arm architecture features - such as SME2 (Scalable
Matrix Extension v2) - without requiring changes to your application code.

As KleidiCV and KleidiAI operate as performance abstraction layers, any future
hardware instruction support can be utilized by simply rebuilding the
application. This enables better performance on newer processors without
additional engineering effort.

---
title: Performance
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The application you built earlier includes a *benchmark mode* that runs the core processing loop multiple times in a hot loop:

- `ai-camera-pipelines/bin/cinematic_mode_benchmark`
- `ai-camera-pipelines/bin/low_light_image_enhancement_benchmark`

These benchmarks demonstrate the performance improvements enabled by KleidiCV and KleidiAI:
- KleidiCV enhances OpenCV performance with computation kernels optimized for Arm processors.

- KleidiAI accelerates TFLite + XNNPack inference using AI-optimized micro-kernels tailored for Arm CPUs.

## Performances with KleidiCV and KleidiAI

By default, the OpenCV library is built with KleidiCV support, and TFLite+xnnpack is built with KleidiAI support. You can run the benchmarks using the applications you built earlier:

```bash
$ bin/cinematic_mode_benchmark 20 resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 2023.39 ms

$ bin/low_light_image_enhancement_benchmark 20 resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l2_loss_int8_only_ptq.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 54.3546 ms
```

From these results, you can see that:
- `cinematic_mode_benchmark` performed 20 iterations in 1985.99 ms.
- `low_light_image_enhancement_benchmark` performed 20 iterations in 52.3448 ms.

## Benchmark results without KleidiCV and KleidiAI

To measure the performance without these optimizations, recompile the pipelines using the following flags in your CMake command:
```bash
-DENABLE_KLEIDICV:BOOL=OFF -DXNNPACK_ENABLE_KLEIDIAI:BOOL=OFF
```

Then rerun the benchmarks:

```bash
$ bin/cinematic_mode_benchmark 20 resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 2029.25 ms

$ bin/low_light_image_enhancement_benchmark 20 resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l2_loss_int8_only_ptq.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 79.431 ms
```

### Comparison table

| Benchmark                                 | Without KleidiCV+KleidiAI | With KleidiCV+KleidiAI |
|-------------------------------------------|---------------------------|------------------------|
| `cinematic_mode_benchmark`                | 2029.25 ms                | 2023.39 ms             |
| `low_light_image_enhancement_benchmark`   | 79.431 ms                 | 54.3546 ms             |

As shown, the background blur pipeline (`cinematic_mode_benchmark`) gains only a small improvement, while the low-light enhancement pipeline sees a significant ~30% performance uplift when KleidiCV and KleidiAI are enabled.

## Future performance uplift with SME2

A major benefit of using KleidiCV and KleidiAI is that they can automatically leverage new Arm architecture features - such as SME2 (Scalable Matrix Extension v2) - without requiring changes to your application code.

As KleidiCV and KleidiAI operate as performance abstraction layers, any future hardware instruction support — like SME2 — can be utilized by simply rebuilding the application. This enables better performance on newer processors without additional engineering effort.



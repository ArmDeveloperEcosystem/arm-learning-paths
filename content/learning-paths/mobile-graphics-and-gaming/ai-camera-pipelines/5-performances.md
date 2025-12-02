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
- KleidiAI accelerates LiteRT+XNNPack inference using AI-optimized micro-kernels tailored for Arm CPUs.

## Performance with SME

You can run the benchmarks using the applications you built earlier (with SME2 support).

Run the Background Blur benchmark:

```bash
bin/cinematic_mode_benchmark 20 --tflite_file resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
```

The output is similar to:

```output
INFO: Frame rate throttling is turned OFF
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
INFO: Total run time over 20 iterations: 614.724 ms
INFO: Average FPS: 32.5349
```

Run the Low Light Enhancement benchmark:

```bash
bin/low_light_image_enhancement_benchmark 20 --tflite_file resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l1_loss_float32.tflite
```

The output is similar to:

```output
INFO: Frame rate throttling is turned OFF
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
INFO: Total run time over 20 iterations: 57.3958 ms
INFO: Average FPS: 348.457
```

Last, run the Neural Denoising benchmark:

```bash
bin/neural_denoiser_temporal_benchmark_4K 20
```

The output is similar to:

```output
INFO: Frame rate throttling is turned OFF
INFO: Total run time over 20 iterations: 36.2114 ms
INFO: Average FPS: 552.312
```

From these results, you can see that:
- `cinematic_mode_benchmark` performed 20 iterations in 614.724 ms, which means 32.5349 FPS
- `low_light_image_enhancement_benchmark` performed 20 iterations in 57.3958 ms, which means 348.457 FPS
- `neural_denoiser_temporal_benchmark_4K` performed 20 iterations in 36.2114 ms, which means 552.312 FPS

## Performance without SME2

To measure the performances without the benefits of SME2, set `ENABLE_SME2=0` and recompile the pipelines as shown in the [build](/learning-paths/mobile-graphics-and-gaming/ai-camera-pipelines/3-build/) page.

You can now re-run the benchmarks and compare the performance benefits of using SME2.

## Example performance with a Vivo X300 Android phone

The table table shows the measurements (in FPS, Frames Per Second) measured on a Vivo X300 android phone:

| Benchmark                                                 | Without SME2 | With SME2 | Uplift  |
|-----------------------------------------------------------|--------------|-----------|---------|
| `cinematic_mode_benchmark`                                | 17           | 27        | +58.8%  |
| `low_light_image_enhancement_benchmark`                   | 51           | 84        | +64.70% |
| `neural_denoiser_temporal_benchmark_4K` (temporal only)   | 249          | 678       | +172.3% |
| `neural_denoiser_temporal_benchmark_4K` (spatio-temporal) | -            | 87        |         |

{{% notice Note %}}
The Android system enforces throttling, so your own results may vary slightly.
{{% /notice %}}

As shown, SME2 brings a dramatic performance improvement. This new power also enables to use much more
complex processing algorithms like the spatio-temporal denoising.

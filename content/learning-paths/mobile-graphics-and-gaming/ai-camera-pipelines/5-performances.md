---
title: Performance
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The application that was previously built has a *benchmark* mode that will run the core function multiple times in a hot loop:

- `ai-camera-pipelines/bin/cinematic_mode_benchmark`
- `ai-camera-pipelines/bin/low_light_image_enhancement_benchmark`

The performance of the camera pipelines have been improved by using KleidiCV and KleidiAI:
- KleidiCV improves the performances of OpenCV with computation kernels optimized for the Arm processors.
- KleidiAI improves the performances of TFLite+XNNPack with computations kernels dedicatd to AI tasks on Arm processors.

## Performances with KleidiCV and KleidiAI

By default, the OpenCV library is built with KleidiCV support, and TFLite+xnnpack is built with KleidiAI support, so let's measure the performance of the applications we have already built:

```BASH
$ bin/cinematic_mode_benchmark 20 resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 2023.39 ms

$ bin/low_light_image_enhancement_benchmark 20 resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l2_loss_int8_only_ptq.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 54.3546 ms
```

It can be seen from above that:
- `cinematic_mode_benchmark` performed 20 iterations in 1985.99 ms,
- `low_light_image_enhancement_benchmark` performed 20 iterations in 52.3448 ms.

## Performances without KleidiCV and KleidiAI

Now re-run the build steps from the previous section and change CMake's invocation to use `-DENABLE_KLEIDICV:BOOL=OFF -DXNNPACK_ENABLE_KLEIDIAI:BOOL=OFF` in order *not* to use KleidiCV and KleidiAI.

You can run the benchmarks again:

```BASH
$ bin/cinematic_mode_benchmark 20 resources/depth_and_saliency_v3_2_assortedv2_w_augment_mobilenetv2_int8_only_ptq.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 2029.25 ms

$ bin/low_light_image_enhancement_benchmark 20 resources/HDRNetLIME_lr_coeffs_v1_1_0_mixed_low_light_perceptual_l2_loss_int8_only_ptq.tflite
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
Total run time over 20 iterations: 79.431 ms
```

Let's put all those numbers together in a simple table to compare them easily:

| Benchmark                                 | Without KleidiCV+KleidiAI | With KleidiCV+KleidiAI |
|-------------------------------------------|---------------------------|------------------------|
| `cinematic_mode_benchmark`                | 2029.25 ms                | 2023.39 ms             |
| `low_light_image_enhancement_benchmark`   | 79.431 ms                 | 54.3546 ms             |

As can be seen, the blur pipeline (`cinematic_mode_benchmark`) benefits marginally from KleidiCV+KleidiAI, whereas low light enhancement got almost a 30% boost.

## Future Performance Uplift with SME2

A nice benefit of using KleidiCV and KleidiAI is that whenever the hardware adds support for new and more powerful instructions, the applications will be able to get a performance uplift without requiring complex software changes — KleidiCV and KleidiAI operate as abstraction layers that will be able to build on hardware improvements to boost future performance. An example of such a performance boost *for free* will take place in a couple of months when processors implementing SME2 become available.
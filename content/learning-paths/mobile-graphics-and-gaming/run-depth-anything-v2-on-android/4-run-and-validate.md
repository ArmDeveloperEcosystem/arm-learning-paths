---
title: Run and validate depth estimation
description: Generate relative-disparity maps from two images, inspect the adapter contract, and verify offline inference.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Generate a depth map

Start Arm AI Portal Image Analysis:

```console
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
```

Run the first image:

1. Select **Depth Anything V2 Small INT8**.
2. Select **Load model**.
3. Select **Choose image** and choose a JPEG or PNG scene with objects at different distances.
4. Select **Run depth estimation**.

The app displays a grayscale map. Brighter pixels have higher relative disparity and represent nearer regions. Darker pixels represent farther regions.

The result panel reports the original resolution, model resolution, and finite disparity range. The status panel reports model load and inference times.

## Understand the adapter contract

The Android adapter follows the model card's fixed contract:

| Stage | Behavior |
| --- | --- |
| Decode | Read the selected RGB image with its orientation applied; the application may subsample a large image during decoding to limit memory use |
| Resize | Resize the decoded RGB image to `686 x 518` with bicubic interpolation; this can change the source aspect ratio |
| Normalize | Scale channels to `[0, 1]`, then apply ImageNet mean and standard deviation |
| Input | Create one `float32 [1, 3, 518, 686]` tensor in NCHW order |
| Inference | Execute `forward` with the XNNPACK-backed ExecuTorch module |
| Output | Require one finite `float32 [1, 518, 686]` relative-disparity tensor |
| Render | Min-max normalize each result to `[0, 255]` and resize it to the original display resolution with bilinear filtering |

If the output is constant, the adapter renders a black map instead of dividing by zero. It rejects an incorrect shape, dtype, missing XNNPACK declaration, or non-finite value.

## Validate input-dependent offline inference

Choose a second image with a different scene and run depth estimation again. Confirm that:

- both runs finish without a load or tensor-contract error;
- the disparity range contains finite numbers;
- the second depth map differs from the first;
- nearer and farther regions have plausible brightness ordering;
- the displayed result fills the original image dimensions.

Enable airplane mode or otherwise disconnect the phone from the network, then run the model again. The result should still appear because inference is local. Re-enable the network afterward if you need it for other applications.

Record the following details:

- Android phone model and Android version
- model filename
- ExecuTorch version (`1.3.1` in this sample)
- both input images and generated maps
- load time and both inference times

The model card reports evaluation on 654 indoor images from the official raw-depth NYU Depth V2 test split. Outdoor and out-of-distribution scenes weren't covered. The original and optimized models are licensed under Apache-2.0. The optimized model is intended for evaluation, prototyping, and integration exploration, and isn't a production-ready or supported solution. Re-evaluate its accuracy and suitability on your own data before production use.

{{% notice Important %}}
The model card and application use different ExecuTorch versions and test conditions. Treat timings displayed by the application as illustrative; don't compare them directly with the published vivo X300 benchmark.
{{% /notice %}}

## What you've accomplished and what's next

You've run Depth Anything V2 Small on an Arm-based Android phone, generated input-dependent relative-disparity maps, and verified that inference works without a network connection.

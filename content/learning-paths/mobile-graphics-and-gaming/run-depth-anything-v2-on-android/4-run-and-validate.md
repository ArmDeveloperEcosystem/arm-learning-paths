---
title: Run and validate depth estimation
description: Generate relative-disparity maps from two images, inspect the adapter contract, and validate input-dependent results.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Generate a depth map

Start Image Analysis:

```console
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
```

Run the first image:

1. Select **Depth Anything V2 Small INT8**.
2. Select **Load model**.
3. Select **Choose image** and choose a JPEG or PNG scene with objects at different distances.
4. Select **Run depth estimation**.

Image Analysis temporarily disables the model and image controls while it decodes an image, loads a model, or runs inference. The controls become available again when the operation finishes or reports an error.

The app displays a grayscale map. Brighter pixels have higher relative disparity and represent nearer regions. Darker pixels represent farther regions.

The result panel reports the original source resolution, model input and output resolution, and finite disparity range. The displayed map uses the decoded preview dimensions, which can be smaller for a large source image. The status panel reports model load and inference times.

After you stage the model in application-private storage, depth inference runs locally on the phone and doesn't need a network connection.

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
| Render | Min-max normalize each result to `[0, 255]` and resize it to the decoded preview dimensions with bilinear filtering |

If the output is constant, the adapter renders a black map instead of dividing by zero. It rejects an incorrect shape, dtype, missing XNNPACK declaration, or non-finite value.

## Validate input-dependent results

Choose a second image with a different scene and run depth estimation again. Confirm that:

- both runs finish without a load or tensor-contract error;
- the disparity range contains finite numbers;
- the second depth map differs from the first;
- nearer and farther regions have plausible brightness ordering;
- the displayed result fills and aligns with the decoded image preview.

## What you've accomplished and what's next

You've run Depth Anything V2 Small on an Arm-based Android phone and generated and validated input-dependent relative-disparity maps.

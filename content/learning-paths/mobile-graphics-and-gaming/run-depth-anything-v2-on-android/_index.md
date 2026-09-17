---
title: Run Depth Anything V2 depth estimation on Android
draft: true
lastmod: 2026-09-17
cascade:
    draft: true

description: Run an Arm-optimized Depth Anything V2 Small model locally on an Arm-based Android phone with ExecuTorch and render a relative-disparity map.

minutes_to_complete: 40

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run monocular depth estimation locally on an Arm-based Android phone.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone
    - Download and run the Depth Anything V2 Small INT8 ExecuTorch model from the Arm AI Portal
    - Explain the model's fixed image preprocessing and relative-disparity output
    - Validate input-dependent depth maps while the phone is offline

prerequisites:
    - A macOS, Linux, or Windows development computer with Git, Python 3, and Java 17 or later
    - An Arm-based Android phone running Android 9 or later
    - Android SDK 35 and Android SDK Platform Tools
    - A Hugging Face account if the model repository requires authentication
    - A data-capable USB cable
    - Basic familiarity with terminal commands and Android applications

author: Elad Gross

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Arm C1
tools_software_languages:
    - Kotlin
    - Python
    - ExecuTorch
    - XNNPACK
    - KleidiAI
    - Arm AI Portal
    - Hugging Face
operatingsystems:
    - Android
    - macOS
    - Linux
    - Windows

further_reading:
    - resource:
        title: Depth Anything V2 Small INT8 model card
        link: https://developer.arm.com/ai/models/hugging-face/Arm/depth-anything-v2-small-int8-xnnpack-executorch-vivo-x300/depth-anything-v2-small-int8-pte
        type: documentation
    - resource:
        title: Depth Anything V2 Small INT8 on Hugging Face
        link: https://huggingface.co/Arm/depth-anything-v2-small-int8-xnnpack-executorch-vivo-x300
        type: documentation
    - resource:
        title: Run apps on a hardware device
        link: https://developer.android.com/studio/run/device
        type: documentation
    - resource:
        title: ExecuTorch for Android
        link: https://docs.pytorch.org/executorch/stable/using-executorch-android.html
        type: documentation
    - resource:
        title: XNNPACK backend for ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/backends-xnnpack.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

## Run monocular depth estimation locally

Depth Anything V2 Small estimates relative scene depth from one RGB image. The Arm-optimized artifact is quantized to INT8 and exported as an ExecuTorch `.pte` program for XNNPACK and KleidiAI on Arm-based mobile CPUs.

You'll use an application called **Arm AI Portal Image Analysis** and its validated Android adapter to download the model, copy it into application-private storage, and generate a grayscale depth map without sending the image to a server. White pixels represent nearer regions and black pixels represent farther regions.

The output is *relative disparity*, not distance measured in meters. Metric depth needs additional scale-and-shift alignment outside the model.

The model accepts a fixed `float32 [1, 3, 518, 686]` tensor. To limit memory use, the application may subsample a large image while decoding it. The adapter bicubically resizes the decoded RGB image to `686 x 518`, even when that changes its aspect ratio, and applies ImageNet normalization. It then validates the `[1, 518, 686]` output and resizes the rendered depth map back to the original display resolution.

{{% notice Note %}}
The model card and application use different ExecuTorch versions and test conditions. Treat timings displayed by the application as illustrative; don't compare them directly with the published vivo X300 benchmark.
{{% /notice %}}

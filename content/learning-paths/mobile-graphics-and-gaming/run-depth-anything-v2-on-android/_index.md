---
title: Run an Arm AI Portal depth estimation model on Android

description: Run an Arm-optimized Depth Anything V2 Small model locally on an Arm-based Android phone with ExecuTorch and render a relative-disparity map.

minutes_to_complete: 35

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run monocular depth estimation locally on an Arm-based Android phone.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone.
    - Download and run the Depth Anything V2 Small INT8 ExecuTorch model from the Arm AI Portal.
    - Inspect the model's fixed image preprocessing and relative-disparity output.
    - Validate input-dependent relative-disparity maps across two images.

prerequisites:
    - A macOS, x86_64 Linux, or Windows development computer with Git, Python 3 with `venv` and `pip`, and JDK 17 or later
    - An Arm-based Android phone running Android 9 or later
    - A Hugging Face account if the model repository requires authentication
    - A data-capable USB cable
    - Network access for the first Gradle build and model download
    - Basic familiarity with terminal commands and Android applications

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-22T20:57:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f6fe2391cc0c1cb9973781971dd86cb1313100befe1428563f7f2b5b12dda9c2
  summary_generated_at: '2026-09-22T20:57:16Z'
  summary_source_hash: f6fe2391cc0c1cb9973781971dd86cb1313100befe1428563f7f2b5b12dda9c2
  faq_generated_at: '2026-09-22T20:57:16Z'
  faq_source_hash: f6fe2391cc0c1cb9973781971dd86cb1313100befe1428563f7f2b5b12dda9c2
  summary: >-
    You'll prepare Android command-line tools, connect an Arm-based Android phone, and build and
    install an application called Image Analysis. You'll then download the Arm-optimized Depth Anything V2 Small
    INT8 ExecuTorch model and copy it into application-private storage. Finally, you'll run on-device
    depth estimation and inspect the adapter’s preprocessing and tensor contract. By comparing
    relative-disparity maps from two images, you'll confirm that the output changes with the input.
  faqs:
  - question: How do I know if my phone is detected?
    answer: >-
      Run `adb devices -l` and confirm that your phone is listed as `device`. If you see `unauthorized`, unlock your
      phone and accept the debugging prompt. On Windows, you might also need the manufacturer’s
      USB driver.
  - question: Where should I place the downloaded model file so that the app can load it?
    answer: >-
      Download `depth_anything_v2_small_executorch_optimized.pte` into `model/$MODEL_ID`. Then, use
      `adb push` to copy it through `/data/local/tmp` and `run-as` to place it at
      `files/models/$MODEL_ID/$MODEL_FILE` in application-private storage. Verify the destination
      with `run-as ... ls -l`, then remove the temporary device copy.
  - question: How do I start the app from the command line and pick the correct model?
    answer: >-
      Run `adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity`. In the app,
      select **Depth Anything V2 Small INT8**, select **Load model**, choose a JPEG or PNG image,
      and then select **Run depth estimation**.
  - question: What should I expect while the model loads or runs inference?
    answer: >-
      You’ll see the model and image controls become unavailable while the app decodes the image,
      loads the model, or runs inference. The controls become available again when the operation
      finishes or reports an error. After inference, you’ll see a grayscale relative-disparity
      map and the model load and inference times.
  - question: Which images can I use, and how do I validate results across two inputs?
    answer: >-
      Use JPEG or PNG scenes with objects at different distances. Run two different images and
      confirm that both runs finish without errors, each disparity range contains finite values,
      and the maps differ. Check that nearer regions appear brighter than farther regions and that
      each result aligns with its decoded image preview.
# END generated_summary_faq

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
        title: Run an Arm AI Portal image segmentation model on Android
        link: https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/run-image-to-image-models-on-android/
        type: learning path
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

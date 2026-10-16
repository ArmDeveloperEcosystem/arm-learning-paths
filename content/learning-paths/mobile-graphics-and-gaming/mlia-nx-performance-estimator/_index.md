---
title: Estimate neural accelerator performance with ML Inference Advisor

description: Use public MLIA packages and quantized MobileNet models to check Neural Technology compatibility, estimate NX performance, and compare model variants.

minutes_to_complete: 40

who_is_this_for: This Learning Path is for machine learning (ML) engineers and graphics developers who want to evaluate model compatibility and estimated neural accelerator (NX) performance for Arm Neural Technology before deployment.

learning_objectives:
    - Install the public Arm ML Inference Advisor (MLIA) Neural Technology plugin and discover its target profiles and backend.
    - Analyze public quantized MobileNet models with automatic model conversion.
    - Check operator compatibility and interpret NX Performance Estimator reports.
    - Compare model variants under the same target configuration and identify accuracy tradeoffs.

prerequisites:
    - An Ubuntu development host
    - Basic familiarity with Python, command-line tools, and model deployment
    - (Optional) An NX-capable Android device

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-16T21:13:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9098f0a925d67cebaa04526a071c5d632f01f4ae03cec4c3152f4694dfa538fc
  summary_generated_at: '2026-10-16T21:13:06Z'
  summary_source_hash: 9098f0a925d67cebaa04526a071c5d632f01f4ae03cec4c3152f4694dfa538fc
  faq_generated_at: '2026-10-16T21:13:06Z'
  faq_source_hash: 9098f0a925d67cebaa04526a071c5d632f01f4ae03cec4c3152f4694dfa538fc
  summary: >-
    You'll use MLIA to check whether quantized MobileNet models work with Arm
    Neural Technology and estimate their NX performance before deployment. First, you'll prepare a
    supported Ubuntu environment, download a public baseline model, and check its operator
    compatibility. Then, you'll inspect performance reports and compare a smaller-input variant
    under the same target profile. If you have a compatible Android
    device, you can also capture and analyze measured performance.
  # faqs:
  # - question: How do I verify my host meets the wheel requirements before installing?
  #   answer: >-
  #     Run `uname -m`, `python3.12 --version`, and `getconf GNU_LIBC_VERSION`. You need `x86_64`,
  #     CPython `3.12.x`, and glibc `2.39` or later on Ubuntu 24.04. You can't use this wheel on
  #     Ubuntu 22.04, native macOS, or native Linux on Arm.
  # - question: MLIA prompted me to install the NX Performance Estimator. What should I do?
  #   answer: >-
  #     Confirm the installation when prompted, read the Arm license, and continue only if you agree.
  #     If you've already installed the backend, you can proceed without repeating setup.
  # - question: Which command do I use to check operator compatibility, and where do the results go?
  #   answer: >-
  #     Run `mlia check models/baseline.tflite --target-profile neural-technology --compatibility
  #     --output-dir runs/baseline-compatibility`. Read the result in
  #     `runs/baseline-compatibility/mlia-output/mlia-output.json`. Check that its compatibility
  #     status is `ok` and that no operator checks failed.
  # - question: What result should I expect from the baseline performance check and how do I interpret it?
  #   answer: >-
  #     Run `mlia check models/baseline.tflite --target-profile neural-technology --performance
  #     --output-dir runs/baseline`. With the tested packages and profile, you should see about
  #     `136,962` total cycles and `0.09131 ms` per inference. Treat these as compiler estimates,
  #     not timings measured on a device.
  # - question: How do I compare a smaller-input MobileNet variant with the baseline?
  #   answer: >-
  #     Run compatibility and performance checks for `models/smaller.tflite` with the same
  #     `neural-technology` target profile, writing each report to a separate directory. Compare
  #     your reports with the baseline, then validate task accuracy, preprocessing, and runtime
  #     behavior on representative data before deployment.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Mali
tools_software_languages:
    - MLIA
    - NX
    - Python
    - LiteRT
    - TOSA
    - VGF
operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: MLIA Neural Technology package on PyPI
        link: https://pypi.org/project/mlia-neural-technology/
        type: documentation
    - resource:
        title: MLIA Neural Technology CLI and output documentation
        link: https://github.com/arm/mlia-neural-technology/tree/main/docs
        type: documentation
    - resource:
        title: Analyze Ethos-U models with MLIA
        link: /learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/
        type: learningpath
    - resource:
        title: TensorFlow MobileNet V1 pretrained model catalog
        link: https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md
        type: documentation
    - resource:
        title: Explore model artifacts with Model Explorer
        link: /learning-paths/cross-platform/explore-model-artifacts-with-model-explorer/
        type: learningpath
    - resource:
        title: Neural Statistics Vulkan capture layer
        link: https://github.com/arm/vulkan-layer-neural-statistics
        type: code

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

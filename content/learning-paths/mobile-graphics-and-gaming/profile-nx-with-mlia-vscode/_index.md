---
title: Profile a model on a neural accelerator with MLIA for VS Code

description: Profile a small neural upscaling model on an Android neural accelerator (NX) and use MLIA for VS Code to inspect cycle costs and follow graph operations to Python source.

minutes_to_complete: 90

who_is_this_for: >-
    This Learning Path is for machine learning or graphics developers investigating model performance on Arm neural accelerators (NX).

learning_objectives:
    - Export a small neural upscaling model with Python debug information.
    - Capture one NX dispatch with Android Scenario Runner.
    - Inspect measured cycle costs in Model Explorer.
    - Follow graph operations to Python source in Visual Studio Code (VS Code).

prerequisites:
    - An x86-64 Ubuntu 24.04 LTS host with internet access and permission to install development tools
    - Visual Studio Code 1.100 or later on the host
    - An NX-capable Android device with USB debugging that meets the [Arm ML Inference Advisor (MLIA) VS Code device requirements](https://github.com/arm/vscode-mlia/blob/main/docs/users/installation.md#requirements)
    - Python 3.12 with virtual environment support, Android Debug Bridge (`adb`), curl, and tar on the host
    - Familiarity with Bash, adb, and PyTorch model export

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-27T18:44:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a123ff8f02855c6f5050335bccb4e4c2a7de817115efb6fc046b931cc6867a6a
  summary_generated_at: '2026-10-27T18:44:38Z'
  summary_source_hash: a123ff8f02855c6f5050335bccb4e4c2a7de817115efb6fc046b931cc6867a6a
  faq_generated_at: '2026-10-27T18:44:38Z'
  faq_source_hash: a123ff8f02855c6f5050335bccb4e4c2a7de817115efb6fc046b931cc6867a6a
  summary: >-
    You'll profile a neural upscaling model on an Android device with an Arm NX,
    then inspect measured cycle costs in MLIA for VS Code. First, you'll export the VGF model and set
    up the extension. Next, you'll prepare Scenario Runner and the device, then capture an NX dispatch.
    Finally, you'll load the capture and matching VGF. You'll inspect the cycle cost of the cascade, and trace an
    operation to Python source.
#   faqs:
#   - question: Which Scenario Runner APK should I build for the example?
#     answer: >-
#       Use a debuggable Android Arm64 Scenario Runner v0.11.0 APK. Follow the MLIA Scenario Runner
#       build instructions, add `-b v2026.09.0` to `repo init`, use NDK r28c (`28.2.13676358`),
#       and set `--package-version 0.11.0`.
#   - question: What paths do I select in MLIA > New Analysis?
#     answer: >-
#       In **MLIA > New Analysis**, select **Profiling**. Add the directory that directly contains
#       `capture.json` as **Profiling data**, then select the matching VGF as **Source model**. You
#       can print both paths from the capture terminal before starting the analysis.
#   - question: How do I know my capture succeeded before I switch to VS Code?
#     answer: >-
#       Check that your retrieved `CAPTURE_ROOT` directory contains `capture.json`. Keep the device
#       connected until the helper finishes capturing the first dispatch in statistics mode `1`
#       and restores the previous GPU debug settings.
#   - question: I'm profiling my existing Android app. What do I do differently?
#     answer: >-
#       Follow the existing-application capture instructions to collect profiling data. When you
#       create the analysis, select your capture directory and the VGF that matches your app's model.
#   - question: What should I look for in Model Explorer to confirm the analysis is set up correctly?
#     answer: >-
#       You can inspect measured cycle counts for the captured NX dispatch in Model Explorer.
#       Selecting a cascade highlights its corresponding operations in **Source Model**. Select
#       a mapped operation there to open the matching Python source in VS Code.
# END generated_summary_faq

author: Matthew Sloyan

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - MLIA
    - NX
    - Visual Studio Code
    - Model Explorer
    - ExecuTorch
    - Python
    - VGF
    - Vulkan
operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: Quantize neural upscaling models with ExecuTorch
        link: /learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/
        type: learningpath
    - resource:
        title: MLIA for VS Code user guide
        link: https://github.com/arm/vscode-mlia/blob/main/docs/users/README.md
        type: documentation
    - resource:
        title: Neural Statistics Vulkan layer
        link: https://github.com/arm/vulkan-layer-neural-statistics
        type: repository
    - resource:
        title: ML SDK for Vulkan
        link: https://github.com/arm/ai-ml-sdk-manifest
        type: repository
    - resource:
        title: Estimate neural accelerator performance with ML Inference Advisor
        link: /learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/
        type: learningpath
    - resource:
        title: Analyze Ethos-U models with MLIA
        link: /learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/
        type: learningpath

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---

---
title: Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch
    
description: Export, deploy, and validate a quantized MobileSAM prompt segmentation model on an Arm Ethos-U85 Fixed Virtual Platform using ExecuTorch.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for embedded machine learning developers who want to evaluate transformer-based image segmentation on an Arm Ethos-U85 NPU with ExecuTorch.

learning_objectives:
    - Identify how the MobileSAM example turns a fixed point prompt and an image into a quantized segmentation mask
    - Set up ExecuTorch and the Arm Ethos-U development tools
    - Export, build, and run the MobileSAM example on a Corstone-320 Fixed Virtual Platform (FVP)
    - Validate quantization quality, Ethos-U delegation, and target mask agreement

prerequisites:
    - A Linux development machine with glibc 2.28 or later, or an Apple silicon Mac running macOS 15 or later
    - Familiarity with PyTorch model export and embedded cross-compilation

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T17:01:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f366e4394846f04a17753ebfb0a8d89686fd53890e83ca73953598e49c33da9e
  summary_generated_at: '2026-09-10T17:01:35Z'
  summary_source_hash: f366e4394846f04a17753ebfb0a8d89686fd53890e83ca73953598e49c33da9e
  faq_generated_at: '2026-09-10T17:01:35Z'
  faq_source_hash: f366e4394846f04a17753ebfb0a8d89686fd53890e83ca73953598e49c33da9e
  summary: >-
    You'll deploy MobileSAM prompt segmentation on Ethos-U85 with ExecuTorch and validate its output on the
    Corstone-320 FVP. First, you'll prepare the model and export a quantized program with a fixed point prompt.
    Then, you'll build the standard Arm runner and pass image tensors through semihosting. Finally, you'll
    compare the host and target masks and confirm both intersection over union (IoU) checks reach `0.9`.
  faqs:
  - question: How do I know my host is supported before I start?
    answer: >-
      Run the preflight check to verify macOS 15 or later on Apple silicon, or glibc 2.28 or later on Linux.
      You'll also check the required tools, including `python3.12`, `git`, `cmake`, `c++`, and either `Ninja` or `Make`.
  - question: Which directory should I run commands from during export and build?
    answer: >-
      Run commands from the `ExecuTorch` repository root. Activate your Python environment and source
      `setup_path.sh` from the `examples/arm/arm-scratch/` directory in the current shell.
  - question: What should I expect after running the MobileSAM export step?
    answer: >-
      Prepare the pinned source and checkpoint first with `prepare_mobilesam.py`. After running
      `export_mobilesam.py` without arguments, you'll find `mobilesam.pte`, `input.bin`, host mask images,
      `metrics.json`, and `delegation.txt` under `arm_test/mobilesam/export/`. Check that
      `fp32_quantized_iou` in the metrics is at least `0.9`.
  - question: What confirms that the FVP execution worked?
    answer: >-
      Confirm successful runner execution in `arm_test/mobilesam/fvp.log` and check that
      `output-0.bin` under `arm_test/mobilesam/io/` contains the target output tensor. Then run the visualization
      step to compare the target mask with your host quantized mask. If you use the complete `run.sh`
      workflow, you'll see `MobileSAM example: PASS` after validation succeeds.
  - question: How do I validate the segmentation quality and target agreement?
    answer: >-
      Run the MobileSAM example's `visualize_fvp_output.py` without arguments, as shown in the validation
      step. Under `arm_test/mobilesam/result/`, check `fvp_reference_iou` in `metrics.json` and inspect
      `fvp_comparison.png`. You need an IoU of at least `0.9`.
      This comparison checks agreement with your host mask on the example image.
# END generated_summary_faq

author: Usamah Zaheer

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Ethos-U
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - MobileSAM
    - Python
    - CMake
    - GCC
    - FVP
operatingsystems:
    - Linux
    - macOS

further_reading:
    - resource:
        title: ExecuTorch MobileSAM prompt segmentation example
        link: https://github.com/pytorch/executorch/tree/main/examples/arm/mobilesam_prompt_segmentation_example_ethos_u
        type: repository
    - resource:
        title: ExecuTorch Arm Ethos-U backend documentation
        link: https://docs.pytorch.org/executorch/stable/embedded-arm-ethos-u.html
        type: documentation
    - resource:
        title: MobileSAM source repository
        link: https://github.com/ChaoningZhang/MobileSAM
        type: repository
    - resource:
        title: Arm Ethos-U85 NPU
        link: https://developer.arm.com/Processors/Ethos-U85
        type: documentation
    - resource:
        title: FVPs-on-Mac
        link: https://github.com/Arm-Examples/FVPs-on-Mac
        type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

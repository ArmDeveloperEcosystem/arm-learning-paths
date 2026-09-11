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
    - A Linux development machine or an Apple silicon Mac
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
    You'll prepare MobileSAM, export a quantized fixed-prompt model for Ethos-U85, and build a bare-metal
    ExecuTorch application. Then, you'll run prompt segmentation on the Corstone-320 FVP
    and save the target output. Finally, you'll reconstruct the target mask and compare it with the host quantized
    mask. You'll confirm that both validation stages meet the required intersection over union (IoU) threshold.
  faqs:
  - question: How do I know my host is supported before I start?
    answer: >-
      Run the preflight check to verify supported platforms and required
      tools, including `python3.12`, `git`, `cmake`, `c++`, and either `Ninja` or `Make`.
  - question: Which directory should I run commands from during export and build?
    answer: >-
      Run commands from the `ExecuTorch` repository root. Activate your Python environment and source
      `examples/arm/arm-scratch/setup_path.sh` in the current shell.
  - question: What should I expect after running the MobileSAM export step?
    answer: >-
      The script downloads the pinned MobileSAM revision, applies the patch for a configurable image size, and keeps
      the external source in a separate working directory. You should see exported assets referenced
      later, such as metadata under `arm_test/mobilesam_manual/export/` and a reference quantized
      mask image.
  - question: What confirms that the FVP execution worked?
    answer: >-
      The example runs on the Corstone-320 FVP and produces a log file used for validation (for
      example, `arm_test/mobilesam_manual/fvp.log`). That log contains the encoded segmentation
      mask for the visualization tool to decode.
  - question: How do I validate the segmentation quality and target agreement?
    answer: >-
      Run the visualization tool with the FVP log, the example input image, the exported metadata
      JSON, and the reference quantized mask. The tool reconstructs the target mask and checks
      that the IoU meets the specified threshold, such as `--minimum-iou=0.9`.
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

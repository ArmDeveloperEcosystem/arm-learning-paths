---
title: Deploy Silero VAD on Arm Ethos-U with ExecuTorch
description: Export a stateful Silero voice activity detection model with ExecuTorch, run it on an Arm Ethos-U85 Fixed Virtual Platform, and validate its output.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for embedded machine learning developers who want to evaluate streaming audio inference with ExecuTorch on Arm Ethos-U.

learning_objectives:
    - Set up ExecuTorch and the Arm development tools for Corstone-320 and Ethos-U85.
    - Export and quantize a stateful Silero voice activity detection (VAD) model as a .pte file.
    - Build and run a bare-metal voice activity detection application on a Corstone-320 Fixed Virtual Platform (FVP).
    - Validate simulated speech probabilities against a host-generated reference.

prerequisites:
    - A Linux host using `x86_64` or `arm64`, or an Apple silicon macOS host
    - Basic familiarity with PyTorch models and command-line development tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-09T16:42:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f56e6a716c01c38d2eb7f19f379804a0bf8d1f3faac81c75121ddb3470cfb799
  summary_generated_at: '2026-09-09T16:42:25Z'
  summary_source_hash: f56e6a716c01c38d2eb7f19f379804a0bf8d1f3faac81c75121ddb3470cfb799
  faq_generated_at: '2026-09-09T16:42:25Z'
  faq_source_hash: f56e6a716c01c38d2eb7f19f379804a0bf8d1f3faac81c75121ddb3470cfb799
  summary: >-
    You'll deploy the stateful Silero VAD model on an Arm Ethos-U85 virtual target.
    First, you'll prepare ExecuTorch, the model, and audio clips. Then, you'll build host quantized operators,
    export a `.pte` model, and create a host reference. Finally, you'll package the model and validation clip
    into a Cortex-M85 application, run it on the Corstone-320 FVP, and compare its speech decisions with
    the host reference.
  faqs:
  - question: How do I know the model export worked?
    answer: >-
      Confirm the exporter creates nonempty `.pte`, `expected_probs.bin`, and `export.log` files. Check
      that `export.log` reports both Vela subgraphs with no CPU operators.
  - question: Which CMake configuration should I use to build for Cortex-M85?
    answer: >-
      Use the `arm-baremetal` preset, then build the `install` target. Use the installed
      ExecuTorch libraries when you build the bare-metal application.
  - question: What result should I expect when running on the Corstone-320 FVP?
    answer: >-
      You get an `fvp.log` file with one `PROB` line for each 512-sample frame and `SEGMENT` lines for
      consecutive speech frames. Use the provided `grep` commands to inspect these records.
  - question: How do I validate the simulated output against the host-generated reference?
    answer: >-
      Run `compare_vad_probs.py` to compare the saved host reference with the probabilities in `fvp.log`.
      The comparison confirms the number of finite probabilities, numerical tolerance, and matching
      speech-or-silence decisions for each frame.
  - question: What should I check if I see only silence or no SEGMENT lines in the log?
    answer: >-
      Confirm that you packaged the validation audio clip and that the FVP run completed. Check the
      correct `fvp.log` file for `PROB` lines before you expect merged `SEGMENT` lines.
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
    - Python
    - CMake
    - Arm GNU Toolchain
    - Arm Fixed Virtual Platform
    - Vela
operatingsystems:
    - Linux
    - macOS
    - Baremetal

further_reading:
    - resource:
        title: ExecuTorch Arm Ethos-U backend
        link: https://docs.pytorch.org/executorch/stable/backends/arm-ethos-u/arm-ethos-u-overview.html
        type: documentation
    - resource:
        title: ExecuTorch Arm Ethos-U quantization
        link: https://docs.pytorch.org/executorch/stable/backends/arm-ethos-u/arm-ethos-u-quantization.html
        type: documentation
    - resource:
        title: Silero VAD Ethos-U example source
        link: https://github.com/pytorch/executorch/tree/main/examples/arm/silero_vad_example_ethos_u
        type: repository
    - resource:
        title: Silero VAD project
        link: https://github.com/snakers4/silero-vad
        type: website
    - resource:
        title: Ethos-U85 operator support in ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/backends/arm-ethos-u/U85_op_support.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

---
title: Optimize ExecuTorch fallback with CMSIS-NN on Cortex-M
    
description: Build an ExecuTorch 1.5.1 application from the published ExecuTorch CMSIS Pack and use CMSIS-NN kernels for Cortex-M fallback.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for embedded machine learning developers building ExecuTorch applications for Cortex-M CPUs and Ethos-U NPUs.

learning_objectives:
    - Export an ExecuTorch graph with Ethos-U, CMSIS-NN, and portable-kernel execution regions.
    - Lower quantized CPU fallback operations to CMSIS-NN-backed Cortex-M operators.
    - Trace the exported operators to selected components in the published ExecuTorch 1.5.1 and CMSIS-NN Packs.
    - Build and run the application on a Corstone-300 Ethos-U55 Fixed Virtual Platform (FVP).

prerequisites:
    - A Windows or Linux host machine, or an Apple silicon Mac running macOS 15 or later
    - Visual Studio Code installed
    - Familiarity with PyTorch
    - Basic familiarity with Cortex-M processors and Ethos-U NPUs

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-16T18:11:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5231760658ab4bce27bb5e1a7d4e422ad7b8c3ce6f2556d7641544dd3ab9fa1f
  summary_generated_at: '2026-11-16T18:11:21Z'
  summary_source_hash: 5231760658ab4bce27bb5e1a7d4e422ad7b8c3ce6f2556d7641544dd3ab9fa1f
  faq_generated_at: '2026-11-16T18:11:21Z'
  faq_source_hash: 5231760658ab4bce27bb5e1a7d4e422ad7b8c3ce6f2556d7641544dd3ab9fa1f
  summary: >-
    You'll build and validate an ExecuTorch application that runs across Ethos-U and Cortex-M,
    with CMSIS-NN accelerating its fallback convolution. First, you'll export the model for
    Cortex-M alone, then add Ethos-U delegation and identify the portable `topk` operation.
    You'll trace the exported operations to versioned CMSIS Pack components and follow the
    solution and generated AI layer into the firmware build. Finally, you'll verify the compiled
    source paths and run the application on the Corstone-300 Ethos-U55 FVP.
  faqs:
  - question: How can I tell that the initial export uses only Cortex-M?
    answer: >-
      Check that the exported graph has no `executorch_call_delegate` node. You'll see
      supported patterns lowered to `cortex_m.*` operators, while `aten.topk` remains
      portable. In this model, the quantized convolutions use CMSIS-NN, but other
      Cortex-M operators can use different implementations.
  - question: Which execution paths does the mixed model use?
    answer: >-
      Inspect the exported operator list. You'll find the stride-1 convolution
      in an Ethos-U55 delegate and the stride-4 convolution on Cortex-M55 through
      CMSIS-NN. The remaining `topk` operation uses a portable ExecuTorch CPU kernel.
  - question: How do I trace exported operations to CMSIS Pack components?
    answer: >-
      Inspect `cmsis-executorch-u55.cbuild-pack.yml` for the resolved ExecuTorch and
      CMSIS-NN Pack versions, then inspect `ai_layer/ai_layer.clayer.yml` for the
      components selected from those Packs. You'll find the Ethos-U backend,
      Cortex-M operator wrappers, CMSIS-NN library, and portable `topk` component.
  - question: How does the CMSIS project include the model and AI layer?
    answer: >-
      Inspect `cmsis-executorch-u55.csolution.yml` to see the `SSE-300-U55` target
      and its Board and AI layer references. The generated AI layer selects the runtime components of the model. The project generates `model_pte.c` from
      `model.pte`, so the bare-metal application can load the program without a
      filesystem.
  - question: What does the final FVP run verify?
    answer: >-
      `compile_commands.json` confirms that the build compiled the
      expected ExecuTorch, Ethos-U, CMSIS-NN, and portable `topk` sources. On the FVP,
      `Test_result: PASS` tells you that inference returned a nonempty output list. Check
      that the output also reports ten values. You need a reference comparison to
      assess numerical accuracy.
# END generated_summary_faq

author:
- Matt Cossins
- Kwashie Andoh

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false
test_maintenance: false

### Tags
skilllevels: Introductory
subjects: AI/ML
armips:
    - Cortex-M
    - Ethos-U
operatingsystems:
    - Linux
    - Windows
    - macOS
tools_software_languages:
    - Python
    - PyTorch
    - ExecuTorch
    - CMSIS
    - CMSIS Pack
    - CMSIS-NN
    - FVP
    - vcpkg

further_reading:
    - resource:
        title: CMSIS-Executorch example project
        link: https://github.com/Arm-Examples/CMSIS-Executorch
        type: documentation
    - resource:
        title: Published ExecuTorch CMSIS Pack
        link: https://www.keil.arm.com/packs/executorch-pytorch/overview/
        type: documentation
    - resource:
        title: ExecuTorch Arm Cortex-M backend
        link: https://docs.pytorch.org/executorch/stable/backends/arm-cortex-m/arm-cortex-m-overview.html
        type: documentation
    - resource:
        title: ExecuTorch Arm Ethos-U backend
        link: https://docs.pytorch.org/executorch/stable/backends-arm-ethos-u.html
        type: documentation
    - resource:
        title: CMSIS-Toolbox MLOps integration
        link: https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information
        type: documentation
    - resource:
        title: CMSIS-NN documentation
        link: https://arm-software.github.io/CMSIS-NN/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

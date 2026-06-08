---
title: Quantize neural upscaling models with ExecuTorch
description: Learn how to apply post-training quantization to PyTorch models using TorchAO and export INT8 models to .vgf format with the ExecuTorch Arm backend.
    
minutes_to_complete: 60

who_is_this_for: This is an advanced topic for ML developers who want to reduce latency and memory bandwidth by exporting INT8 models to the `.vgf` file format using the ExecuTorch Arm backend.

learning_objectives:
    - Explain when to use post-training quantization (PTQ) vs quantization-aware training (QAT)
    - Prepare and quantize a PyTorch model using TorchAO PT2E quantization APIs
    - Export the quantized model to TOSA and generate a model artifact with the ExecuTorch Arm backend
    - Validate the exported graph by visualizing it using Google's Model Explorer

prerequisites:
    - Basic PyTorch model training and evaluation experience
    - A development machine with Python 3.10+ and PyTorch installed that runs ExecuTorch

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:05:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 56d9d0fe9606e42281a2d2be52992c7a4b6846b208376c92e7fe3094647d1c70
  summary_generated_at: '2026-06-02T02:56:51Z'
  summary_source_hash: 56d9d0fe9606e42281a2d2be52992c7a4b6846b208376c92e7fe3094647d1c70
  faq_generated_at: '2026-06-03T00:05:22Z'
  faq_source_hash: 56d9d0fe9606e42281a2d2be52992c7a4b6846b208376c92e7fe3094647d1c70
  summary: >-
    This advanced Learning Path guides ML developers through applying post-training quantization
    (PTQ) and quantization-aware training (QAT) to PyTorch models using TorchAO PT2E APIs, then
    exporting INT8 models to the .vgf format via the ExecuTorch Arm backend. You start with a
    complete, runnable CIFAR-10-based example to generate a VGF artifact intended for Arm hardware
    with dedicated neural accelerators (NX), export to TOSA, and validate the graph using Google’s
    Model Explorer. The steps cover environment setup, PTQ and QAT workflows, and graph inspection
    to spot issues such as unexpected layout conversions. Prerequisites include basic PyTorch
    training/evaluation experience and a machine with Python 3.10+ and PyTorch that runs ExecuTorch
    on Linux, macOS, or Windows.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need basic PyTorch model training and evaluation experience and a development machine
      with Python 3.10+ and PyTorch installed that runs ExecuTorch. The path supports Linux, macOS,
      and Windows.
  - question: Should I start with PTQ or QAT in this workflow?
    answer: >-
      Start with PTQ using the end-to-end CIFAR-10 example to quickly generate a .vgf artifact
      and validate the export path. Then extend the same example with QAT to compare PTQ and QAT
      outputs using the same model and data.
  - question: Where will the .vgf files be generated, and what result should I expect?
    answer: >-
      Running the provided example produces a .vgf artifact as part of the ExecuTorch Arm backend
      export. The path uses default output directories such as ./output/ for PTQ and ./output_qat/
      for QAT.
  - question: How do I inspect the exported graph and what should I look for?
    answer: >-
      Install and launch Model Explorer with the VGF adapter, then open the .vgf files from the
      output directories. Check for unexpected layout conversions (for example, extra transpose
      operations) and operators you did not intend to run on your GPU.
  - question: Can I apply this quantization and export flow to my own model?
    answer: >-
      Yes. After running the CIFAR-10 example end to end, reuse the same PTQ (and optionally QAT)
      logic with your model and calibration data to export your own .vgf artifact.
# END generated_summary_faq

author:
- Richard Burton
- Annie Tallund

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - ExecuTorch
    - TorchAO
    - Vulkan
    - TOSA
    - NX
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: Get started with neural graphics using ML Extensions for Vulkan
        link: /learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/
        type: learningpath
    - resource:
        title: Fine-tuning neural graphics models with Model Gym
        link: /learning-paths/mobile-graphics-and-gaming/model-training-gym/
        type: learningpath
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: Arm neural technology in ExecuTorch 1.0
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/arm-neural-technology-in-executorch-1-0
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


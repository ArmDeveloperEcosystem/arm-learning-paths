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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:26:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1ef7d38456c2bfcd75d1fae357d93d6190a7133bc115ad4d5229cfb9059346e3
  summary_generated_at: '2026-08-21T17:26:13Z'
  summary_source_hash: 1ef7d38456c2bfcd75d1fae357d93d6190a7133bc115ad4d5229cfb9059346e3
  faq_generated_at: '2026-08-21T17:26:13Z'
  faq_source_hash: 1ef7d38456c2bfcd75d1fae357d93d6190a7133bc115ad4d5229cfb9059346e3
  summary: >-
    You'll use TorchAO and the ExecuTorch Arm backend to export INT8 `.vgf` artifacts from an
    image-to-image PyTorch model. First, you'll set up the Python environment and run a CIFAR-10-based PTQ
    example, then extend it with QAT. Finally, you'll inspect both exports in Model Explorer for
    layouts, operators, and tensor shapes before adapting the workflow to your model and calibration data.
  faqs:
  - question: How do I know the Arm backend export path worked?
    answer: >-
      Run the PTQ example and check `./output/` for an exported `.vgf` artifact. Then, open it in
      Model Explorer with the VGF adapter and inspect the graph.
  - question: Where should the exported .vgf files appear?
    answer: >-
      Find the PTQ export in `./output/` and the QAT export in `./output_qat/`. Open the exported
      `.vgf` files from those directories for inspection.
  - question: How should I decide between PTQ and QAT for my model?
    answer: >-
      PTQ optimizes for speed of iteration, while QAT optimizes for quality and robustness. Export
      both, inspect the graphs in Model Explorer, and compare outputs to choose a strategy that
      fits your accuracy and development needs.
  - question: What changes do I make to use my own model and data?
    answer: >-
      First, run the CIFAR-10 example to verify your environment. Then, adapt the PTQ or QAT export
      structure in `quantize_and_export_vgf.py` for your FP32 model, inference input, and representative
      calibration data or QAT fine-tuning loop.
  - question: What should I look for when inspecting the graph in Model Explorer?
    answer: >-
      Check for unexpected layout conversions, operators that you didn't intend to run on your
      GPU path, and model I/O shapes that don't match your integration. Use these findings before
      you integrate the `.vgf` artifact into your runtime.
# END generated_summary_faq

author:
    - Richard Burton
    - Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

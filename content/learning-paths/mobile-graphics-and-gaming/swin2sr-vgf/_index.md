---
title: Upscale an image with Swin2SR and Arm VGF

description: Export Swin2SR with ExecuTorch and run it through Arm VGF on your Linux host to upscale a low-resolution image and reconstruct finer detail.

minutes_to_complete: 60
lastmod: 2026-09-14

who_is_this_for: This Learning Path is for machine learning and graphics developers getting started with image super-resolution using ExecuTorch and Arm Vulkan Graph Format (VGF).

learning_objectives:
    - Prepare ExecuTorch, the Arm ML SDK for Vulkan, and a sample image.
    - Export a pretrained Swin2SR model as a VGF-backed ExecuTorch program.
    - Build the host runner and upscale a 64 × 64 image to 128 × 128.
    - Check the output dimensions and compare the result with the high-resolution reference.

prerequisites:
    - A 64-bit Linux host (AArch64 or x86_64) with a Vulkan 1.3 GPU and driver that support shaderFloat64, as required by the packaged ML SDK emulation layer
    - Python 3.12 with development headers and venv support, Git, curl, xz-utils, and a C++17 compiler
    - An internet connection to download ExecuTorch, model weights, and the Arm ML SDK dependencies
    - Basic familiarity with Python and command-line tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-05T19:42:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1da8efb1fa123c1aeb23cf8610070bd13ebb38d1fb191f33bd83b284b7b0f266
  summary_generated_at: '2026-10-05T19:42:27Z'
  summary_source_hash: 1da8efb1fa123c1aeb23cf8610070bd13ebb38d1fb191f33bd83b284b7b0f266
  faq_generated_at: '2026-10-05T19:42:27Z'
  faq_source_hash: 1da8efb1fa123c1aeb23cf8610070bd13ebb38d1fb191f33bd83b284b7b0f266
  summary: >-
    You'll set up a Linux host and sample image, export a pretrained Swin2SR ×2 model as an
    ExecuTorch program, and build a host runner for Arm VGF. Then, you'll
    upscale a 64 × 64 image to 128 × 128. Finally, you'll check the output dimensions and compare
    its reconstructed detail with the high-resolution reference.
  faqs:
  - question: How do I restore the environment if I open a new terminal?
    answer: >-
      From your `executorch` directory, run `source .venv/bin/activate` and then
      `source examples/arm/arm-scratch/setup_path.sh` before building or running the model.
  - question: Do I need to train Swin2SR or prepare calibration images?
    answer: >-
      No. You'll export a pretrained ×2 checkpoint pinned to a specific revision. The export uses
      `--quantization-mode none`, so you don't need calibration images.
  - question: Why do I need both swin2sr.pte and swin2sr.json?
    answer: >-
      The `.pte` file contains your executable model, while the `.json` file tells the image
      helper how to read the input and reconstruct the output. Keep them in the same directory
      with the same base name.
  - question: Can I use my own image with the exported program?
    answer: >-
      Yes, if your image is 64 × 64 pixels and RGB. For a different input size, export a
      matching program first. The helper doesn't resize or tile images automatically.
  - question: How do I know that the image run succeeded?
    answer: >-
      Look for `Saved super-resolved image to` in the terminal output. Check that your generated
      image is 128 × 128 RGB and shows the same scene without obvious corruption. You can
      compare it with the high-resolution reference, but the visual check isn't a quality
      benchmark or performance result.
# END generated_summary_faq

author: Usamah Zaheer

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Mali
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - Python
    - Vulkan
    - VGF
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Swin2SR VGF example source
        link: https://github.com/pytorch/executorch/tree/v1.5.1/examples/arm/super_resolution_example_vgf
        type: code
    - resource:
        title: Swin2SR pretrained model
        link: https://huggingface.co/caidas/swin2SR-classical-sr-x2-64
        type: website
    - resource:
        title: Arm ML SDK for Vulkan
        link: https://github.com/arm/ai-ml-sdk-for-vulkan
        type: documentation
    - resource:
        title: Prepare models for neural graphics with Arm neural technology
        link: /learning-paths/mobile-graphics-and-gaming/preparing-models-for-nt/
        type: learningpath
    - resource:
        title: Quantize neural upscaling models with ExecuTorch
        link: /learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/
        type: learningpath

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

---
title: Classify pet images with DeiT-Tiny and Arm VGF using ExecuTorch
description: Fine-tune DeiT-Tiny for pet breed classification, export a quantized ExecuTorch program with Arm VGF, and run inference on a Linux host.


minutes_to_complete: 120

who_is_this_for: This Learning Path is for machine learning developers who want to deploy an image classifier with ExecuTorch and Arm VGF using the machine learning (ML) SDK for Vulkan's host emulation layers.

learning_objectives:
    - Prepare ExecuTorch, the ML SDK for Vulkan, and a VGF runner on a Linux host.
    - Fine-tune DeiT-Tiny on the Oxford-IIIT Pet dataset and export a quantized VGF-backed ExecuTorch program.
    - Classify a pet image with the VGF-backed ExecuTorch program.
    - Compare the predicted breed with the dataset label and confirm VGF execution on the host.

prerequisites:
    - An Arm Linux development machine
    - A working Vulkan 1.3 or later GPU driver with `shaderFloat64` support for the packaged ML emulation layer
    - Internet access and sufficient disk space for the source code, SDK, Oxford-IIIT Pet dataset, and model checkpoints

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-30T18:00:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 15123daf094da867c4b4116eb91b79008fb0ef74f0c419a94a7ca6dac5aa18bf
  summary_generated_at: '2026-09-30T18:00:46Z'
  summary_source_hash: 15123daf094da867c4b4116eb91b79008fb0ef74f0c419a94a7ca6dac5aa18bf
  faq_generated_at: '2026-09-30T18:00:46Z'
  faq_source_hash: 15123daf094da867c4b4116eb91b79008fb0ef74f0c419a94a7ca6dac5aa18bf
  summary: >-
    You'll fine-tune DeiT-Tiny for pet breed classification, export it as a quantized VGF-backed
    ExecuTorch program, and run it on an Arm Linux host. First, you'll prepare ExecuTorch and build
    the VGF runner. You'll then train the model on the Oxford-IIIT Pet dataset and prepare its
    checkpoint for export. Finally, you'll classify a test image, decode the predicted breed, and
    confirm VGF execution.
  faqs:
  - question: Which ExecuTorch release should I use?
    answer: >-
      Use the ExecuTorch 1.5.1 release for both the Python package and the native source. This
      release uses stable PyTorch and TorchAO.
  - question: Do the Vulkan packages install my GPU’s driver?
    answer: >-
      No. The listed packages provide Vulkan libraries and tools but don't install a vendor‑specific
      driver. Ensure that your GPU’s Vulkan driver is installed and working before building and running
      the VGF runner.
  - question: What does the helper script do?
    answer: >-
      The Learning Path helper handles checkpoint compatibility, image preparation, and breed
      decoding.
  - question: How can I confirm that the export completed successfully?
    answer: >-
      Check that the exporter reports the output path in `arm_test/deit_vgf/export.log`. Then, run
      `test -s arm_test/deit_vgf/deit_quantized_vgf.pte` to confirm that the exported program exists
      and isn't empty. The log also reports the host accuracy check on 100 test images.
  - question: What should I see after preparing the input image?
    answer: >-
      You'll see the input image path, the tensor shape `[1, 3, 224, 224]`, and the dataset's
      `Expected breed`. The helper also saves `input.bin` for the runner. The expected breed is
      a reference label, not a model prediction.
# END generated_summary_faq

author: Usamah Zaheer

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - Python
    - VGF
    - Vulkan
    - CMake
    - Hugging Face
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: ExecuTorch VGF image classification example
        link: https://github.com/pytorch/executorch/tree/v1.5.1/examples/arm/image_classification_example_vgf
        type: website
    - resource:
        title: ExecuTorch Arm VGF backend documentation
        link: https://github.com/pytorch/executorch/blob/v1.5.1/docs/source/backends/arm-vgf/arm-vgf-overview.md
        type: documentation
    - resource:
        title: ML SDK for Vulkan
        link: https://github.com/arm/ai-ml-sdk-for-vulkan
        type: website
    - resource:
        title: DeiT-Tiny model card
        link: https://huggingface.co/facebook/deit-tiny-patch16-224
        type: documentation
    - resource:
        title: Oxford-IIIT Pet dataset on Hugging Face
        link: https://huggingface.co/datasets/timm/oxford-iiit-pet
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

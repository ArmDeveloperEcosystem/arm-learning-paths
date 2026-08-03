---
title: Build a multimodal retail restocking assistant on Armv9 with MNN

minutes_to_complete: 90

who_is_this_for: This Learning Path is for developers and engineers who want to run multimodal image, audio, and text models on Armv9 Linux systems using MNN as a portable, CPU-first inference runtime. It is aimed at readers who are comfortable building software from source and want a reproducible on-device workflow without quantization or heterogeneous scheduling.

description: Learn how to build MNN on an Armv9 system, run text, vision, and audio prompts with a multimodal Omni model, and combine image and audio inputs into a single-shot retail restock ticket workflow.

learning_objectives:
    - Build MNN natively on an Armv9 Linux system for multimodal inference
    - Verify a CPU-only Omni model workflow with text, vision, and audio prompts
    - Create a reproducible multimodal application flow that combines image and audio inputs into an actionable restock ticket

prerequisites:
    - An Armv9 Linux device with at least 32 GB of available disk space, for example a Radxa Orion O6
    - Familiarity with the Linux command line, Git, and building C++ projects with CMake
    - Internet access to download source code, model assets, and sample data

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:43:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: bf3183bd62b590d4930f0bcf9c9dc836bbc5206a991be7bec5e18e9c20942352
  summary_generated_at: '2026-07-29T16:43:21Z'
  summary_source_hash: bf3183bd62b590d4930f0bcf9c9dc836bbc5206a991be7bec5e18e9c20942352
  faq_generated_at: '2026-07-29T16:43:21Z'
  faq_source_hash: bf3183bd62b590d4930f0bcf9c9dc836bbc5206a991be7bec5e18e9c20942352
  summary: >-
    You'll build MNN natively on Armv9 Linux, prepare a prebuilt Omni multimodal model, and validate a
    CPU-only inference workflow. You'll compile MNN and use `llm_demo` to establish a text-only baseline. Then, you'll
    add a vision shelf audit that identifies the sparsest priority zone, and handle unclear images
    with `NOT_SURE`. Finally, you'll convert an audio prompt into a reproducible, semicolon-separated
    restock ticket.
  faqs:
  - question: How do I know the MNN build worked and the Omni model is ready?
    answer: >-
      Use the `llm_demo` binary to load the prebuilt Omni MNN model package. If the package loads without
      errors and a simple prompt produces tokens, continue to the next steps.
  - question: What should I look for in the text-only baseline output?
    answer: >-
      The baseline produces a predictable response with visible token generation. Record the output
      so you can compare behavior after adding vision and audio inputs.
  - question: What output should the vision shelf audit produce?
    answer: >-
      The audit estimates coverage for the top, middle, and bottom shelf levels. It identifies the
      sparsest priority zone and gives a short reason. If the image is unclear, it returns `NOT_SURE`.
  - question: Do I need a GPU or cloud service to run these demos on Armv9?
    answer: >-
      No. The workflow uses a native CPU-only MNN build, and the vision reasoning runs locally
      without cloud round trips.
  - question: What does the audio-to-ticket result look like and how is it used?
    answer: >-
      The result is a single-line, semicolon-separated ticket for predictable parsing and consistent
      terminal display. Combine it with the vision audit's priority zone to create an actionable
      restock ticket.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - CMake
    - CPP
    - Bash

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: MNN GitHub repository
        link: https://github.com/alibaba/MNN
        type: website
    - resource:
        title: ModelScope model hub
        link: https://modelscope.cn/models
        type: website
    - resource:
        title: KleidiAI explainer
        link: /learning-paths/cross-platform/kleidiai-explainer/
        type: website
    - resource:
        title: Install CMake
        link: /install-guides/cmake/
        type: website
    - resource:
        title: Vision LLM inference on Android with KleidiAI and MNN
        link: /learning-paths/mobile-graphics-and-gaming/vision-llm-inference-on-android-with-kleidiai-and-mnn/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

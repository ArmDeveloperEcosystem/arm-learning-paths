---
title: Build a Multimodal Retail Restocking Assistant on Armv9 With MNN

    
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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:47:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: bf3183bd62b590d4930f0bcf9c9dc836bbc5206a991be7bec5e18e9c20942352
  summary_generated_at: '2026-06-01T21:13:18Z'
  summary_source_hash: bf3183bd62b590d4930f0bcf9c9dc836bbc5206a991be7bec5e18e9c20942352
  faq_generated_at: '2026-06-02T21:47:36Z'
  faq_source_hash: bf3183bd62b590d4930f0bcf9c9dc836bbc5206a991be7bec5e18e9c20942352
  summary: >-
    This advanced Learning Path shows how to build the MNN (Mobile Neural Network) inference engine
    natively on an Armv9 Linux device and run a CPU-only Omni multimodal model. You start by verifying
    a text-only baseline to confirm the core inference path, then run local vision reasoning on
    retail shelf images to estimate coverage across top, middle, and bottom levels, identify the
    most sparse priority zone with a short reason, or return NOT_SURE when images are unclear.
    You also convert a spoken restock note into a single-line, semicolon-separated ticket and
    combine image and audio inputs into a single-shot restock workflow. Prerequisites include
    an Armv9 Linux system with 32 GB free space, command-line and CMake/Git experience, and internet
    access. Estimated time is about 90 minutes.
  faqs:
  - question: Do I need a GPU or accelerator to run the demos?
    answer: >-
      No. This Learning Path uses a native CPU-only MNN build on an Armv9 Linux system by design.
  - question: What do I need before building MNN on my Armv9 device?
    answer: >-
      You need an Armv9 Linux device with at least 32 GB of available disk space, internet access,
      and familiarity with the Linux command line, Git, and building C++ projects with CMake.
  - question: How do I confirm my MNN build and model are ready?
    answer: >-
      Verify that the llm_demo binary can load a prebuilt Omni MNN model package on your Armv9
      system. This confirms the setup needed for the text, vision, and audio demos.
  - question: What result should I expect from the text-only baseline?
    answer: >-
      A reproducible text-only inference run with a simple prompt and predictable output behavior.
      This validates the MNN runtime, the prompt input path, and token generation before adding
      vision and audio.
  - question: What outputs should I expect from the vision and audio steps, and how do they fit
      together?
    answer: >-
      The vision audit estimates shelf coverage for top, middle, and bottom levels, identifies
      the most sparse priority zone, provides a short reason, and returns NOT_SURE when the image
      is unclear. The audio step converts a spoken note into a one-line, semicolon-separated ticket.
      Together, they form a single-shot restock workflow using local image and audio inputs.
# END generated_summary_faq

author: Odin Shen

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


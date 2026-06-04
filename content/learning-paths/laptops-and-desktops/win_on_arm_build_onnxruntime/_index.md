---
title: Run Phi-3 on Windows on Arm using ONNX Runtime

description: Learn how to build ONNX Runtime with the Generate() API and run Phi-3 model inference with KleidiAI acceleration on Windows on Arm.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers looking to build ONNX Runtime for Windows on Arm (WoA) and leverage the Generate() API to run Phi-3 inference with KleidiAI acceleration.

learning_objectives: 
    - Build ONNX Runtime and enable the Generate() API for Windows on Arm.
    - Run inference with a Phi-3 model using ONNX Runtime with KleidiAI acceleration.
prerequisites:
    - A Windows on Arm computer such as a Lenovo Thinkpad X13 running Windows 11, or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:29:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 606702e7afc9a29976d027eceab021570cf3f91ec408ef2dd2051df0b05d9bda
  summary_generated_at: '2026-06-01T22:17:48Z'
  summary_source_hash: 606702e7afc9a29976d027eceab021570cf3f91ec408ef2dd2051df0b05d9bda
  faq_generated_at: '2026-06-02T23:29:03Z'
  faq_source_hash: 606702e7afc9a29976d027eceab021570cf3f91ec408ef2dd2051df0b05d9bda
  summary: >-
    This Learning Path shows how to build ONNX Runtime with the Generate() API on Windows on Arm
    and run inference on the Phi-3 Mini (3.3B) model with KleidiAI acceleration. You will clone
    and build ONNX Runtime and the Generate() API from source using Visual Studio and CMake, then
    download the short-context (4K) Phi-3 Mini ONNX model (quantized to 4-bits) and execute a
    simple model runner that reports performance metrics. The target environment is a Windows
    on Arm device or a Windows on Arm virtual machine. Tools used include Visual Studio, C++,
    Python, Git, CMake, and ONNX Runtime. Outcome: a working build and a validated Phi-3 inference
    run on WoA.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to a Windows on Arm computer such as a Lenovo ThinkPad X13 running Windows
      11, or a Windows on Arm virtual machine. No other explicit prerequisites are listed.
  - question: Which Phi-3 model variant should I use in this path?
    answer: >-
      Use the short-context (4K) Phi-3 Mini (3.3B) model in ONNX format, quantized to 4-bits.
      This version consumes less memory than the long-context (128K) model and is the variant
      used in the steps.
  - question: How is the ONNX Runtime Generate() API used here?
    answer: >-
      You build the Generate() API from source and use it for text generation with Phi-3. It handles
      pre- and post-processing, inference with ONNX Runtime (including logits processing), search
      and sampling, and KV cache management.
  - question: How do I know the build and run were successful?
    answer: >-
      You should be able to run the simple model runner without build errors, see generated model
      outputs, and observe reported performance metrics. These results indicate a successful build
      and inference run.
  - question: Do I need extra configuration to use KleidiAI acceleration?
    answer: >-
      The path runs inference with KleidiAI acceleration, but specific configuration steps beyond
      building ONNX Runtime and the Generate() API are not explicitly listed. Follow the provided
      build and run instructions.
# END generated_summary_faq

author: Barbara Corriero

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Visual Studio
    - CPP
    - Python
    - Git
    - CMake
    - ONNX Runtime
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: ONNX Runtime
        link: https://onnxruntime.ai/docs/
        type: documentation
    - resource:
        title: ONNX Runtime Generate() API
        link: https://onnxruntime.ai/docs/genai/
        type: documentation
    - resource:
        title: Accelerating AI Developer Innovation Everywhere with New Arm Kleidi
        link: https://newsroom.arm.com/blog/arm-kleidi
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


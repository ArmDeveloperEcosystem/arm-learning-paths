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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:20:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d2843e64b8d2ade9644f494a35c60bdf690b5718e2d395d8842b4eb65ade36ad
  summary_generated_at: '2026-08-11T16:20:41Z'
  summary_source_hash: d2843e64b8d2ade9644f494a35c60bdf690b5718e2d395d8842b4eb65ade36ad
  faq_generated_at: '2026-08-11T16:20:41Z'
  faq_source_hash: d2843e64b8d2ade9644f494a35c60bdf690b5718e2d395d8842b4eb65ade36ad
  summary: >-
    You'll build ONNX Runtime and the `Generate()` API from source on Windows on Arm, then run Phi-3
    Mini (3.3B) inference with KleidiAI acceleration.
    You configure a WoA development environment, compile the ONNX Runtime inference engine, and
    add the `Generate()` API that implements the generative text loop including preprocessing, sampling,
    and KV cache management. You'll download the Phi-3 Mini short-context (4K) ONNX model and run a model runner that prints generated text and performance
    metrics. By the end, you can execute Phi-3 text generation on WoA and recognize successful
    output and reported metrics.
  faqs:
  - question: Which Phi-3 model variant should I use for this path?
    answer: >-
      Use the Phi-3 Mini (3.3B) short-context (4K) ONNX model, which is quantized to 4 bits.
  - question: How do I know ONNX Runtime built correctly for Windows on Arm?
    answer: >-
      Confirm the build completes without errors and produces the expected binaries for WoA. If
      the build succeeds, proceed to build the `Generate()` API and run the model runner.
  - question: How can I confirm the Generate() API is available in my setup?
    answer: >-
      Build the `onnxruntime-genai` source and use the provided runner to generate text. Successful
      text generation indicates the `Generate()` API is correctly integrated.
  - question: What result should I expect when running the model runner?
    answer: >-
      Expect generated text from the Phi-3 Mini model along with performance metrics printed by
      the runner. If output appears without errors, continue to experiment with prompts.
  - question: Do I need to configure KleidiAI separately?
    answer: >-
      No. The path builds and runs ONNX Runtime with KleidiAI acceleration, and it doesn't list any
      additional KleidiAI configuration.
# END generated_summary_faq

author: Barbara Corriero

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

---
title: Accelerate Generative AI workloads using KleidiAI 
description: Learn how to use KleidiAI micro-kernels to accelerate AI inference performance through optimized matrix multiplication on Arm processors with architecture features like i8mm.
minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to learn how to use KleidiAI to accelerate the execution of Generative AI workloads on hardware.

learning_objectives: 
    - Describe how basic math operations power Large Language Models.
    - Describe how the KleidiAI micro-kernels speed up Generative AI inference performance.
    - Run a basic C++ matrix multiplication example to showcase the speedup that KleidiAI micro-kernels can deliver.

prerequisites:
    - An Arm-based Linux machine that implements the Int8 Matrix Multiplication (*i8mm*) architecture feature. The example in this Learning Path is run on an AWS Graviton 3 instance. Instructions on setting up an Arm-based server are [found here](/learning-paths/servers-and-cloud-computing/csp/aws/).
    - A basic understanding of linear algebra terminology, such as dot product and matrix multiplication.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:38:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 907255b3c2c1086b421abe4a1e378b68533de4524a4f4dd81138545a2ff1a5b5
  summary_generated_at: '2026-07-29T16:38:55Z'
  summary_source_hash: 907255b3c2c1086b421abe4a1e378b68533de4524a4f4dd81138545a2ff1a5b5
  faq_generated_at: '2026-07-29T16:38:55Z'
  faq_source_hash: 907255b3c2c1086b421abe4a1e378b68533de4524a4f4dd81138545a2ff1a5b5
  summary: >-
    You'll explore KleidiAI micro-kernels on Arm CPUs and see how matrix multiplication supports generative
    AI workloads. You'll locate the `matmul` kernels and packing and quantization routines in the KleidiAI
    GitLab repository, review the architecture, and identify when a framework can invoke i8mm kernels.
    Then, you'll run a C++ example that exercises the i8mm kernel and its supporting data path, so you can
    trace the optimized execution directly.
  faqs:
  - question: How do I know if my ML framework will use KleidiAI automatically?
    answer: >-
      Your framework uses KleidiAI automatically when it integrates KleidiAI and your hardware
      supports the required Arm instructions, such as i8mm. If either condition is missing, run the
      standalone example to observe the micro-kernel behavior directly.
  - question: Where in the KleidiAI repository are the relevant micro-kernels?
    answer: >-
      Open `/kai/ukernels/matmul` in the KleidiAI GitLab repository. The `pack` directory contains
      quantization and packing routines. Adjacent directories contain the matrix multiplication
      routines.
  - question: Which example should I review to understand the i8mm execution path?
    answer: >-
      Open the KleidiAI example that demonstrates the i8mm matrix multiplication micro-kernel with
      its packing and quantization routines. The steps identify the example before you run it.
  - question: What should I expect when the C++ example runs successfully?
    answer: >-
      The example exercises the i8mm matmul micro-kernel with its packing and quantization steps.
      It demonstrates the micro-kernel data path and performance, not framework integration.
  - question: What should I check if I don’t observe the expected acceleration?
    answer: >-
      Verify that your hardware implements the required Arm instructions, such as i8mm, and that
      your software selects the optimized kernels. If you use a framework, confirm that it integrates
      KleidiAI. Otherwise, run the standalone example to validate the micro-kernel path.
# END generated_summary_faq

author: Zach Lasiuk

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory 
subjects: ML
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - CPP
    - Generative AI
    - Neon
    - Runbook

operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: KleidiAI documentation
        link: https://gitlab.arm.com/kleidi/kleidiai/-/blob/main/docs/matmul_qsi4cx/README.md?ref_type=heads
        type: documentation
    - resource:
        title: KleidiAI visualized
        link: https://community.arm.com/arm-community-blogs/b/ai-and-ml-blog/posts/kleidiai
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

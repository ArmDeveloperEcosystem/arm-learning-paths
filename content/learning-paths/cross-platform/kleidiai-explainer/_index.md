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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:44:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 907255b3c2c1086b421abe4a1e378b68533de4524a4f4dd81138545a2ff1a5b5
  summary_generated_at: '2026-06-01T21:09:31Z'
  summary_source_hash: 907255b3c2c1086b421abe4a1e378b68533de4524a4f4dd81138545a2ff1a5b5
  faq_generated_at: '2026-06-02T21:44:03Z'
  faq_source_hash: 907255b3c2c1086b421abe4a1e378b68533de4524a4f4dd81138545a2ff1a5b5
  summary: >-
    This introductory path shows how KleidiAI micro-kernels accelerate Generative AI inference
    on Arm CPUs by optimizing matrix multiplication using architecture features such as Int8 Matrix
    Multiplication (i8mm). You will explore the KleidiAI GitLab repository, review the organization
    of quantizing/packing and matmul micro-kernels under /kai/ukernels/matmul, and run a basic
    C++ matrix multiplication example that highlights the i8mm micro-kernel and its supporting
    routines. The path also connects core linear algebra operations to how Large Language Models
    execute. It targets Arm-based Linux systems with i8mm; the example is run on an AWS Graviton
    3 instance. By the end, you can explain where KleidiAI fits in a software stack and demonstrate
    its micro-kernel speedup using the provided example. Prerequisites include an Arm-based Linux
    machine with i8mm and basic linear algebra knowledge.
  faqs:
  - question: What do I need before running the example?
    answer: >-
      You need an Arm-based Linux machine that implements the Int8 Matrix Multiplication (i8mm)
      feature; the example is run on an AWS Graviton 3 instance. Instructions on setting up an
      Arm-based server are found here: /learning-paths/servers-and-cloud-computing/csp/aws/. A
      basic understanding of dot product and matrix multiplication is also required.
  - question: How do I know if my ML framework will use KleidiAI automatically?
    answer: >-
      If your ML framework integrates KleidiAI and your hardware supports the required Arm instructions
      for your inference, you will benefit from KleidiAI without any further action. Both conditions
      must be met.
  - question: Where do I find the relevant micro-kernels in the KleidiAI repository?
    answer: >-
      Navigate to the KleidiAI GitLab repository and go to /kai/ukernels/matmul. Quantizing/packing
      routines are in the pack directory, and matrix multiplication routines are in the remaining
      subdirectories there.
  - question: What should I expect when I run the C++ matrix multiplication example?
    answer: >-
      The example highlights the i8mm matrix multiplication micro-kernel along with the enabling
      quantizing/packing micro-kernels. It is designed to showcase KleidiAI micro-kernel performance
      rather than require changes to your ML framework.
  - question: Do I need to modify my ML stack or write assembly to use KleidiAI?
    answer: >-
      No. KleidiAI micro-kernels are hand-optimized in Arm assembly, but in practice your ML framework
      will leverage them automatically if supported. This Learning Path uses a standalone example
      to illustrate how the micro-kernels work.
# END generated_summary_faq

author: Zach Lasiuk
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


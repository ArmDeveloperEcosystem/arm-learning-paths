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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:15Z'
  generator: template
  source_hash: 907255b3c2c1086b421abe4a1e378b68533de4524a4f4dd81138545a2ff1a5b5
  summary: >-
    Learn how to use KleidiAI micro-kernels to accelerate AI inference performance through optimized
    matrix multiplication on Arm processors with architecture features like i8mm. It is designed
    for developers who want to learn how to use KleidiAI to accelerate the execution of Generative
    AI workloads on hardware. By the end, you will be able to describe how basic math operations
    power Large Language Models, describe how the KleidiAI micro-kernels speed up Generative AI
    inference performance, and run a basic C++ matrix multiplication example to showcase the speedup
    that KleidiAI micro-kernels can deliver. It focuses on tools and technologies such as CPP,
    Generative AI, Neon, and Runbook, Linux environments, and Arm platforms including Cortex-A
    and Neoverse. The main steps cover KleidiAI and matrix multiplication, KleidiAI in a real
    software stack, and Quantizing and packing micro-kernels.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe how basic math operations power Large Language Models, describe how the
      KleidiAI micro-kernels speed up Generative AI inference performance, and run a basic C++
      matrix multiplication example to showcase the speedup that KleidiAI micro-kernels can deliver.
      Learn how to use KleidiAI micro-kernels to accelerate AI inference performance through optimized
      matrix multiplication on Arm processors with architecture features like i8mm.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers who want to learn how to use KleidiAI to accelerate
      the execution of Generative AI workloads on hardware.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm-based Linux machine that implements
      the Int8 Matrix Multiplication (*i8mm*) architecture feature. The example in this Learning
      Path is run on an AWS Graviton 3 instance. Instructions on setting up an Arm-based server
      are [found here](/learning-paths/servers-and-cloud-computing/csp/aws/).; A basic understanding
      of linear algebra terminology, such as dot product and matrix multiplication.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including CPP, Generative AI, Neon, and Runbook, Linux environments,
      and Arm platforms such as Cortex-A and Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around KleidiAI and matrix multiplication, KleidiAI in a
      real software stack, and Quantizing and packing micro-kernels.
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


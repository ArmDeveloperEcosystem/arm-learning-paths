---
title: Understand KleidiAI SME2 matmul microkernels
    
minutes_to_complete: 40

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners.

learning_objectives: 
    - Explain how a KleidiAI microkernel performs matrix multiplication (matmul) with quantized data
    - Identify how SME2 INT8 MOPA (matrix outer product accumulate) instructions map to matmul work
    - Trace how quantization and packing feed an SME2 matmul microkernel (using GGML Q4_0 and llama.cpp call stacks as a concrete example)
    - Perform basic hands-on checks (source inspection and optional disassembly) to confirm where SME2 instructions appear

prerequisites:
    - Basic understanding of general matrix multiplication (GEMM) and matmul operations
    - Basic understanding of quantization concepts for neural networks
    - (Optional) Access to an Arm CPU with SME2 support (Linux or Android) for hands-on verification steps

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: 5a94138f74e7b2266c35dbd555f9966ca0ff29fdbd1842d4724e0da0cd4e46db
  summary: >-
    Understand KleidiAI SME2 matmul microkernels walks you through an end-to-end Arm software
    workflow. It is designed for software developers, performance engineers, and AI practitioners.
    By the end, you will be able to explain how a KleidiAI microkernel performs matrix multiplication
    (matmul) with quantized data, identify how SME2 INT8 MOPA (matrix outer product accumulate)
    instructions map to matmul work, and trace how quantization and packing feed an SME2 matmul
    microkernel (using GGML Q4_0 and llama.cpp call stacks as a concrete example). It focuses
    on tools and technologies such as C++, KleidiAI, llama.cpp, and SME2, Android and Linux environments,
    and Arm platforms including Arm C1. The main steps cover Overview and setup, Matmul tiling
    and packing, SME2 INT8 MOPA for matmul, Decode the SME2 matmul microkernel, and Repack RHS
    weights (GGML Q4_0).
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will explain how a KleidiAI microkernel performs matrix multiplication (matmul) with
      quantized data, identify how SME2 INT8 MOPA (matrix outer product accumulate) instructions
      map to matmul work, and trace how quantization and packing feed an SME2 matmul microkernel
      (using GGML Q4_0 and llama.cpp call stacks as a concrete example).
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers, performance engineers, and AI practitioners.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Basic understanding of general matrix
      multiplication (GEMM) and matmul operations; Basic understanding of quantization concepts
      for neural networks; (Optional) Access to an Arm CPU with SME2 support (Linux or Android)
      for hands-on verification steps.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including C++, KleidiAI, llama.cpp, and SME2, Android and
      Linux environments, and Arm platforms such as Arm C1.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview and setup, Matmul tiling and packing, SME2
      INT8 MOPA for matmul, Decode the SME2 matmul microkernel, and Repack RHS weights (GGML Q4_0).
# END generated_summary_faq

author: Zenon Zhilong Xiu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1
tools_software_languages:
    - C++
    - KleidiAI
    - llama.cpp
    - SME2
operatingsystems:
    - Android
    - Linux



further_reading:
    - resource:
        title: Part 1, Arm Scalable Matrix Extension introduction
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Part 2, Arm Scalable Matrix Extension instructions
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: Part 4 Arm SME2 introduction
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: blog
    - resource:
        title: Profile llama.cpp performance with Arm Streamline and KleidiAI LLM kernels
        link: /learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
        type: blog
        


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


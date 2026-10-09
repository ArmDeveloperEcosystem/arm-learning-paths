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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:05:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3a0a9c01e8e7fb6ccb1df84d3f131679987196fb5b94a2ad22731c5ba5bfd90f
  summary_generated_at: '2026-08-17T22:05:12Z'
  summary_source_hash: 3a0a9c01e8e7fb6ccb1df84d3f131679987196fb5b94a2ad22731c5ba5bfd90f
  faq_generated_at: '2026-08-17T22:05:12Z'
  faq_source_hash: 3a0a9c01e8e7fb6ccb1df84d3f131679987196fb5b94a2ad22731c5ba5bfd90f
  summary: >-
    You'll examine how a KleidiAI SME2 INT8 MOPA microkernel performs quantized matrix multiplication
    on Arm CPUs. First, you'll learn how tiling and packing parameters control the kernel, decode its name, and
    interpret its work unit. Then, you'll follow a `GGML Q4_0` example and inspect source or disassembly to
    identify the SME2 instructions.
  faqs:
  - question: Do I need an SME2-capable Arm CPU to complete the Learning Path?
    answer: >-
      No. SME2 hardware is only required for the optional hands-on verification steps. 
  - question: How do I know the microkernel is using SME2 INT8 MOPA in the inner loop?
    answer: >-
      Inspect the microkernel's inner loop for SME2 outer product accumulate instructions that
      update the ZA storage. Optional disassembly can also confirm where these instructions appear.
  - question: What do mr, nr, bl, and kr affect when preparing inputs?
    answer: >-
      These tiling and block parameters define the output tile shape and how many K elements are
      processed per step. Pack A and B so their layouts align with these increments and the kernel’s
      access pattern.
  - question: What does 1vlx4vl indicate in the kernel name?
    answer: >-
      It indicates that one inner-loop iteration computes an intermediate 1VL by 4VL submatrix
      of the output. The actual element counts depend on the device’s SME2 streaming vector length.
  - question: What should I expect after repacking GGML Q4_0 weights for the example matmul?
    answer: >-
      The RHS buffer layout changes to the format expected by the SME2 microkernel so the inner
      loop can stream data efficiently. The kernel then consumes the packed weights without additional
      rearrangement.
# END generated_summary_faq

author: Zenon Zhilong Xiu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1
tools_software_languages:
    - CPP
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

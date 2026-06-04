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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:54:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5a94138f74e7b2266c35dbd555f9966ca0ff29fdbd1842d4724e0da0cd4e46db
  summary_generated_at: '2026-06-02T02:50:20Z'
  summary_source_hash: 5a94138f74e7b2266c35dbd555f9966ca0ff29fdbd1842d4724e0da0cd4e46db
  faq_generated_at: '2026-06-02T23:54:55Z'
  faq_source_hash: 5a94138f74e7b2266c35dbd555f9966ca0ff29fdbd1842d4724e0da0cd4e46db
  summary: >-
    This advanced Learning Path explains how KleidiAI implements matrix multiplication microkernels
    for quantized inference on Arm CPUs using SME2 INT8 MOPA instructions. You will decode a specific
    SME2 matmul microkernel, understand its tiling and packing parameters (mr, nr, bl, kr), and
    trace how quantized GGML Q4_0 weights from llama.cpp are repacked and consumed. Using a simplified
    example with FP32 activations [16,64] and Q4_0 weights [64,64], you will connect normal matmul
    semantics to the SME2 inner loop and see where MOPA instructions appear. Optional hands-on
    steps include source inspection and disassembly on Linux or Android systems with SME2 support.
    Prerequisites are basic GEMM/matmul and quantization knowledge; no other explicit prerequisites
    are listed.
  faqs:
  - question: Do I need a device with SME2 support to follow this Learning Path?
    answer: >-
      No. SME2-capable hardware is optional and only required for the hands-on verification steps
      such as disassembly. The core explanations and examples can be followed without hardware.
  - question: How do I verify that SME2 INT8 MOPA instructions are used in the microkernel?
    answer: >-
      The path shows where these instructions appear in the inner loop and suggests basic checks
      via source inspection. If you have SME2 hardware, you can optionally confirm via disassembly.
  - question: Which llama.cpp operations route through the SME2 matmul microkernel in this context?
    answer: >-
      The heavy matmul work in attention (K/Q/V projections) and feed-forward network (FFN) layers
      can run through the SME2 matmul microkernel. In these cases, the LHS activations are FP32
      and the RHS weights use GGML Q4_0.
  - question: Which tiling and packing parameters should I pay attention to?
    answer: >-
      Focus on mr, nr, bl, and kr, which define the output tile shape and inner-loop step sizes.
      The microkernel computes C in tiles and expects inputs to be quantized and packed accordingly.
  - question: What SVL and matrix sizes does the example assume, and how do I interpret 1vlx4vl?
    answer: >-
      The example assumes an SME2 streaming vector length (SVL) of 512 bits and a simplified matmul
      of LHS [16, 64] by RHS [64, 64]. The 1vlx4vl suffix means each inner-loop iteration computes
      a 1VL × 4VL submatrix of the output, with exact element counts depending on the hardware
      SVL.
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


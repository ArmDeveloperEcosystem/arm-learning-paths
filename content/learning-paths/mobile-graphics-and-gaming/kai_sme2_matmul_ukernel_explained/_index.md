---
title: Understand KleidiAI SME2 matmul microkernels

draft: true
cascade:
    draft: true
    
minutes_to_complete: 40

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners.

learning_objectives: 
    - Explain how a KleidiAI microkernel performs matrix multiplication (matmul) with quantized data
    - Identify how SME2 INT8 MOPA (matrix outer product accumulate) instructions map to matmul work
    - Trace how quantization and packing feed an SME2 matmul microkernel (using GGML Q4_0 and llama.cpp call stacks as a concrete example)
    - Perform basic hands-on checks (source inspection and optional disassembly) to confirm where SME2 instructions appear

prerequisites:
    - Familiarity with basic GEMM/matmul and quantization concepts
    - (Optional) Access to an Arm CPU with SME2 support (Linux or Android) for the "run on device" steps

author: Zenon Zhilong Xiu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1 core
    - SME2
tools_software_languages:
    - C++
    - KleidiAI
    - llama.cpp
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
        title: Part 4, Arm SME2 introduction
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

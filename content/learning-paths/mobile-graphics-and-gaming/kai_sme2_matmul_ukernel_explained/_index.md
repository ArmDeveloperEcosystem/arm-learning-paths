---
title: KleidiAI SME2 matmul microkernel for quantized models explained

minutes_to_complete: 40

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners 

learning_objectives: 
    - Learn how a KleidiAI matmual microkernel performs matrix multiplication with quantized data
    - Learn how SME2 INT8 Outer Product Accumulate instructions are used for matrix multiplication
    - Learn how a KleidiAI SME2 matmul microkernel accelerates matmul operators in a Large Lanague Model
    - Learn how to integrate KleidiAI SME2 matmul microkernels to an AI framework or application

prerequisites:
    - Knowledge of KleidiAI and SME2

author: Zenon Zhilong Xiu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1 CPU
    - Arm SME2 unit
tools_software_languages:
    - C++
    - KleidiAI
    - llama.cpp
operatingsystems:
    - Android
    - Linux



further_reading:
    - resource:
        title: part 1 Arm Scalable Matrix Extension Introduction 
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: part 2 Arm Scalable Matrix Extension Instructions 
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: part4 Arm SME2 Introduction 
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: blog
    - resource:
        title: Profile llama.cpp performance with Arm Streamline and KleidiAI LLM kernels
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
        type: blog
        


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
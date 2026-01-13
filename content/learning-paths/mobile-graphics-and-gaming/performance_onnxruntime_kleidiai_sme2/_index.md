---
title: Profile ONNX model performance with SME2 using KleidiAI and ONNX Runtime



minutes_to_complete: 40

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners. 

learning_objectives: 
    - Build ONNX Runtime with KleidiAI and SME2 support for Android
    - Profile ONNX model performance using benchmark tools
    - Analyze how KleidiAI kernels accelerate ONNX operators with SME2
    - Compare performance improvements between standard and SME2-optimized execution

prerequisites:
    - An Android device with Arm SME2 support
    - Basic understanding of machine learning model inference
    - Familiarity with Android NDK and cross-compilation

author: Zenon Zhilong Xiu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1 CPU
    - Arm SME2 unit
tools_software_languages:
    - C++
    - ONNX Runtime
operatingsystems:
    - Android
    - Linux



further_reading:
    - resource:
        title: Arm Scalable Matrix Extension Introduction (Part 1)
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Arm Scalable Matrix Extension Instructions (Part 2)
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: Arm SME2 Introduction (Part 4)
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: blog
        


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
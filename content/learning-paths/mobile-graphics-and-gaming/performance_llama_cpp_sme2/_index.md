---
title: Profile SME2 with llama.cpp and KleidiAI on Android

draft: true
cascade:
    draft: true
    
minutes_to_complete: 40

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners 

learning_objectives: 
    - Build llama.cpp library with KleidiAI and SME2 support
    - Profile performance of LLMs running on llama-cli
    - Learn how KleidiAI and SME2 accelerates LLM operators

prerequisites:
    - Knowledge of KleidiAI and SME2
    - A Linux host machine (x86_64 or aarch64) for building llama.cpp with the Arm GNU Toolchain used in this Learning Path
    - Git, CMake and Android Debug Bridge (ADB) installed on the host machine
    - An Android device with Arm SME2 support for running and profiling the built executable

author: Zenon Zhilong Xiu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1 core
    - SME2
tools_software_languages:
    - C++
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

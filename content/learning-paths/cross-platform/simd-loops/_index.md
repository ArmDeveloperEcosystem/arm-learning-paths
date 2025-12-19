---
title: "Code kata: perfect your SVE and SME skills with SIMD Loops"

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who want to learn how to use the full range of features available in SVE, SVE2, and SME2 to improve software performance on Arm processors.

learning_objectives:
     - Improve SIMD code performance using Scalable Vector Extension (SVE) and Scalable Matrix Extension (SME)
     - Describe what SIMD Loops contains and how kernels are organized across scalar, NEON, SVE,SVE2, and SME2 variants
     - Build and run a selected kernel with the provided runner and validate correctness against the C reference
     - Choose the appropriate build target to compare NEON, SVE/SVE2, and SME2 implementations


prerequisites:
    - An AArch64 computer running Linux or macOS. You can use cloud instances, refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) for a list of cloud service providers. 
    - Some familiarity with SIMD programming and NEON intrinsics.
    - Recent toolchains that support SVE/SME (GCC 13+ or Clang 16+ recommended)

author:
    - Alejandro Martinez Vicente
    - Mohamad Najem

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
  - C
  - C++
  - GCC
  - Clang

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming
    - automotive

further_reading:
    - resource:
        title: SVE Programming Examples
        link: https://developer.arm.com/documentation/dai0548/latest
        type: documentation
    - resource:
        title: Port Code to Arm Scalable Vector Extension (SVE)
        link: /learning-paths/servers-and-cloud-computing/sve
        type: website
    - resource:
        title: Introducing the Scalable Matrix Extension for the Armv9-A Architecture
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture
        type: website
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 1)
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 2)
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: (Part 3) Matrix-matrix multiplication. Neon, SVE, and SME compared
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/matrix-matrix-multiplication-neon-sve-and-sme-compared
        type: blog
    - resource:
        title: Build adaptive libraries with multiversioning
        link: /learning-paths/cross-platform/function-multiversioning/
        type: website
    - resource:
        title: SME Programmer's Guide
        link: https://developer.arm.com/documentation/109246/latest
        type: documentation
    - resource:
        title: Compiler Intrinsics
        link: https://en.wikipedia.org/wiki/Intrinsic_function
        type: website
    - resource:
        title: ACLE - Arm C Language Extension
        link: https://github.com/ARM-software/acle
        type: website
    - resource:
        title: Application Binary Interface for the Arm Architecture
        link: https://github.com/ARM-software/abi-aa
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

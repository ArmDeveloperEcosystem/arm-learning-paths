---
title: Explore SME matrix operations with interactive visualizations
description: Explore nine interactive views of ZA layout, transposition, operand preparation, and matrix multiplication to understand Arm SME data movement.

draft: true
cascade:
    draft: true
    
minutes_to_complete: 40

who_is_this_for: This is an introductory topic for software developers who want to understand how Arm SME moves matrix data before they read or write SME2 code.

learning_objectives:
    - Understand how ZA storage and ZA tiles are affected by Streaming Vector Length and data element size.
    - Explore transposition, packing, and padding to optimize memory layout.
    - Compare three matrix multiplication implementations and explain how their input layouts affect data movement efficiency.

prerequisites:
    - A browser with JavaScript enabled
    - Basic familiarity with vectors and matrix multiplication

author:
    - Chris Sidebottom
    - Andrew Pickard

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Arm C1
tools_software_languages:
    - SME2

operatingsystems:
    - Linux
    - macOS
    - Windows

### Cross-platform metadata only
shared_path: true
shared_between:
    - mobile-graphics-and-gaming
    - laptops-and-desktops

further_reading:
    - resource:
        title: Arm SME and SME2 Programmer's Guide
        link: https://developer.arm.com/documentation/109246/latest
        type: documentation
    - resource:
        title: Accelerate matrix multiplication performance with SME2
        link: /learning-paths/cross-platform/multiplying-matrices-with-sme2/
        type: website
    - resource:
        title: Matrix-matrix multiplication with Neon, SVE, and SME compared
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/matrix-matrix-multiplication-neon-sve-and-sme-compared
        type: blog
    - resource:
        title: 'SME2 from scratch: Build matrix multiplication'
        link: https://www.youtube.com/watch?v=5peYlm5j0U8
        type: video

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

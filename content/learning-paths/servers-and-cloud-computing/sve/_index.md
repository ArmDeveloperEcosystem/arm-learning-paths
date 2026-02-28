---
title: Port Code to Arm Scalable Vector Extension (SVE)

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers using SIMD instructions for High-Performance Computing, Machine Learning, Digital Signal Processing, Audio and Video Codec applications.

learning_objectives: 
    - Understand the differences between SVE and NEON for vectorization
    - Compile code for SVE-capable Arm processors
    - Run SVE instructions on any Armv8-A processor

prerequisites:
    - General knowledge about SIMD processing, vectorization or Arm NEON.
    - An Arm computer running Linux. Cloud instances can be used, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

author: Florent Lebeau

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - SVE
    - NEON
    - armie
    - GCC
    - armclang
    - Runbook

further_reading:
    - resource:
        title: Introduction to SVE
        link: https://developer.arm.com/documentation/102476/latest/
        type: website
    - resource:
        title: SVE Optimization Guide
        link: https://developer.arm.com/documentation/102699/0100/?lang=en
        type: documentation
    - resource:
        title: Tutorials - Introduction to SVE2
        link: https://developer.arm.com/documentation/102340/0001/?lang=en
        type: documentation
    - resource:
        title: Arm Instruction Emulator user guide
        link: https://developer.arm.com/documentation/102190/22-0/Get-started/Get-started-with-Arm-Instruction-Emulator
        type: documentation
    - resource:
        title: Accelerating DSP functions with dot product instructions
        link: https://developer.arm.com/documentation/102651/a/?lang=en
        type: documentation
    - resource:
        title: Optimizing HPCG for Arm SVE
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/optimizing-hpcg-for-arm-sve
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

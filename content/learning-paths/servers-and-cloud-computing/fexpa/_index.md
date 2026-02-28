---
title: Optimize exponential functions with FEXPA

    
minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers interested in accelerating exponential function computations using Arm's Scalable Vector Extension (SVE). The FEXPA instruction provides hardware acceleration for exponential calculations on Arm Neoverse processors.

learning_objectives: 
    - Implement the exponential function using SVE intrinsics
    - Optimize the function with FEXPA

prerequisites:
    - Access to an [AWS Graviton4, Google Axion, or Azure Cobalt 100 virtual machine from a cloud service provider](/learning-paths/servers-and-cloud-computing/csp/)
    - Some familiarity with SIMD programming and SVE intrinsics

author: 
- Arnaud Grasset
- Claudio Martino
- Alexandre Romana

further_reading:
    - resource:
        title: Arm Optimized Routines
        link: https://github.com/ARM-software/optimized-routines
        type: website
    - resource:
        title: Scalable Vector Extensions documentation
        link: https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions
        type: documentation
    - resource:
        title: FEXPA documentation
        link: https://developer.arm.com/documentation/ddi0602/2025-12/SVE-Instructions/FEXPA--Floating-point-exponential-accelerator-?lang=en
        type: documentation

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
armips:
    - Neoverse
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - C
    - CPP

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


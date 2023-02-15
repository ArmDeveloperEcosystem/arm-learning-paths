---
title: Port Code to Arm Scalable Vector Extension (SVE)

description: Learning path for porting code from Arm NEON to the Scalable Vector Extension (SVE)

minutes_to_complete: 20   

who_is_this_for: This is an introductory topic for software developers using SIMD instructions for High-Performance Computing, Machine Learning, Digital Signal Processing, Audio and Video Codec applications.

learning_objectives: 
    - Understand the differences between SVE and NEON for vectorization
    - Compile code for SVE-capable Arm processors
    - Run SVE instructions on any Armv8-A processor

prerequisites:
    - General knowledge about SIMD processing, vectorization or Arm NEON.
    - An Arm computer running Linux. Cloud instances can be used, refer to the list of [Arm cloud service providers](/learning-paths/server-and-cloud/csp/).

author_primary: Florent Lebeau

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
    - Cortex-A75
    - Cortex-A55
operatingsystems:
    - Linux
tools_software_languages:
    - C
    - Assembly
    - GCC
    - Armclang

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

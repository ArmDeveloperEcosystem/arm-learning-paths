---
title: Learn about function multiversioning

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers interested in optimizing their C/C++ applications across Arm64 targets.

description: Learn how to optimize C/C++ applications using function multiversioning on Arm64 targets with GCC or LLVM, enabling automatic runtime selection of hardware-optimized function versions.

learning_objectives:
    - Use hardware features to tune your applications at function level.
    - Create multiple versions of C/C++ functions for the targets that you intend to run applications on.
    - Assist the compiler in generating optimal code for the targets, or provide your own optimized versions at source level.
    - Automatically select the most appropriate function version at runtime.
    - Reuse your optimized application binaries across various targets.

prerequisites:
    - Basic knowledge of GNU function attributes. 
    - Familiarity with indirect functions (ifuncs).
    - Basic knowledge of loop vectorization.
    - Familiarity with Arm assembly.
    - A LLVM 20 compiler with runtime library support or GCC 16.

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:53Z'
  generator: template
  source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  summary: >-
    Learn how to optimize C/C++ applications using function multiversioning on Arm64 targets with
    GCC or LLVM, enabling automatic runtime selection of hardware-optimized function versions.
    It is designed for developers interested in optimizing their C/C++ applications across Arm64
    targets. By the end, you will be able to use hardware features to tune your applications at
    function level, create multiple versions of C/C++ functions for the targets that you intend
    to run applications on, and assist the compiler in generating optimal code for the targets,
    or provide your own optimized versions at source level. It focuses on tools and technologies
    such as C, CPP, and Runbook, Linux, Android, and macOS environments, and Arm platforms including
    Cortex-A and Neoverse. The main steps cover About function multiversioning, Example 1 - code
    generation, Example 2 - runtime using ACLE intrinsics, Example 3 - inline assembly at runtime,
    and Compatibility with streaming mode.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will use hardware features to tune your applications at function level, create multiple
      versions of C/C++ functions for the targets that you intend to run applications on, and
      assist the compiler in generating optimal code for the targets, or provide your own optimized
      versions at source level. Learn how to optimize C/C++ applications using function multiversioning
      on Arm64 targets with GCC or LLVM, enabling automatic runtime selection of hardware-optimized
      function versions.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers interested in optimizing their C/C++ applications
      across Arm64 targets.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Basic knowledge of GNU function attributes.;
      Familiarity with indirect functions (ifuncs).; Basic knowledge of loop vectorization.; Familiarity
      with Arm assembly.; A LLVM 20 compiler with runtime library support or GCC 16.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including C, CPP, and Runbook, Linux, Android, and macOS environments,
      and Arm platforms such as Cortex-A and Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around About function multiversioning, Example 1 - code generation,
      Example 2 - runtime using ACLE intrinsics, Example 3 - inline assembly at runtime, and Compatibility
      with streaming mode.
# END generated_summary_faq

author: Alexandros Lamprineas

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - C
    - CPP
    - Runbook
operatingsystems:
    - Linux
    - Android
    - macOS

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming
    - laptops-and-desktops
    - embedded-and-microcontrollers

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Arm C Language Extensions
        link: https://arm-software.github.io/acle/main/acle.html
        type: documentation


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


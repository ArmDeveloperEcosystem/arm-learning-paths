---
title: Enable reproducible math functions across vector extensions with Arm Performance Libraries

minutes_to_complete: 10

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:59Z'
  generator: template
  source_hash: d643c9ef25aa5442aec65ac6a8f48264d4789f8e24ffd6270c2efacce48dd8fc
  summary: >-
    Enable reproducible math functions across vector extensions with Arm Performance Libraries
    walks you through an end-to-end Arm software workflow. It is designed for developers who want
    to produce reproducible code across vector extensions using math functions in Libamath, a
    component of Arm Performance Libraries. By the end, you will be able to explain what numerical
    reproducibility means in numerical software, describe generic applications of numerical reproducibility
    in the industry, and describe how reproducibility is defined and implemented in Libamath.
    It focuses on tools and technologies such as Arm Performance Libraries, GCC, LLVM, and Libamath,
    Linux environments, and Arm platforms including Neoverse. The main steps cover Understand
    numerical reproducibility in floating-point math, Explore where reproducibility is critical,
    Enable reproducibility in Libamath, and Verify reproducible results across scalar, Neon, and
    SVE.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will explain what numerical reproducibility means in numerical software, describe generic
      applications of numerical reproducibility in the industry, and describe how reproducibility
      is defined and implemented in Libamath.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers who want to produce reproducible code across
      vector extensions using math functions in Libamath, a component of Arm Performance Libraries.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm computer running Linux with [Arm
      Performance Libraries](/install-guides/armpl/) version 26.01 or newer installed; A C compiler
      such as [GCC](/install-guides/gcc/native/) or Clang installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Arm Performance Libraries, GCC, LLVM, and Libamath,
      Linux environments, and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand numerical reproducibility in floating-point
      math, Explore where reproducibility is critical, Enable reproducibility in Libamath, and
      Verify reproducible results across scalar, Neon, and SVE.
# END generated_summary_faq

author: Joana Cruz

who_is_this_for: This is an introductory topic for developers who want to produce reproducible code across vector extensions using math functions in Libamath, a component of Arm Performance Libraries. 

learning_objectives: 
    - Explain what numerical reproducibility means in numerical software
    - Describe generic applications of numerical reproducibility in the industry
    - Describe how reproducibility is defined and implemented in Libamath
    - Enable and use reproducible Libamath functions in real applications

prerequisites:
    - An Arm computer running Linux with [Arm Performance Libraries](/install-guides/armpl/) version 26.01 or newer installed
    - A C compiler such as [GCC](/install-guides/gcc/native/) or Clang installed

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performance Libraries
    - GCC
    - LLVM
    - Libamath
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: ArmPL Libamath Documentation
        link: https://developer.arm.com/documentation/101004/2601/Arm-Performance-Libraries-Math-Functions
        type: documentation
    - resource:
        title: ArmPL Installation Guide on Linux
        link: /install-guides/armpl/#linux
        type: website
    - resource:
        title: Use multi-accuracy math functions in Libamath
        link: /learning-paths/servers-and-cloud-computing/multi-accuracy-libamath/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


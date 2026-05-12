---
title: Migrating x86_64 workloads to aarch64

description: Learn the software migration methodology for porting Linux workloads from x86_64 to aarch64, including using Arm compilers, porting compiler intrinsics, and deploying applications in containers.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for embedded software developers looking at migrating Linux workloads to aarch64.

learning_objectives: 
    - Understand software migration methodology
    - Use different Arm compilers and libraries
    - Port applications containing compiler intrinsics

prerequisites:
    - Introductory understanding of software containers
    - Knowledge about building workflows
    - Access to an aarch64 or x86_64 machine running Linux

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: 81a15ff0d5579be9529a8c9c444be57521ebc48bbf5234f042f5a47a8a709b5c
  summary: >-
    Learn the software migration methodology for porting Linux workloads from x86_64 to aarch64,
    including using Arm compilers, porting compiler intrinsics, and deploying applications in
    containers. It is designed for embedded software developers looking at migrating Linux workloads
    to aarch64. By the end, you will be able to understand software migration methodology, use
    different Arm compilers and libraries, and port applications containing compiler intrinsics.
    It focuses on tools and technologies such as GCC, Arm Compiler for Linux, Docker, and Neon,
    Linux environments, and Arm platforms including Cortex-A and Neoverse. The main steps cover
    Porting methodology, Porting analysis, Development environment, Application porting, and Run
    and evaluate.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand software migration methodology, use different Arm compilers and libraries,
      and port applications containing compiler intrinsics. Learn the software migration methodology
      for porting Linux workloads from x86_64 to aarch64, including using Arm compilers, porting
      compiler intrinsics, and deploying applications in containers.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for embedded software developers looking at migrating Linux workloads
      to aarch64.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Introductory understanding of software
      containers; Knowledge about building workflows; Access to an aarch64 or x86_64 machine running
      Linux.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including GCC, Arm Compiler for Linux, Docker, and Neon, Linux
      environments, and Arm platforms such as Cortex-A and Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Porting methodology, Porting analysis, Development
      environment, Application porting, and Run and evaluate.
# END generated_summary_faq

author: Kasper Mecklenburg

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - GCC
    - Arm Compiler for Linux
    - Docker
    - Neon

further_reading:
    - resource:
        title: Porting architecture specific intrinsics
        link: /learning-paths/cross-platform/intrinsics/
        type: blog
    - resource:
        title: SIMD-everywhere repository
        link: https://github.com/simd-everywhere/simde
        type: website
    - resource:
        title: Migrating applications to Arm servers
        link: /learning-paths/servers-and-cloud-computing/migration
        type: blog
    - resource:
        title: Port Code to Arm Scalable Vector Extension (SVE)
        link: /learning-paths/servers-and-cloud-computing/sve/
        type: blog

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---


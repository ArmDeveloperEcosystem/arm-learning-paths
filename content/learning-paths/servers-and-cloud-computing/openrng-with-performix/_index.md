---
title: Accelerate random number generation with OpenRNG and Performix

description: Learn how to profile an example C++ data-processing workload on Arm Linux with Arm Performix, then accelerate random number generation using OpenRNG and Arm Performance Libraries.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for C++ developers who want to profile a data-processing workload on Arm Linux, identify performance bottlenecks with Arm Performix, and accelerate random number generation using OpenRNG and Arm Performance Libraries.

learning_objectives:
    - Build and run a baseline C++ data-processing workload on Arm Linux
    - Use Arm Performix Code Hotspots to identify the highest-impact optimization target
    - Accelerate random number generation by integrating OpenRNG and Arm Performance Libraries
    - Measure performance improvements using a microbenchmark across multiple data sizes

prerequisites:
    - An Arm Linux (aarch64) server, such as an AWS Graviton3 instance
    - Basic understanding of C++ and CMake

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 778ac2a8b8ad9ffd665f6f0be545541090465f355094c354cc693e784d27559a
  summary: >-
    Learn how to profile an example C++ data-processing workload on Arm Linux with Arm Performix,
    then accelerate random number generation using OpenRNG and Arm Performance Libraries. It is
    designed for C++ developers who want to profile a data-processing workload on Arm Linux, identify
    performance bottlenecks with Arm Performix, and accelerate random number generation using
    OpenRNG and Arm Performance Libraries. By the end, you will be able to build and run a baseline
    C++ data-processing workload on Arm Linux, use Arm Performix Code Hotspots to identify the
    highest-impact optimization target, and accelerate random number generation by integrating
    OpenRNG and Arm Performance Libraries. It focuses on tools and technologies such as CMake,
    Arm Performix, OpenRNG, and Arm Performance Libraries, Linux environments, and Arm platforms
    including Neoverse. The main steps cover Set up your environment, Run the baseline data-processing
    example, Identify code hotspots with Arm Performix, Accelerate distribution generation with
    OpenRNG, and Measure performance improvements with a microbenchmark.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build and run a baseline C++ data-processing workload on Arm Linux, use Arm Performix
      Code Hotspots to identify the highest-impact optimization target, and accelerate random
      number generation by integrating OpenRNG and Arm Performance Libraries. Learn how to profile
      an example C++ data-processing workload on Arm Linux with Arm Performix, then accelerate
      random number generation using OpenRNG and Arm Performance Libraries.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for C++ developers who want to profile a data-processing workload
      on Arm Linux, identify performance bottlenecks with Arm Performix, and accelerate random
      number generation using OpenRNG and Arm Performance Libraries.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm Linux (aarch64) server, such
      as an AWS Graviton3 instance; Basic understanding of C++ and CMake.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including CMake, Arm Performix, OpenRNG, and Arm Performance
      Libraries, Linux environments, and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up your environment, Run the baseline data-processing
      example, Identify code hotspots with Arm Performix, Accelerate distribution generation with
      OpenRNG, and Measure performance improvements with a microbenchmark.
# END generated_summary_faq

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - CMake
    - Arm Performix
    - OpenRNG
    - Arm Performance Libraries
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: OpenRNG project repository
        link: https://gitlab.arm.com/libraries/openrng
        type: documentation
    - resource:
        title: Find code hotspots with Arm Performix
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: documentation
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: /learning-paths/servers-and-cloud-computing/performix-microarchitecture/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


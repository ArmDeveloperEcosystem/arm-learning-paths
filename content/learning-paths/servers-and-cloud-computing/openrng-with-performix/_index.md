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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:44:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 778ac2a8b8ad9ffd665f6f0be545541090465f355094c354cc693e784d27559a
  summary_generated_at: '2026-06-02T04:42:23Z'
  summary_source_hash: 778ac2a8b8ad9ffd665f6f0be545541090465f355094c354cc693e784d27559a
  faq_generated_at: '2026-06-03T01:44:04Z'
  faq_source_hash: 778ac2a8b8ad9ffd665f6f0be545541090465f355094c354cc693e784d27559a
  summary: >-
    Learn to profile and accelerate a C++ data-processing workload on Arm Linux (aarch64) using
    Arm Performix and OpenRNG from Arm Performance Libraries. You will build and run a baseline
    application, use Performix Code Hotspots to identify the most impactful functions to optimize,
    then integrate OpenRNG’s vector API to speed up random number generation. Finally, you will
    run a microbenchmark sweep to measure runtime across input sizes from 2^8 to 2^15 elements
    and compare baseline versus accelerated builds. This introductory path targets C++ developers
    and assumes access to an Arm Linux server, such as an AWS Graviton3 instance, plus basic knowledge
    of C++ and CMake.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm Linux (aarch64) server, such as an AWS Graviton3 instance, and a basic understanding
      of C++ and CMake. No other explicit prerequisites are listed.
  - question: Which packages should I install, and what if I’m not using Amazon Linux?
    answer: >-
      Install git, cmake, g++, environment-modules, and python3 with your package manager. The
      steps use dnf on Amazon Linux 2023, but you can substitute apt on Ubuntu or Debian.
  - question: How do I decide which function to optimize after running the baseline?
    answer: >-
      Use Arm Performix Code Hotspots to profile the entire program with hardware performance
      counters and identify the routines with the highest impact. This avoids relying on manual
      timers that might miss hotspots like both generateDistribution and min_length.
  - question: When integrating OpenRNG, which API should I use and what changes am I making?
    answer: >-
      Use OpenRNG’s Vector Statistical Library (VSL) API to generate Gaussian values in bulk via
      a stream object. Replace the baseline’s one-sample-at-a-time generation with this vectorized,
      bulk generation.
  - question: What result should I expect from the microbenchmark sweep, and how do I compare
      builds?
    answer: >-
      The microbenchmark isolates generateDistribution and times it in microseconds across sizes
      from 2^8 to 2^15. Run both the baseline and accelerated builds and compare the recorded
      times to see how the speedup from OpenRNG scales with input size.
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


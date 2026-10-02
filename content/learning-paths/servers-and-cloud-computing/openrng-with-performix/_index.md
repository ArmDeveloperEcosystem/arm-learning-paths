---
title: Accelerate random number generation with OpenRNG and Performix

description: Learn how to profile an example C++ data-processing workload on Arm Linux with Arm Performix, then accelerate random number generation using OpenRNG and Arm Performance Libraries.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for C++ developers who want to profile a data-processing workload on Arm Linux, identify performance bottlenecks with Arm Performix, and accelerate random number generation using OpenRNG and Arm Performance Libraries.

learning_objectives:
    - Build and run a baseline C++ data-processing workload on Arm Linux.
    - Use Arm Performix Code Hotspots to identify the highest-impact optimization target.
    - Accelerate random number generation by integrating OpenRNG and Arm Performance Libraries.
    - Measure performance improvements using a microbenchmark across multiple data sizes. 

prerequisites:
    - An Arm Linux (aarch64) server, such as an AWS Graviton3-based instance
    - Basic understanding of C++ and CMake

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:44:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 004969d91992cbe6672e86cb8cc4734742e4461085198eaf09f3e2ff2afaf24d
  summary_generated_at: '2026-10-01T19:44:16Z'
  summary_source_hash: 004969d91992cbe6672e86cb8cc4734742e4461085198eaf09f3e2ff2afaf24d
  faq_generated_at: '2026-10-01T19:44:16Z'
  faq_source_hash: 004969d91992cbe6672e86cb8cc4734742e4461085198eaf09f3e2ff2afaf24d
  summary: >-
    You'll accelerate random-number generation in a C++ workload on Arm Linux with OpenRNG. First, you'll build
    and run the baseline application, then use Arm Performix Code Hotspots to identify expensive
    functions. You'll then replace scalar distribution generation with the OpenRNG vector API from Arm
    Performance Libraries and profile the updated build. Finally, you'll run a microbenchmark across
    eight input sizes and compare the baseline and accelerated timings.
  faqs:
  - question: Which package manager should I use during setup if I'm using Ubuntu or Debian?
    answer: >-
      Replace `dnf` with `apt` on Ubuntu or Debian. 
  - question: What result should I expect when I run the baseline example?
    answer: >-
      The program generates two random distributions, filters points within a window, and computes
      the shortest distance from the origin. Use this run to establish baseline behavior and timing
      before profiling and acceleration.
  - question: What should I look for in the Arm Performix Code Hotspots report?
    answer: >-
      Focus on functions consuming the largest share of CPU cycles. In this example, routines
      such as `generateDistribution` or `min_length` might appear near the top and inform which code to
      optimize first.
  - question: Which OpenRNG API should I use to speed up distribution generation?
    answer: >-
      Use the Vector Statistical Library (VSL) API with a stream object to generate values in
      bulk. This vector approach reduces per-call overhead for random number generation.
  - question: What output indicates the microbenchmark sweep ran correctly?
    answer: >-
      The sweep times the isolated distribution generator across eight sizes from 2^8 to 2^15
      and reports elapsed time in microseconds. Run both baseline and accelerated builds, then compare
      timings across sizes to evaluate scaling and improvements.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
        link: https://github.com/arm/openrng
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

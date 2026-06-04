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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:38:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  summary_generated_at: '2026-06-01T21:06:01Z'
  summary_source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  faq_generated_at: '2026-06-02T21:38:11Z'
  faq_source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  summary: >-
    This advanced Learning Path shows how to apply function multiversioning in C/C++ for Arm64
    targets using GCC or LLVM so your binaries can select the most appropriate implementation
    at runtime. You will annotate functions with target_version and target_clones, build example
    programs on Linux, Android, or macOS, and observe how the compiler generates versions specialized
    for features such as SVE, SVE2, and FEAT_MOPS, including cases using ACLE intrinsics and inline
    assembly. A dedicated step covers compatibility with Arm streaming mode. By the end, you will
    be able to create function-level variants that leverage hardware capabilities and reuse the
    same binary across different Arm64 systems. Prerequisites include basic GNU attributes, ifuncs,
    loop vectorization, Arm assembly, and LLVM 20 (with runtime support) or GCC 16.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need either an LLVM 20 compiler with runtime library support or GCC 16. The path assumes
      basic knowledge of GNU function attributes, familiarity with indirect functions (ifuncs)
      and loop vectorization, and some familiarity with Arm assembly.
  - question: Which attribute should I use to define multiple function versions?
    answer: >-
      Use __attribute__((target_version("name"))) to define a version keyed to specific features,
      or __attribute__((target_clones("name", ...))) to create multiple versions at once. The
      "name" string lists architectural features separated by '+'.
  - question: Does the order of features in target_clones affect runtime selection?
    answer: >-
      No. The examples note that the order in which versions are listed with target_clones does
      not matter.
  - question: How do I know which version ran at runtime?
    answer: >-
      One example prints a message such as "Running the sve version of dotProduct" when the SVE
      path executes. In general, the runtime mechanism selects the most appropriate version automatically,
      and the examples include output cues to validate this.
  - question: Is multiversioning compatible with Arm streaming mode?
    answer: >-
      Yes, as long as all versions of a function use the same calling convention. The examples
      demonstrate compatibility using attributes like __arm_streaming and a variant specialized
      for sme2.
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


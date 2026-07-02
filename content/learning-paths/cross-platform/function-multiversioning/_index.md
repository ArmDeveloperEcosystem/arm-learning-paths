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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:33:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  summary_generated_at: '2026-07-02T19:33:13Z'
  summary_source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  faq_generated_at: '2026-07-02T19:33:13Z'
  faq_source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  summary: >-
    You'll implement function multiversioning for arm64 in C/C++ using
    the `target_version` and `target_clones` attributes, so a single binary contains feature-specific
    implementations. You'll create versions keyed to architectural features such as `default`,
    `sve`, `sve2`, `simd`, `mops`, and `sme2` to enable runtime selection of the most suitable function.
    Through hands-on examples, you'll compare code generation for a vectorized loop, write an SVE-based
    dot product with Arm C Language Extensions (ACLE), and mix SVE2 inline assembly with library
    calls where the compiler can emit `FEAT_MOPS` for `memcpy`. You'll also cover streaming mode
    compatibility by keeping calling conventions consistent across function versions.
  faqs:
  - question: How do I know which function version executed at runtime?
    answer: >-
      In the dot product example, the SVE-specialized function prints a message when it runs.
      If that message does not appear, the default version executed.
  - question: Which option should I use in `target_version` or `target_clones`?
    answer: >-
      Use architectural feature names shown in the examples, such as `default`, `sve`, `sve2`, `simd`,
      `mops`, or `sme2`. You can also combine multiple features using a `+` separator in the attribute
      string.
  - question: Does the order of entries in `target_clones` affect selection?
    answer: >-
      No. The order of versions listed in `target_clones` does not affect which version is chosen
      at runtime.
  - question: How should I organize code that uses ACLE intrinsics or inline assembly?
    answer: >-
      Place SVE or SVE2-specific code in functions annotated with the corresponding `target_version`
      (for example, `sve` or `sve2`). Keep a generic `default` version so the binary runs on Armv8
      targets without those features.
  - question: What should I check if I use streaming mode with multiversioning?
    answer: >-
      Ensure every version of the function uses the same calling convention. The examples show
      combining `__arm_streaming` (and related attributes) with `target_version` or `target_clones`
      to keep versions compatible.
# END generated_summary_faq

author: Alexandros Lamprineas

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

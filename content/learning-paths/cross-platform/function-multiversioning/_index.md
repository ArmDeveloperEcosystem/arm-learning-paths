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
  generated_at: '2026-07-02T17:55:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  summary_generated_at: '2026-07-02T17:55:26Z'
  summary_source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  faq_generated_at: '2026-07-02T17:55:26Z'
  faq_source_hash: 1c1d745bd1af535315d5edd1b2b9214c96419d46abde3af8fa75bdde299bb65d
  summary: >-
    This Learning Path shows how to implement function multiversioning in C/C++ for Arm64 using
    GCC or LLVM attributes to emit multiple function implementations in one binary and select
    among them at runtime. You annotate functions with target_version and target_clones to specialize
    for features such as SVE, SVE2, and FEAT_MOPS, alongside a default baseline. Through focused
    examples, you compare compiler-generated code for loops, use Arm C Language Extensions (ACLE)
    intrinsics for a dot product, and add inline assembly for string handling. The path also demonstrates
    how to keep multiversioned functions compatible with Arm streaming mode by aligning calling
    conventions across all versions.
  faqs:
  - question: 'Which attribute should I use: target_version or target_clones?'
    answer: >-
      Use target_version to provide a specific implementation for a named feature set. Use target_clones
      to request multiple versions from a single function definition for the listed targets; order
      does not matter. Include a default version to provide a baseline implementation.
  - question: How do I know which function version ran at runtime?
    answer: >-
      In the dot product example, the SVE specialization prints a message when it runs. You can
      add similar messages to other versions or inspect generated code to see whether SVE/SVE2/MOPS
      instructions were used.
  - question: What should I check if the loop example does not vectorize?
    answer: >-
      Confirm the function uses target_clones with "sve" and "default" as shown. Use an optimization
      level where the compiler decides to vectorize loops, and inspect the generated code to verify
      SVE appears only in the specialized case.
  - question: How do I name architectural features in the attributes?
    answer: >-
      Use the feature names shown in the examples, such as sve, sve2, mops, simd, sme2, or default.
      You can combine multiple features by separating them with a plus sign (+).
  - question: What should I check when using streaming mode with multiversioning?
    answer: >-
      Ensure every function version uses the same calling convention. Follow the example patterns
      with __arm_streaming and __arm_locally_streaming so all versions remain compatible in streaming
      mode.
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


---
title: Enable reproducible math functions across vector extensions with Arm Performance Libraries

minutes_to_complete: 10

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:01:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d643c9ef25aa5442aec65ac6a8f48264d4789f8e24ffd6270c2efacce48dd8fc
  summary_generated_at: '2026-06-02T05:03:04Z'
  summary_source_hash: d643c9ef25aa5442aec65ac6a8f48264d4789f8e24ffd6270c2efacce48dd8fc
  faq_generated_at: '2026-06-03T02:01:52Z'
  faq_source_hash: d643c9ef25aa5442aec65ac6a8f48264d4789f8e24ffd6270c2efacce48dd8fc
  summary: >-
    This Learning Path shows you how to enable and use reproducible math functions in Libamath,
    a component of Arm Performance Libraries, on Linux-based Arm systems. You will learn what
    numerical reproducibility means and where it matters, then configure Libamath so supported
    functions produce bitwise-identical floating‑point results across scalar, Neon (AdvSIMD),
    and SVE implementations while operating in the default accuracy mode (within 3.5 ULP). The
    hands-on example verifies reproducibility using the single‑precision expf function across
    vector paths. Prerequisites include an Arm computer running Linux with Arm Performance Libraries
    26.01 or newer, and a C compiler such as GCC or Clang.
  faqs:
  - question: What do I need before running the example?
    answer: >-
      You need an Arm computer running Linux with Arm Performance Libraries version 26.01 or newer
      installed, and a C compiler such as GCC or Clang. No other prerequisites are explicitly
      listed.
  - question: Which vector extensions are covered by reproducibility in this path?
    answer: >-
      On Linux, Libamath supports bitwise-reproducible results across scalar, Neon (AdvSIMD),
      and SVE implementations for a subset of math functions.
  - question: Which math functions are reproducible in Libamath?
    answer: >-
      Reproducibility is provided for a subset of Libamath functions on Linux. This path demonstrates
      expf; the complete list of supported functions is not explicitly listed here.
  - question: How do I compile and link the example against Arm Performance Libraries?
    answer: >-
      Set CC to your compiler (for example, gcc), and export C_INCLUDE_PATH, LIBRARY_PATH, and
      LD_LIBRARY_PATH to point to $ARMPL_DIR/include and $ARMPL_DIR/lib. Then build your C code
      so it includes Libamath headers and links against the Arm Performance Libraries.
  - question: What result should I expect when verifying reproducibility?
    answer: >-
      For the same inputs, the floating-point results should be bitwise identical across scalar,
      Neon, and SVE code paths for supported Libamath functions. These routines operate in the
      default accuracy mode, within 3.5 ULP of the correctly rounded value.
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


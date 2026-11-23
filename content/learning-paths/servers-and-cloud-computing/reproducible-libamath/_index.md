---
title: Enable reproducible Arm Performance Libraries math functions
description: Enable reproducible Libamath functions in Arm Performance Libraries and verify bitwise-identical results across scalar, Neon, and SVE code paths.

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers who want to produce reproducible code across vector extensions using math functions in Libamath, a component of Arm Performance Libraries. 

learning_objectives: 
    - Identify what numerical reproducibility means in numerical software.
    - Describe generic applications of numerical reproducibility in the industry.
    - Identify how reproducibility is defined and implemented in Libamath across scalar, Neon, and Scalable Vector Extension (SVE) code paths.
    - Enable and use reproducible Libamath functions in real applications.

prerequisites:
    - An Arm computer running Linux with [Arm Performance Libraries](/install-guides/armpl/) version 26.01 or later installed
    - A C compiler such as [GCC](/install-guides/gcc/native/) or Clang installed

author: Joana Cruz

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:55:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a074724dad6507fb0141d71b991741694c3495e60c44ee20a06b430eef613adc
  summary_generated_at: '2026-11-23T20:55:50Z'
  summary_source_hash: a074724dad6507fb0141d71b991741694c3495e60c44ee20a06b430eef613adc
  faq_generated_at: '2026-11-23T20:55:50Z'
  faq_source_hash: a074724dad6507fb0141d71b991741694c3495e60c44ee20a06b430eef613adc
  summary: You'll enable reproducible Libamath routines in Arm Performance Libraries and compare
    floating-point results across scalar, Neon, and SVE code paths. First, you'll learn what bitwise
    reproducibility means and where it matters. Then, you'll build against the reproducible library
    for supported functions and run an `expf` example. You'll compare the resulting bit patterns
    and review the scope and accuracy limits of this mode.
  faqs:
  - question: How do I know that reproducibility is enabled for my run?
    answer: Compare the floating-point bit patterns from supported scalar, Neon, and Scalable Vector Extension (SVE) Libamath
      functions for identical inputs. Matching IEEE 754 encodings indicate reproducible results.
  - question: How can I tell whether a function supports reproducibility?
    answer: Check `amath_repro.h` for the full list of supported functions. The reproducible library
      contains a subset of the functions in the regular Libamath library.
  - question: What accuracy do reproducible routines provide?
    answer: For supported functions, you get results within 3.5 ULP of the correctly rounded value
      in the default accuracy mode.
  - question: What should I compare in the expf example?
    answer: Compare the IEEE 754 bit patterns produced by the scalar, Neon, and SVE paths for
      identical inputs. Matching patterns show reproducible behavior for this example.
  - question: Which build options enable reproducible Libamath routines?
    answer: Include `amath.h` in your C or C++ source, compile with `-DAMATH_REPRO=1`, and link
      with `-lamath_repro`. Calls to supported functions then use the reproducible implementations.
# END generated_summary_faq

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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


---
title: Control floating-point accuracy modes in Arm Performance Libraries

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for developers who want to use the different accuracy modes for vectorized math functions in Libamath, a component of Arm Performance Libraries.

description: Select and apply accuracy modes for vectorized math functions in Libamath to balance performance and precision for your application.

learning_objectives: 
    - Understand how accuracy is defined and measured in Libamath.
    - Select an appropriate accuracy mode for your application.
    - Use Libamath with different vector accuracy modes in practice.

prerequisites:
    - An Arm computer running Linux with [Arm Performance Libraries](/install-guides/armpl/) version 25.04 or newer installed


# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:54:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ead9a4e32a3aa9ccbbfb609b422eec15f46170b5f5f4454f3a0df97e84638893
  summary_generated_at: '2026-09-28T19:54:04Z'
  summary_source_hash: ead9a4e32a3aa9ccbbfb609b422eec15f46170b5f5f4454f3a0df97e84638893
  faq_generated_at: '2026-09-28T19:54:04Z'
  faq_source_hash: ead9a4e32a3aa9ccbbfb609b422eec15f46170b5f5f4454f3a0df97e84638893
  summary: >-
    You'll control floating-point accuracy for Libamath vector functions in Arm Performance Libraries.
    First, you'll review IEEE 754 representation and Units in the Last Place (ULP), then use ULP error to
    interpret results. You'll map Libamath function suffixes to selectable accuracy modes and their
    error bounds. Finally, you'll run the Neon single-precision exponential function in each mode,
    calculate its ULP error, and compare it with the example demonstrated in the Learning Path.
  faqs:
  - question: How do I recognize which Libamath accuracy mode a function uses?
    answer: >-
      Check the function symbol suffix. The `_u10` suffix selects high accuracy with a 1 ULP bound,
      no suffix selects default accuracy, and `_umax` selects maximum performance.
  - question: What ULP error bounds should I expect for each mode?
    answer: >-
      Compare your measured error with these limits: high accuracy is at most 1 ULP, default accuracy
      is at most 3.5 ULP, and low accuracy is approximately at most 4,096 ULP.
  - question: What result should I expect when running the example?
    answer: >-
      Confirm that the program calls the Neon single-precision exponential function in each mode
      and reports an error calculated by `ulp_error.h`. Each value should remain within its documented
      ULP bound.
  - question: What should I check if the example can’t find amath.h or float32x4_t?
    answer: >-
      Confirm that Arm Performance Libraries 25.04 or later is installed and that your build uses
      the correct include paths. Compile on an Arm system so that the example’s vector types and calling
      convention are available.
  - question: How is ULP computed, and why use it instead of absolute error?
    answer: >-
      Calculate `ULP(x)` as `nextafter(x, +inf) - x`, which gives the spacing to the next representable
      value. ULP error scales with magnitude, so you avoid the bias that absolute error can introduce
      across different ranges.
# END generated_summary_faq

author: Joana Cruz

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
    - Libamath
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Arm Performance Libraries math functions documentation
        link: https://developer.arm.com/documentation/101004/2410/General-information/Arm-Performance-Libraries-math-functions
        type: documentation
    - resource:
        title: Arm Performance Libraries installation guide
        link: /install-guides/armpl/
        type: website
    - resource:
        title: What Every Computer Scientist Should Know About Floating-Point Arithmetic
        link: https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
        type: documentation
    - resource:
        title: Arm Optimized Routines
        link: https://github.com/ARM-software/optimized-routines
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

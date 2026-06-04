---
title: Control floating-point accuracy modes in Arm Performance Libraries

minutes_to_complete: 20

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:34:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a10683fdd14359e93056dc4ba24581856833765c64915979d0466a06887e0755
  summary_generated_at: '2026-06-02T04:29:42Z'
  summary_source_hash: a10683fdd14359e93056dc4ba24581856833765c64915979d0466a06887e0755
  faq_generated_at: '2026-06-03T01:34:28Z'
  faq_source_hash: a10683fdd14359e93056dc4ba24581856833765c64915979d0466a06887e0755
  summary: >-
    Learn how to control floating-point accuracy for vectorized math functions in Libamath, a
    component of Arm Performance Libraries, on Linux. This path introduces IEEE-754 representation,
    Units in the Last Place (ULP), and the ULP error metric used to assess function accuracy.
    You will see how Libamath offers multiple accuracy modes, how to recognize them by function-name
    suffixes (for example, _u10 for results within 1 ULP), and how to select a mode that balances
    precision and speed for your workload. A concise C example invokes the Neon single-precision
    exp function across modes and computes ULP error using a provided helper header. Prerequisite:
    an Arm computer running Linux with Arm Performance Libraries 25.04 or newer installed.
  faqs:
  - question: What do I need before running the example code?
    answer: >-
      You need an Arm computer running Linux with Arm Performance Libraries version 25.04 or newer
      installed. The path uses C code and Libamath, and assumes a typical GCC-based environment.
  - question: How do I select a specific Libamath accuracy mode in my code?
    answer: >-
      Accuracy modes are encoded in the function symbol suffix. For example, a suffix of _u10
      indicates a high-accuracy variant (≤ 1 ULP); other modes are exposed via their documented
      suffixes when available.
  - question: How is ULP error computed when checking results?
    answer: >-
      ULP error is defined as |want − got| divided by ULP(want). Because it scales with floating-point
      spacing, it provides a more meaningful accuracy measure than absolute error across different
      magnitudes.
  - question: What files should I have to build the example?
    answer: >-
      Create example.c using the provided code and ensure ulp_error.h from the previous section
      is available. The example includes amath.h and calls Libamath Neon single-precision exp
      variants to compare accuracy.
  - question: What should I check if the build fails with missing headers or vector types?
    answer: >-
      Verify Arm Performance Libraries 25.04+ is installed and accessible, and that you included
      both amath.h and ulp_error.h. Build on an Arm Linux system; the example uses AArch64 vector
      calling conventions and Neon vector types.
# END generated_summary_faq

author: Joana Cruz

who_is_this_for: This is an introductory topic for developers who want to use the different accuracy modes for vectorized math functions in Libamath, a component of Arm Performance Libraries.

description: Select and apply accuracy modes for vectorized math functions in Libamath to balance performance and precision for your application.

learning_objectives: 
    - Describe how accuracy is defined and measured in Libamath
    - Select an appropriate accuracy mode for your application
    - Use Libamath with different vector accuracy modes in practice

prerequisites:
    - An Arm computer running Linux with [Arm Performance Libraries](/install-guides/armpl/) version 25.04 or newer installed. 

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


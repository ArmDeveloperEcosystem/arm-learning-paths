---
title: Control floating-point accuracy modes in Arm Performance Libraries

minutes_to_complete: 20

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: a10683fdd14359e93056dc4ba24581856833765c64915979d0466a06887e0755
  summary: >-
    Select and apply accuracy modes for vectorized math functions in Libamath to balance performance
    and precision for your application. It is designed for developers who want to use the different
    accuracy modes for vectorized math functions in Libamath, a component of Arm Performance Libraries.
    By the end, you will be able to describe how accuracy is defined and measured in Libamath,
    select an appropriate accuracy mode for your application, and use Libamath with different
    vector accuracy modes in practice. It focuses on tools and technologies such as Arm Performance
    Libraries, GCC, and Libamath, Linux environments, and Arm platforms including Neoverse. The
    main steps cover Floating-point representation, Units in the last place (ULP), ULP error and
    accuracy, Accuracy modes in Libamath, and Arm Performance Libraries example.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe how accuracy is defined and measured in Libamath, select an appropriate
      accuracy mode for your application, and use Libamath with different vector accuracy modes
      in practice. Select and apply accuracy modes for vectorized math functions in Libamath to
      balance performance and precision for your application.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers who want to use the different accuracy modes
      for vectorized math functions in Libamath, a component of Arm Performance Libraries.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm computer running Linux with [Arm
      Performance Libraries](/install-guides/armpl/) version 25.04 or newer installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Arm Performance Libraries, GCC, and Libamath, Linux
      environments, and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Floating-point representation, Units in the last place
      (ULP), ULP error and accuracy, Accuracy modes in Libamath, and Arm Performance Libraries
      example.
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


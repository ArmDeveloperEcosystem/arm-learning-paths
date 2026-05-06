---
title: Write Neon intrinsics using GitHub Copilot to improve Adler32 performance

description: Learn how to use GitHub Copilot to write Neon intrinsics that accelerate the Adler32 checksum algorithm on Arm platforms, achieving significant performance improvements over standard C implementations.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for C/C++ developers who are interested in using GitHub Copilot to improve performance using Neon intrinsics.

learning_objectives: 
    - Use GitHub Copilot to write Neon intrinsics that accelerate the Adler32 checksum algorithm.

prerequisites:
    - An Arm computer running Linux with the GNU compiler (gcc) installed.
    - Visual Studio Code with the GitHub Copilot extension installed. 

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:53Z'
  generator: template
  source_hash: 37b19106fba70423ba8c58f82097d9251f0ae208e882c852f9c4531afcebb46c
  summary: >-
    Learn how to use GitHub Copilot to write Neon intrinsics that accelerate the Adler32 checksum
    algorithm on Arm platforms, achieving significant performance improvements over standard C
    implementations. It is designed for C/C++ developers who are interested in using GitHub Copilot
    to improve performance using Neon intrinsics. By the end, you will be able to use GitHub Copilot
    to write Neon intrinsics that accelerate the Adler32 checksum algorithm. It focuses on tools
    and technologies such as GCC and Runbook, Linux environments, and Arm platforms including
    Neoverse and Cortex-A. The main steps cover About Neon and Adler32, Create a C Version of
    Adler32, Create a test program, Create a Makefile, and Build and run the test program.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will use GitHub Copilot to write Neon intrinsics that accelerate the Adler32 checksum
      algorithm. Learn how to use GitHub Copilot to write Neon intrinsics that accelerate the
      Adler32 checksum algorithm on Arm platforms, achieving significant performance improvements
      over standard C implementations.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for C/C++ developers who are interested in using GitHub Copilot
      to improve performance using Neon intrinsics.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm computer running Linux with the
      GNU compiler (gcc) installed.; Visual Studio Code with the GitHub Copilot extension installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including GCC and Runbook, Linux environments, and Arm platforms
      such as Neoverse and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around About Neon and Adler32, Create a C Version of Adler32,
      Create a test program, Create a Makefile, and Build and run the test program.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - GCC
    - Runbook

operatingsystems:
    - Linux
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming


further_reading:
    - resource:
        title: Arm C Language Extensions
        link: https://arm-software.github.io/acle/
        type: Documentation
    - resource:
        title: Adler-32 Checksum Algorithm
        link: https://en.wikipedia.org/wiki/Adler-32
        type: Article
    - resource:
        title: Neon Programming Quick Reference
        link: https://developer.arm.com/documentation/den0018/a
        type: Documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


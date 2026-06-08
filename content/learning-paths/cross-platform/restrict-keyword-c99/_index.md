---
title: Understand the `restrict` keyword in C99

minutes_to_complete: 30

description: Learn how to use the C99 restrict keyword to indicate non-overlapping memory regions and enable better compiler optimizations for vectorization on Arm platforms.

who_is_this_for: This is an introductory topic for C developers who are interested in software optimization

learning_objectives: 
    - Learn the importance of using the `restrict` keyword in C correctly

prerequisites:
    - An Arm computer running Linux OS and a recent version of compiler (Clang or GCC) installed

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:49:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9825df99004e981fadce5884b40b2152f4e43064cbba2cd2129fd90006090678
  summary_generated_at: '2026-06-01T21:16:11Z'
  summary_source_hash: 9825df99004e981fadce5884b40b2152f4e43064cbba2cd2129fd90006090678
  faq_generated_at: '2026-06-02T21:49:44Z'
  faq_source_hash: 9825df99004e981fadce5884b40b2152f4e43064cbba2cd2129fd90006090678
  summary: >-
    This Learning Path shows C developers on Arm Linux how to use the C99 restrict keyword to
    indicate non-overlapping memory regions so compilers can apply stronger optimizations, including
    vectorization on AArch64. You will examine a case where overlapping pointers limit optimization,
    learn the rule-of-thumb for when restrict is valid, and study an SVE2 example with generated
    code. The steps reference GCC 13 with -O3 -march=armv9-a and compare results with Clang. After
    completing the path, you will know when and how to apply restrict safely in your own functions.
    Prerequisites: an Arm computer running Linux with a recent GCC or Clang installed. Estimated
    time: 30 minutes.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      Use an Arm computer running Linux with a recent version of GCC or Clang installed. No additional
      prerequisites are explicitly listed.
  - question: Which compiler and options are used in the SVE2 example?
    answer: >-
      The example shows output from gcc-13 built with -O3 -march=armv9-a. In this case, GCC 13
      produced a better result than Clang for the demonstrated function.
  - question: How do I decide if I can add restrict to a function’s pointer parameters?
    answer: >-
      Add restrict when you are certain the pointer arguments refer to non-overlapping memory
      and those objects are not accessed by any other means inside the function. The path provides
      a rule of thumb and a counterexample to guide this decision.
  - question: How do I know that restrict enabled vectorization on Arm?
    answer: >-
      Inspect the compiler’s generated output and compare versions with and without restrict.
      In the SVE2 example, vectorization appears as SVE2 instructions operating on z registers
      (for example, ld1b and add on z registers).
  - question: What should I avoid when considering restrict?
    answer: >-
      Do not use restrict if the memory regions referenced by pointer arguments may overlap or
      if the objects can be accessed through other pointers within the function. The path includes
      a counterexample illustrating when restrict is not appropriate.
# END generated_summary_faq

author: Konstantinos Margaritis

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Aarch64
    - Armv8-a
    - Armv9-a
tools_software_languages:
    - GCC
    - Clang
    - SVE2
    - Runbook

operatingsystems:
    - Linux
shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming
   

further_reading:
    - resource:
        title: How to use the restrict qualifier in C
        link: https://www.oracle.com/solaris/technologies/solaris10-cc-restrict.html
        type: blog
       
    - resource:
        title: Explore the usage of restrict with Godbolt
        link: https://godbolt.org/z/PxWxjc1oh
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


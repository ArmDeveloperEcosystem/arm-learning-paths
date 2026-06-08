---
title: Use the Eigen Linear Algebra Library on Arm

description: Learn how to use the Eigen linear algebra library on Arm systems with ASIMD and SVE vectorization, including building TensorFlow with SVE support for optimized performance.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for C/C++ developers who want to create high performance applications using the Eigen linear algebra library.

learning_objectives: 
    - Describe how to use Eigen on Arm systems.
    - Build TensorFlow with SVE on Arm systems.

prerequisites:
    - An Arm-based computer running Linux and a recent version of a C++ compiler (Clang or GCC).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:36:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  summary_generated_at: '2026-06-01T21:04:54Z'
  summary_source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  faq_generated_at: '2026-06-02T21:36:20Z'
  faq_source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  summary: >-
    Learn to use the Eigen C++ linear algebra library on Arm systems that support ASIMD (Neon)
    and SVE, then build TensorFlow with SVE enabled. You will build and run compact Eigen examples
    that exercise vectorized operations, including element-wise expressions on a 100×100 matrix
    and repeated 512×512 matrix multiplications that use FMA. The path then guides you to install
    TensorFlow build requirements and follow the upstream build-from-source process with slight
    modifications to enable SVE, producing a build you can run. Target environment is an Arm-based
    Linux system. Tools include GCC or Clang. Prerequisites: an Arm-based computer running Linux
    with a recent C++ compiler. Outcome: use Eigen on Arm and produce an SVE-enabled TensorFlow
    build.
  faqs:
  - question: What do I need before running the examples or building TensorFlow?
    answer: >-
      You need an Arm-based computer running Linux and a recent version of a C++ compiler (Clang
      or GCC). No other prerequisites are explicitly listed.
  - question: Which compiler should I use, and are special flags required for ASIMD or SVE?
    answer: >-
      You can use either GCC or Clang. The path demonstrates Eigen on Arm SIMD engines, and specific
      compiler options for ASIMD or SVE are not explicitly listed.
  - question: What code do I create and what results indicate the Eigen examples worked?
    answer: >-
      You will write small Eigen programs, including a 100×100 matrix example that returns the
      sum of all elements and a 512×512 matrix multiplication example in a file named eigen-test3.cpp.
      Successful runs print a numeric result, such as a summed value or a line like "C.norm():
      <number>".
  - question: How do I approach building TensorFlow with SVE in this path?
    answer: >-
      You follow TensorFlow’s build-from-source instructions with slight modifications. First
      install the required build dependencies provided in the steps, then build and run the SVE-enabled
      TensorFlow.
  - question: What should I do if my Arm system does not support SVE?
    answer: >-
      The path covers Eigen on both ASIMD (Neon) and SVE, so you can still work through the Eigen
      examples using ASIMD. The steps do not list an alternative workflow for building TensorFlow
      without SVE.
# END generated_summary_faq

author: Konstantinos Margaritis

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - GCC
    - Clang
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
        title: Eigen official Tutorial on Matrix class
        link: https://libeigen.gitlab.io/docs/group__TutorialMatrixClass.html
        type: documentation
    - resource:
        title: Eigen Webinar from Linaro
        link: https://static.linaro.org/connect/webinars/presentations/Eigen_Webinar_3.pdf
        type: documentation
    - resource:
        title: TensorFlow Install from Source instructions
        link: https://www.tensorflow.org/install/source
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


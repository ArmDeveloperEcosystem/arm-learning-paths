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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T17:21:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  summary_generated_at: '2026-07-02T17:21:03Z'
  summary_source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  faq_generated_at: '2026-07-02T17:21:03Z'
  faq_source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  summary: >-
    This Learning Path shows how to apply Eigen’s vectorized operations on Arm systems with ASIMD
    (Neon) and Scalable Vector Extension (SVE), then build TensorFlow with SVE enabled. Learners
    create and run two C++ programs that construct random matrices, iterate computations, and
    report numeric results, illustrating how Eigen maps common linear algebra expressions onto
    Arm SIMD. The first example works with a 100 x 100 matrix and accumulates a scalar result,
    while the second performs repeated 512 x 512 matrix multiplications and prints the matrix
    norm. The path then guides the build of TensorFlow with SVE support so that Eigen’s SVE vectorization
    is available during execution.
  faqs:
  - question: What result should I expect when running the matrix multiplication example?
    answer: >-
      The program prints a line like: C.norm(): <number>. The exact value varies because the matrices
      are initialized randomly, but seeing that output without errors confirms the loop completed.
  - question: Can I change the matrix sizes or iteration count in the examples?
    answer: >-
      Yes. Update the matrix dimensions in the constructors and adjust the N definition to change
      the iteration count. Larger sizes and higher N increase runtime and memory usage.
  - question: Do I need SVE hardware to complete the Eigen examples?
    answer: >-
      No. Eigen supports Neon/ASIMD in addition to SVE. On Arm systems without SVE, Eigen’s ASIMD
      paths are used.
  - question: Which Eigen headers and data types are used in these examples?
    answer: >-
      The examples include the Eigen/Dense module. One example operates on a 100 x 100 float matrix,
      and the matrix-multiplication example uses MatrixXd, which is double-precision.
  - question: What should I check if the TensorFlow with SVE build fails?
    answer: >-
      Verify that all required build dependencies from the TensorFlow instructions are installed
      and that you applied the SVE-specific steps from this path. Use a recent GCC or Clang on
      an Arm Linux system and re-run the build.
# END generated_summary_faq

author: Konstantinos Margaritis

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


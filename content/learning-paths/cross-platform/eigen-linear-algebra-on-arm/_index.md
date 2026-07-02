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
  generated_at: '2026-07-02T19:26:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  summary_generated_at: '2026-07-02T19:26:16Z'
  summary_source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  faq_generated_at: '2026-07-02T19:26:16Z'
  faq_source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  summary: >-
    You'll apply Eigen’s vectorized math on Arm by writing and running
    small C++ programs that exercise Neon/ASIMD and Scalable Vector Extension (SVE) code paths.
    You'll implement two concrete examples: summing elements in a 100×100 matrix over multiple
    iterations, and performing repeated 512×512 matrix multiplications that use fused multiply-add
    operations. After validating the Eigen examples on an Arm Linux system, you'll build TensorFlow
    with SVE enabled by following the documented build flow and required
    dependencies. You'll compile and run Eigen-based workloads and complete an SVE-capable
    TensorFlow build on Arm.
  faqs:
  - question: What result should I expect when I run the Eigen examples?
    answer: >-
      Example 1 prints a single numeric value representing the sum of all elements. Example 2
      prints one number from `C.norm()`. The exact values can vary because the matrices are randomized.
  - question: Can I change `N` or the matrix dimensions to adjust runtime?
    answer: >-
      Yes. Edit the `N` constant or the matrix sizes in the sample code, then rebuild. Larger matrices
      or a higher `N` increase runtime.
  - question: Why does the matrix multiplication example mention fused multiply-add (FMA)?
    answer: >-
      The example is structured so Eigen can use FMA on CPUs that support it. You do not need
      to verify FMA usage to continue; a correct run still prints a single numeric norm.
  - question: Which compiler should I use to build the examples?
    answer: >-
      Use a recent version of GCC or Clang on Linux as listed in the prerequisites. A successful
      build runs and prints the expected single-number outputs without errors.
  - question: How do I approach the TensorFlow with SVE step, and how do I know it worked?
    answer: >-
      Follow the TensorFlow build-from-source flow in this path, including the SVE-related steps
      and required dependencies. A successful outcome completes the build and allows TensorFlow
      to run on your Arm system.
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

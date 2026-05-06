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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:53Z'
  generator: template
  source_hash: 39c5e146afbfc74c3076d2cf3f1a67ddc0e4715f39b2cff1ccf76b288415bdc0
  summary: >-
    Learn how to use the Eigen linear algebra library on Arm systems with ASIMD and SVE vectorization,
    including building TensorFlow with SVE support for optimized performance. It is designed for
    C/C++ developers who want to create high performance applications using the Eigen linear algebra
    library. By the end, you will be able to describe how to use Eigen on Arm systems and build
    TensorFlow with SVE on Arm systems. It focuses on tools and technologies such as GCC, Clang,
    and Runbook, Linux environments, and Arm platforms including Cortex-A and Neoverse. The main
    steps cover About Eigen, Eigen examples, Eigen on Arm, and Build and Run TensorFlow with SVE.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe how to use Eigen on Arm systems and build TensorFlow with SVE on Arm systems.
      Learn how to use the Eigen linear algebra library on Arm systems with ASIMD and SVE vectorization,
      including building TensorFlow with SVE support for optimized performance.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for C/C++ developers who want to create high performance applications
      using the Eigen linear algebra library.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm-based computer running Linux
      and a recent version of a C++ compiler (Clang or GCC).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including GCC, Clang, and Runbook, Linux environments, and
      Arm platforms such as Cortex-A and Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around About Eigen, Eigen examples, Eigen on Arm, and Build
      and Run TensorFlow with SVE.
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


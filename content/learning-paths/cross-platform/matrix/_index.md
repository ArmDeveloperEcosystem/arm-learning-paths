---
title: Develop a native C++ library on an Arm-based machine
description: Learn how to develop and test a modern C++ library using CMake, GoogleTest, and matrix processing as a practical example on Arm platforms.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for developers who want to learn how to develop a library in modern C++ on Arm, using matrix processing as an example.

learning_objectives:
    - Develop a new C++ library.
    - Test a C++ library, ensuring it does not regress functionally.

prerequisites:
    - An Arm-based computer running Linux, macOS, or Windows.
    - An intermediate understanding of C++ programming.
    - A suitable Integrated Development Environment (IDE).
    - The [CMake](/install-guides/cmake/) build tool.
    - A C++ compiler with C++17 support.
    - A build system [GNU Make](https://www.gnu.org/software/make/) or [Ninja](https://ninja-build.org/).
    - A documentation generator [Doxygen](https://www.doxygen.nl/).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:45:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5611b6d1eebbea167d1860e3ac7f4f7910584561cbb18c3ed696aa27215edce9
  summary_generated_at: '2026-06-01T21:10:50Z'
  summary_source_hash: 5611b6d1eebbea167d1860e3ac7f4f7910584561cbb18c3ed696aa27215edce9
  faq_generated_at: '2026-06-02T21:45:23Z'
  faq_source_hash: 5611b6d1eebbea167d1860e3ac7f4f7910584561cbb18c3ed696aa27215edce9
  summary: >-
    This Learning Path guides you through developing and testing a modern C++ matrix-processing
    library on an Arm-based machine using CMake and GoogleTest. You will prepare a C++17 toolchain
    (GCC or Clang), select a build system (GNU Make or Ninja), and set up an IDE and a documentation
    generator such as Doxygen. Starting from project boilerplate, you implement core matrix types
    and operations (add, subtract, multiply), separate traversal from data processing, and write
    unit tests to guard against regressions. The path also discusses practical error-handling
    trade-offs. By the end, you have a buildable CMake project with a GoogleTest suite running
    on Linux, macOS, or Windows on Arm. Prerequisites are listed, and the estimated time to complete
    is about 120 minutes.
  faqs:
  - question: What do I need on my Arm-based machine before starting?
    answer: >-
      You need an Arm-based computer running Linux, macOS, or Windows; an IDE; CMake; a C++17-capable
      compiler (GCC or Clang); a build system (GNU Make or Ninja); and Doxygen. The path provides
      an example installation on Ubuntu using build-essential, clang, ninja-build, cmake, and
      doxygen.
  - question: Which compiler, C++ standard, and build system should I use?
    answer: >-
      Use GCC or Clang with C++17 support. Either GNU Make or Ninja is suitable as the build system,
      driven by CMake.
  - question: How do I know my environment is set up correctly?
    answer: >-
      After configuring the project with CMake and adding GoogleTest, build and run the unit tests
      for the Matrix library. Successful compilation and passing tests indicate the setup is working.
  - question: What functionality will I implement in the Matrix library?
    answer: >-
      You first add the core boilerplate for Matrix objects (construction, assignment, and dump-to-screen),
      then implement add, subtract, and multiply. The design separates matrix traversal from the
      data processing to make testing and extension straightforward.
  - question: How does this path address error handling in the library?
    answer: >-
      It explains how to balance safety and security with performance depending on the use case.
      The path discusses considerations rather than prescribing a single policy.
# END generated_summary_faq

author: Arnaud de Grandmaison


### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - CPP
    - GCC
    - Clang
    - CMake
    - Google Test
    - Runbook

operatingsystems:
    - Linux
    - macOS
    - Windows
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: CMake Tutorial
        link: https://cmake.org/cmake/help/latest/guide/tutorial/index.html
        type: documentation
    - resource:
        title: Quickstart Building with CMake
        link: https://google.github.io/googletest/quickstart-cmake.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


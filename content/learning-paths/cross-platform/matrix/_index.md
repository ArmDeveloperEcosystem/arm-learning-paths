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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:40:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5611b6d1eebbea167d1860e3ac7f4f7910584561cbb18c3ed696aa27215edce9
  summary_generated_at: '2026-07-29T16:40:06Z'
  summary_source_hash: 5611b6d1eebbea167d1860e3ac7f4f7910584561cbb18c3ed696aa27215edce9
  faq_generated_at: '2026-07-29T16:40:06Z'
  faq_source_hash: 5611b6d1eebbea167d1860e3ac7f4f7910584561cbb18c3ed696aa27215edce9
  summary: >-
    You'll build and test a modern C++ matrix library on an Arm-based machine with CMake and GoogleTest.
    First, you'll configure a C++17 toolchain and add unit tests. Then, you'll implement matrix construction, assignment,
    addition, subtraction, and multiplication, keeping traversal separate from data processing.
    You'll choose a build system and balance error checking with performance before validating the library
    with consistent builds and passing tests.
  faqs:
  - question: Which C++ compiler should I use and which standard is required?
    answer: >-
      Use a compiler with C++17 support. Both Clang and GCC work for this Learning Path.
  - question: Should I use GNU Make or Ninja for the build?
    answer: >-
      Either GNU Make or Ninja works with CMake. Choose one and use it consistently across builds.
  - question: What result should I expect after the first build and test run?
    answer: >-
      Expect the project to build successfully, and the unit tests to run without failures. At this stage, you
      can construct, assign, and print `Matrix` objects.
  - question: Which matrix operations do I implement and how should I structure them?
    answer: >-
      Implement addition, subtraction, and multiplication. Keep traversal separate from data
      processing so you can compose functionality and test components independently.
  - question: How should I approach error handling while implementing the library?
    answer: >-
      Balance safety and performance for your use case. Trusted, curated data can use different checks
      from untrusted input, so choose the validation level accordingly.
# END generated_summary_faq

author: Arnaud de Grandmaison

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

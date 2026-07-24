---
title: Write a Dynamic Memory Allocator

description: Learn how to implement a dynamic memory allocator in C, understanding heap management and how malloc and free work under the hood with practical examples.

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for software developers learning about dynamic memory allocation for the first time, and who may have used malloc and free in C programming. It also provides a starting point to explore more advanced memory allocation topics.

learning_objectives:
- Explain how dynamic memory allocation and the C heap works
- Write a simple dynamic memory allocator
- Explain some of the risks of heap allocation in general

prerequisites:
- Familiarity with C programming, with a good understanding of pointers.
- A Linux machine to run the example code.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:24:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  summary_generated_at: '2026-07-02T19:24:07Z'
  summary_source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  faq_generated_at: '2026-07-02T19:24:07Z'
  faq_source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  summary: >-
    You'll design and implement a minimal dynamic memory
    allocator in C on Linux, showing how heap-style allocation works behind familiar interfaces.
    First, you'll define the behavior of `simple_malloc` and `simple_free`, implement them in a small project
    with `heap.c` and `heap.h`, and exercise them from a provided test program. Then, you'll contrast
    dynamic and static allocation, describe failure behavior, and explore practical trade-offs
    of a simple allocator. You'll build and run the code, observe allocations
    and frees in action, and reason about basic risks and limitations of heap usage when integrating
    allocation into real programs.
  faqs:
  - question: Which files do I edit to implement the allocator?
    answer: >-
      Put the implementation in `heap.c` and the declarations in `heap.h`. The test program that calls
      your functions is in `main.c`, and `CMakeLists.txt` configures the build.
  - question: How do I confirm the test program calls my `simple_malloc` and `simple_free`?
    answer: >-
      Check that `main.c` includes `heap.h` and uses `simple_malloc` and `simple_free`. You can also add
      temporary logging or assertions in `heap.c` to verify the call flow during a test run.
  - question: What should I check if `simple_malloc` returns `NULL` for a small request?
    answer: >-
      Verify the requested size and confirm your allocator is initialized before the first request.
      Ensure your implementation handles allocation failure paths correctly and that the test
      code checks for `NULL` before using the returned pointer.
  - question: Do I need to replace the C library `malloc` and `free`?
    answer: >-
      No. You'll use separate functions named `simple_malloc` and `simple_free` and won't replace
      the C library allocator.
  - question: How can I sanity-check that `simple_free` works before moving on?
    answer: >-
      Run sequences that allocate, free, and then allocate again to see if subsequent requests
      succeed without errors. Add basic checks or prints in `main.c` and `heap.c` to confirm that
      block metadata and returned pointers behave as expected.
# END generated_summary_faq

author: David Spickett

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_images:
- ubuntu:latest
test_link: null
test_maintenance: true

further_reading:
    - resource:
        title: C Dynamic Memory Management Functions
        link: https://en.cppreference.com/w/c/memory
        type: documentation
    - resource:
        title: LLSoftSecBook chapter on Memory Vulnerabilities
        link: https://llsoftsec.github.io/llsoftsecbook/#memory-vulnerability-based-attacks
        type: website

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Cortex-A
  - Neoverse
operatingsystems:
  - Linux
tools_software_languages:
  - C 
  - Runbook

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops
    - embedded-and-microcontrollers

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

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
  generated_at: '2026-07-02T17:20:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  summary_generated_at: '2026-07-02T17:20:24Z'
  summary_source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  faq_generated_at: '2026-07-02T17:20:24Z'
  faq_source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  summary: >-
    This Learning Path walks through designing and implementing a minimal dynamic memory allocator
    in C on Linux. You compare static and dynamic allocation, then define a small API surface
    with simple_malloc and simple_free and outline their expected behavior. A provided project
    layout (CMakeLists.txt, heap.c, heap.h, and a test program) lets learners focus on the allocator
    logic rather than build scaffolding. You implement the allocator, build the example, and run
    allocations and frees to observe success cases and NULL returns. The path closes by highlighting
    trade-offs and limitations in simple allocators, preparing learners to reason about heap management
    and the choices behind standard malloc and free implementations.
  faqs:
  - question: Which functions do I need to implement for the allocator?
    answer: >-
      Implement simple_malloc and simple_free. Their declarations are in heap.h, and their behavior
      is described in the design step.
  - question: What files should I edit to change the allocator’s behavior?
    answer: >-
      Edit heap.c to change the allocator implementation and heap.h if you need to adjust the
      interface. The test program in main.c exercises your changes, and CMakeLists.txt configures
      the build.
  - question: What result should I expect when I run the example program?
    answer: >-
      The program should allocate memory with simple_malloc, use it, and call simple_free without
      errors. If a request cannot be satisfied, simple_malloc returns NULL as specified.
  - question: Do I need to replace standard malloc and free in my system?
    answer: >-
      No. This path introduces separate functions named simple_malloc and simple_free to avoid
      interfering with the system allocator. Use the provided test program to call your versions.
  - question: Do I need to implement calloc or realloc for this path?
    answer: >-
      No. The scope is limited to simple_malloc and simple_free. Additional functions are not
      listed and are outside this Learning Path.
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


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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:35:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  summary_generated_at: '2026-06-01T21:04:25Z'
  summary_source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  faq_generated_at: '2026-06-02T21:35:52Z'
  faq_source_hash: c59308676849aea9b7cfce8c48c7d6e1ca072ef6fb38fb193a34aa5b2597b9b9
  summary: >-
    This introductory Learning Path guides you through implementing a simple dynamic memory allocator
    in C on Linux. You will design and code two functions, simple_malloc and simple_free, to understand
    how heap allocation works and what malloc/free do under the hood, then build and run provided
    examples to observe allocation behavior. The project uses a small CMake-based structure (heap.c,
    heap.h, main.c, CMakeLists.txt) to configure and build the test program. Prerequisites are
    familiarity with C pointers and access to a Linux machine. The material also highlights some
    risks of heap allocation and is relevant to developers targeting Arm Cortex-A and Neoverse
    software. Estimated time to complete is about 120 minutes.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need a Linux machine and familiarity with C programming, including pointers. No additional
      prerequisites are explicitly listed.
  - question: Which allocator functions am I expected to implement?
    answer: >-
      You will implement simple_malloc and simple_free. simple_malloc takes a size in bytes and
      returns a pointer or NULL on failure, and simple_free releases previously allocated memory.
  - question: How is the project organized in the implementation step?
    answer: >-
      The project includes CMakeLists.txt, heap.c (allocator implementation), heap.h (function
      declarations), and main.c (a test program). Everything required to build and run example
      allocations is provided.
  - question: How do I build and run the code on Linux?
    answer: >-
      Use the provided CMakeLists.txt to configure and build the project as shown in the Learning
      Path steps. Building produces a program that exercises simple_malloc and simple_free.
  - question: How do I know my allocator works as intended?
    answer: >-
      Run the included test program and observe that allocations succeed and that simple_malloc
      returns NULL when memory cannot be allocated. The examples demonstrate basic allocation
      and freeing behavior.
# END generated_summary_faq

author: David Spickett

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


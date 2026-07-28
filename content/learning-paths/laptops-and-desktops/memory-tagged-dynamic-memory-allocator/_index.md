---
title: Adding Memory Tagging to a Dynamic Memory Allocator

description: Learn how to apply Arm Memory Tagging Extension (MTE) to protect dynamic memory allocations and prevent common memory use errors.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for software developers who want to learn how to use the Memory Tagging Extension (MTE) to protect dynamic memory allocations.

learning_objectives:
- Learn how to apply MTE to an existing memory allocator
- Understand how MTE can prevent common memory use errors

prerequisites:
- A Linux computer.
- Basic knowledge of how MTE works. Refer to the [Learn about Memory Tagging Extension Learning Path](/learning-paths/mobile-graphics-and-gaming/mte/)
- Knowledge of how a dynamic memory allocator can be implemented. Refer to [Write a Dynamic Memory Allocator Learning Path](/learning-paths/cross-platform/dynamic-memory-allocator/).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:22:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 87d4afe4ce7f0cef113cd61fd712fde073cca0eaafbe86a2066b76a117328d11
  summary_generated_at: '2026-07-28T16:22:41Z'
  summary_source_hash: 87d4afe4ce7f0cef113cd61fd712fde073cca0eaafbe86a2066b76a117328d11
  faq_generated_at: '2026-07-28T16:22:41Z'
  faq_source_hash: 87d4afe4ce7f0cef113cd61fd712fde073cca0eaafbe86a2066b76a117328d11
  summary: >-
    This Learning Path shows how to integrate Arm Memory Tagging Extension (MTE) into a simple
    dynamic memory allocator on Linux and observe how tag checks catch misuse at runtime. Learners
    review a small C project, enable tagged addresses and synchronous checking in process initialization,
    and use helper utilities to apply and compare tags during allocation and access. The path
    focuses on allocator-specific changes rather than allocator design, then runs targeted examples
    that intentionally trigger tag mismatches to demonstrate fault behavior. By the end, learners
    can trace where tags are set and checked in heap.c and supporting code, and recognize the
    resulting exceptions when common memory misuse occurs.
  faqs:
  - question: Which files should I modify to explore allocator and tagging behavior?
    answer: >-
      Edit heap.c and heap.h for allocator changes and mte_utils.c and mte_utils.h for tag helper
      logic. Use main.c to exercise the allocator and drive specific scenarios.
  - question: How do I run the example misuse cases that demonstrate tag faults?
    answer: >-
      Add calls in main.c to the example functions described in the demo and rebuild the project.
      Each function triggers a scenario so you can observe how the MTE-enabled allocator responds.
  - question: What should I check if no tag faults occur when I expect them?
    answer: >-
      Verify that process and heap initialization that enables tagged addresses runs before any
      allocations. Also confirm that the example functions are actually called from main.c.
  - question: What result should I expect when there is a tag mismatch?
    answer: >-
      On access, MTE compares the pointer’s logical tag with the memory’s allocation tag and raises
      an exception if they differ. The demo scenarios are designed to make this behavior visible.
  - question: Which tag checking mode does the demo configure?
    answer: >-
      The initialization sets synchronous tag checking. This configuration is applied when enabling
      tagged addresses for the process.
# END generated_summary_faq

author: David Spickett

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
- Cortex-A
tools_software_languages:
- MTE
- Linux
- C
operatingsystems:
- Linux

further_reading:
    - resource:
        title: LLSoftSecBook Chapter on Stack Buffer Overflows
        link: https://llsoftsec.github.io/llsoftsecbook/#stack-buffer-overflows
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


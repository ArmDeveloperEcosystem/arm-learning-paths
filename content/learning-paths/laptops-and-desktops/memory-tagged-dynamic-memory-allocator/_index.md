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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:09:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 87d4afe4ce7f0cef113cd61fd712fde073cca0eaafbe86a2066b76a117328d11
  summary_generated_at: '2026-06-01T22:08:16Z'
  summary_source_hash: 87d4afe4ce7f0cef113cd61fd712fde073cca0eaafbe86a2066b76a117328d11
  faq_generated_at: '2026-06-02T23:09:52Z'
  faq_source_hash: 87d4afe4ce7f0cef113cd61fd712fde073cca0eaafbe86a2066b76a117328d11
  summary: >-
    This advanced Learning Path shows how to add Arm Memory Tagging Extension (MTE) to a C dynamic
    memory allocator on Linux. Using the provided project (CMakeLists.txt, heap.c/.h, mte_utils.c/.h,
    and main.c), you will enable tagged addressing for the process, request memory with tag storage,
    and implement tagging in allocator operations. The steps focus on MTE-specific changes and
    include runnable examples that illustrate how tag checks catch common allocation and use errors.
    It targets developers who already understand MTE and dynamic memory allocators. Estimated
    time to complete is 120 minutes. The outcome is a working demo allocator that applies MTE
    for learning and experimentation.
  faqs:
  - question: What do I need before running the code in this Learning Path?
    answer: >-
      You need a Linux computer, basic knowledge of how MTE works, and familiarity with how a
      dynamic memory allocator can be implemented. The referenced Learning Paths on MTE and writing
      a dynamic memory allocator provide the necessary background.
  - question: Which source files contain the allocator and MTE-specific logic?
    answer: >-
      The project includes CMakeLists.txt, heap.c and heap.h for the allocator, mte_utils.c and
      mte_utils.h for tag handling helpers, and main.c for the demo application. Review these
      files to see how tagging is integrated into allocation and use sites.
  - question: How is MTE enabled and memory with tag storage requested in the allocator?
    answer: >-
      Memory with tag storage is not allocated by the kernel by default, so the application must
      request it. The heap does this in simple_heap_init using prctl(PR_SET_TAGGED_ADDR_CTRL,
      PR_TAGGED_ADDR_ENABLE | PR_MTE_TCF_SYNC | (0xfffe << PR_MTE_TAG_SHIFT), ...). The provided
      code shows the exact initialization used.
  - question: How do I exercise the examples and what result should I expect?
    answer: >-
      The demo starts in main.c, where each example exploit is a function you can call from main.
      When a tagged pointer accesses memory with a mismatched allocation tag, MTE raises an exception,
      demonstrating how common mistakes are caught.
  - question: Is the allocator implementation intended for production use?
    answer: >-
      No. It is a demo that illustrates concepts and does not make optimal use of MTE from a security
      or performance perspective. Any production code should be rigorously tested.
# END generated_summary_faq

author: David Spickett

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


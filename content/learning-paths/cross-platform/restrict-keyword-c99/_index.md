---
title: Understand the `restrict` keyword in C99

minutes_to_complete: 30

description: Learn how to use the C99 restrict keyword to indicate non-overlapping memory regions and enable better compiler optimizations for vectorization on Arm platforms.

who_is_this_for: This is an introductory topic for C developers who are interested in software optimization

learning_objectives: 
    - Learn the importance of using the `restrict` keyword in C correctly

prerequisites:
    - An Arm computer running Linux OS and a recent version of compiler (Clang or GCC) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:46:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9825df99004e981fadce5884b40b2152f4e43064cbba2cd2129fd90006090678
  summary_generated_at: '2026-07-29T16:46:57Z'
  summary_source_hash: 9825df99004e981fadce5884b40b2152f4e43064cbba2cd2129fd90006090678
  faq_generated_at: '2026-07-29T16:46:57Z'
  faq_source_hash: 9825df99004e981fadce5884b40b2152f4e43064cbba2cd2129fd90006090678
  summary: >-
    You'll use the C99 `restrict` qualifier to describe non-overlapping pointer regions and enable compiler
    vectorization on Arm. First, you'll examine how aliasing inhibits optimization. Then, you'll add `restrict`
    where its contract is safe and inspect the generated assembly. The examples highlight SVE2 code
    for a byte-processing loop on Armv9-A. You'll use the examples to recognize when `restrict` is valid or unsafe.
  faqs:
  - question: How do I know if I can mark these pointers as `restrict`?
    answer: >-
      Use `restrict` when the memory regions referenced by the pointer parameters don't overlap
      and the function has no other access path to those regions. If any argument can alias another,
      don't use `restrict`.
  - question: What result should I expect after I add `restrict` to a loop?
    answer: >-
      The compiler can assume no aliasing and might generate vectorized code. On Arm with SVE2, look
      for vector registers (`z0`–`z31`) and predicated operations in the assembly.
  - question: How do I spot an overlap that would invalidate my use of `restrict`?
    answer: >-
      If one pointer argument derives from another, such as a pointer into the same array, the
      regions overlap. Passing those pointers to a `restrict`-qualified function violates its contract.
  - question: Where do I check that the compiler used SVE2 for my example?
    answer: >-
      Inspect the generated assembly for SVE2 instructions and vector registers. `whilelo` predicates
      and `ld1b` or `st1b` instructions with `z` registers indicate SVE2 code generation.
  - question: When should I avoid using `restrict` even if pointers look independent?
    answer: >-
      Avoid `restrict` if the function can reach the same memory through another alias, such as a
      global pointer or indirect access. The non-aliasing guarantee must hold throughout the function.
# END generated_summary_faq

author: Konstantinos Margaritis

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Aarch64
    - Armv8-a
    - Armv9-a
tools_software_languages:
    - GCC
    - Clang
    - SVE2
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
        title: How to use the restrict qualifier in C
        link: https://www.oracle.com/solaris/technologies/solaris10-cc-restrict.html
        type: blog

    - resource:
        title: Explore the usage of restrict with Godbolt
        link: https://godbolt.org/z/PxWxjc1oh
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

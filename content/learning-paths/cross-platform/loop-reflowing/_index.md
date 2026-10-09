---
title: Optimize C and C++ code using compiler autovectorization techniques
description: Learn how to optimize C/C++ code using compiler autovectorization techniques including loop modifications, restrict qualifiers, and conditional handling for Arm processors.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for C/C++ developers who are interested in taking advantage of autovectorization in compilers.

learning_objectives: 
    - Modify loops to take advantage of autovectorization in compilers

prerequisites:
    - An Arm computer running Linux and a recent version of Clang or the GNU compiler (gcc) installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:39:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4218b8b0c1dee3862bb9765a83dfed0cb38555d1da7425e791c5c16b17f98c21
  summary_generated_at: '2026-07-29T16:39:29Z'
  summary_source_hash: 4218b8b0c1dee3862bb9765a83dfed0cb38555d1da7425e791c5c16b17f98c21
  faq_generated_at: '2026-07-29T16:39:29Z'
  faq_source_hash: 4218b8b0c1dee3862bb9765a83dfed0cb38555d1da7425e791c5c16b17f98c21
  summary: >-
    You'll enable and inspect compiler autovectorization for C and C++ loops on Arm Linux with GCC or Clang.
    You'll build focused examples, apply the C99 `restrict` qualifier, and inspect assembly to verify
    vectorization. Then, you'll examine countable loops and branches, refactor conditionals when needed,
    and use an integer dot product to recognize Arm SIMD instructions in generated code.
  faqs:
  - question: How do I know if the compiler vectorized my loop?
    answer: >-
      Compile with optimization, then disassemble the binary with `objdump -D`. In the
      target function, look for wide loads, stores, and arithmetic that process multiple elements
      per iteration instead of scalar steps.
  - question: I added `restrict` but my loop still doesn’t vectorize. What should I check next?
    answer: >-
      Confirm that the loop is countable and free of loop-carried dependencies or branches. If the loop
      includes conditionals, restructure or move the conditionals so the hot path is branch-free.
  - question: Can I use Clang instead of GCC for the steps?
    answer: >-
      Yes. The examples use `gcc`, but Clang can compile the same sources and generate assembly for
      inspection.
  - question: Which files should I compile in the `restrict` example, and what do I inspect?
    answer: >-
      Compile the example sources, such as `addvec.c` and `addvec_neon.c`, then disassemble the
      `addvec` binary. Inspect the `addvec` function for vectorized operations after applying
      `restrict`.
  - question: What should I look for in the dot product example to confirm Arm-specific instructions
      are used?
    answer: >-
      Build `dotprod.c` and inspect the assembly for `dotprod`. Look for vectorized integer operations
      that process multiple elements per iteration with vector loads and stores.
# END generated_summary_faq

author: Konstantinos Margaritis

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
    - GCC
    - Clang
    - Runbook

operatingsystems:
    - Linux
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: An update on GNU performance
        link: https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/update-on-gnu-performance
        type: blog
    - resource:
        title: Auto-Vectorization in LLVM
        link: https://llvm.org/docs/Vectorizers.html
        type: website
    - resource:
        title: GCC Autovectorization
        link: https://hpac.cs.umu.se/teaching/sem-accg-16/slides/08.Schmitz-GGC_Autovec.pdf
        type: documentation
    - resource:
        title: Auto-vectorization in GCC
        link: https://gcc.gnu.org/projects/tree-ssa/vectorization.html
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

---
title: Explore SME matrix operations with interactive visualizations

draft: true
cascade:
    draft: true
    
description: Trace Arm SME data movement through interactive ZA layout, operand preparation, and matrix multiplication visualizations.
    
minutes_to_complete: 40

who_is_this_for: This is an introductory topic for software developers who want to understand how Arm Scalable Matrix Extension (SME) moves matrix data before they read or write SME2 code.

learning_objectives:
    - Understand how ZA storage and ZA tiles are affected by Streaming Vector Length and data element size.
    - Explore transposition, packing, and padding to optimize memory layout.
    - Trace three General Matrix Multiplication (GEMM) visualizations and compare how gather-load and interleaved input layouts affect data movement.

prerequisites:
    - A browser with JavaScript enabled
    - Basic familiarity with vectors and matrix multiplication

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-12T19:39:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 628adebf53ab27b8d2071a02d01dd5653e0b2222152932642444e24ee2b11699
  summary_generated_at: '2026-11-12T19:39:01Z'
  summary_source_hash: 628adebf53ab27b8d2071a02d01dd5653e0b2222152932642444e24ee2b11699
  faq_generated_at: '2026-11-12T19:39:01Z'
  faq_source_hash: 628adebf53ab27b8d2071a02d01dd5653e0b2222152932642444e24ee2b11699
  summary: >-
    You'll use interactive visualizations to trace how Arm SME moves matrix data through ZA and
    prepares operands for multiplication. First, you'll inspect ZA tiles and follow in-place and
    incomplete-edge transposes. Next, you'll see how outer products accumulate results, then pack
    matrix A and pad matrix B for a GEMM. Finally, you'll compare gather loads with a transposed-and-interleaved
    layout and confirm that both produce the same output.
  # faqs:
  # - question: How do data type and vector length change the ZA tile layout?
  #   answer: >-
  #     Use **Data Type** and **Scalable Vector Length** to change the layout view. You'll see
  #     how the same ZA storage maps to different numbers and sizes of logical tiles.
  # - question: How do I check a transpose with an incomplete edge?
  #   answer: >-
  #     Compare **Input Matrix Data** with **Output Matrix Data**. You can follow the highlighted
  #     edge values to confirm that each reaches its transposed position without being lost or duplicated.
  # - question: How does a vector outer product contribute to matrix C?
  #   answer: >-
  #     Follow one column of matrix A and the corresponding row of matrix B. You'll see their
  #     outer product add a partial result to multiple elements of matrix C at the same time.
  #     Repeat for each column and row pair to see the complete result accumulate in ZA.
  # - question: What should I check after packing A and padding B?
  #   answer: >-
  #     In **Output Packed Data**, you should see matrix A's values in the new order, with zeros
  #     where its final tile has no input rows. In **Output Padded Data**, check that matrix B's
  #     original values remain in order and zeros fill the inactive columns.
  # - question: What changes between the gather-load and interleaved GEMM views?
  #   answer: >-
  #     Compare how each view loads matrix A. With gather loads, you read values from non-contiguous
  #     addresses. With the transposed-and-interleaved layout, you load from contiguous addresses. You can
  #     compare **Output Matrix Data** in both views to confirm that the results are identical.
# END generated_summary_faq

author:
    - Chris Sidebottom
    - Andrew Pickard

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Arm C1
tools_software_languages:
    - SME2

operatingsystems:
    - Linux
    - macOS
    - Windows

### Cross-platform metadata only
shared_path: true
shared_between:
    - mobile-graphics-and-gaming
    - laptops-and-desktops

further_reading:
    - resource:
        title: Arm SME and SME2 Programmer's Guide
        link: https://developer.arm.com/documentation/109246/latest
        type: documentation
    - resource:
        title: Accelerate matrix multiplication performance with SME2
        link: /learning-paths/cross-platform/multiplying-matrices-with-sme2/
        type: website
    - resource:
        title: Matrix-matrix multiplication with Neon, SVE, and SME compared
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/matrix-matrix-multiplication-neon-sve-and-sme-compared
        type: blog
    - resource:
        title: 'SME2 from scratch: Build matrix multiplication'
        link: https://www.youtube.com/watch?v=5peYlm5j0U8
        type: video

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

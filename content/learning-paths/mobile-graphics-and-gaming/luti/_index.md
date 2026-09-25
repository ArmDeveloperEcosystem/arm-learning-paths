---
title: Decode low-bit weights with Arm SME2 LUTI
description: Learn how to decode packed low-bit weights using Arm SME2 LUTI2 and LUTI4, and validate the results against a plain C implementation.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to efficiently decode packed low-bit weights inside a Scalable Matrix Extension 2 (SME2) matrix multiplication kernel with lookup-table instructions (LUTIs).

learning_objectives: 
    - Understand how LUTI2 expands packed 2-bit indices into arithmetic-ready values.
    - Compare equivalent low-bit decode paths implemented with plain C and SME2 LUTI2.
    - Validate the implementations against a scalar reference and inspect the generated SME2 instructions.
    - Apply a repeatable workflow for programming SME2 LUTI.

prerequisites:
    - Familiarity with C, AArch64 assembly, quantization, and matrix multiplication
    - Understanding of SME2 streaming mode and ZA storage; for more information, see [Accelerate matrix multiplication performance with SME2](/learning-paths/cross-platform/multiplying-matrices-with-sme2/)
    - A Mac system with Apple silicon (M4 or later), or an Android device with SME2 support
    - Make, wget, and LLVM Clang 22 or later for native macOS builds
    - For Android builds, a macOS or Linux build host with LLVM Clang 22 or later and Android NDK r29
    - For Android execution, an Android 15 or later device with SME2

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-23T20:40:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 93f9c0482a45773822c12d3216e3ad7ecb59acc95c0f1369bc747c59c6ac4762
  summary_generated_at: '2026-09-23T20:40:37Z'
  summary_source_hash: 93f9c0482a45773822c12d3216e3ad7ecb59acc95c0f1369bc747c59c6ac4762
  faq_generated_at: '2026-09-23T20:40:37Z'
  faq_source_hash: 93f9c0482a45773822c12d3216e3ad7ecb59acc95c0f1369bc747c59c6ac4762
  summary: >-
    You'll decode packed 2-bit and 4-bit weight indices with Arm SME2 LUTI2 and LUTI4, then validate
    the results against plain C references. First, you'll learn how LUTI expands low-bit codes through
    `ZT0`, Z registers, and `ZA`. Next, you'll configure a macOS or Android environment and compare
    LUTI2 with scalar decoding. Finally, you'll apply a four-step programming method to LUTI4 and
    chained LUTI4-to-LUTI2 examples, then examine additional LUTI feature paths.
  faqs:
  - question: How do I choose between running natively on my Mac and cross-compiling for my Android
      device?
    answer: >-
      Run natively on an arm64 macOS system with Apple silicon M4 or later, or cross-compile on
      macOS or Linux and run on an Android phone with SME2 support. Use LLVM Clang 22 or later
      in both cases, and use Android NDK r29 when targeting Android.
  - question: What result should I expect when I compare the plain C and SME2 paths?
    answer: >-
      You should see `PASS: LUTI2 SME2 matches plain C matmul.` after the program compares the
      matrices element by element. If the device prints `SKIP: No support for SME2 on this device.`,
      you haven’t validated the calculation, but you can still inspect the generated instructions
      on the build host.
  - question: Where does SME2 store the LUT that I reference with LUTI?
    answer: >-
      In the original SME2 forms used by the runnable examples, you load the lookup table into the
      fixed 512-bit `ZT0` register. LUTI2 and LUTI4 then use packed indices from source Z registers
      to select table entries. With `FEAT_LUT`, you can instead use one or two scalable Z registers
      as the table source.
  - question: When should I use LUTI2 versus LUTI4 in my code?
    answer: >-
      Use LUTI2 for 2-bit packed indices and LUTI4 for 4-bit packed indices. You can use LUTI4 with
      `FMOPA`, or chain LUTI4 and LUTI2 before `SDOT`.
  - question: How do I check that the compiler generated LUTI and the expected SME2 instructions?
    answer: >-
      Run `make disassemble-example-1` for the native macOS executable or `make
      disassemble-example-1-android` for the Android executable. Confirm that the output contains
      one LUTI2 instruction followed by four `SMOPA` instructions that target `ZA0` through `ZA3`.
      You can disassemble either executable without SME2 hardware.
# END generated_summary_faq

author:
    - Aude Vuilliomenet
    - Felix Johnny Thomasmathibalan

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Arm C1
tools_software_languages:
    - C
    - Assembly
    - LLVM
    - Clang
    - SME2
operatingsystems:
    - macOS
    - Linux
    - Android

further_reading:
    - resource:
        title: SME2 lookup table
        link: https://developer.arm.com/documentation/109246/0101/SME-Overview/SME-and-SME2/SME2-lookup-table
        type: documentation
    - resource:
        title: LUTI2 lookup-table read with 2-bit indices
        link: https://developer.arm.com/documentation/ddi0602/2025-12/SVE-Instructions/LUTI2--8-bit-and-16-bit---Lookup-table-read-with-2-bit-indices--8-bit-and-16-bit--?lang=en
        type: documentation
    - resource:
        title: LUTI4 lookup-table read with 4-bit indices
        link: https://developer.arm.com/documentation/ddi0602/2025-12/SVE-Instructions/LUTI4--8-bit-and-16-bit---Lookup-table-read-with-4-bit-indices--8-bit-and-16-bit--?lang=en
        type: documentation
    - resource:
        title: Set up your SME2 development environment
        link: /learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/
        type: documentation
    - resource:
        title: Understand SME2 outer products
        link: /learning-paths/cross-platform/multiplying-matrices-with-sme2/5-outer-product/
        type: documentation
    - resource:
        title: KleidiAI project
        link: https://github.com/ARM-software/kleidiai
        type: website
    - resource:
        title: Arm SME2 introduction
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: website
    - resource:
        title: Introduction to streaming and non-streaming mode
        link: https://arm-software.github.io/acle/main/acle.html#controlling-the-use-of-streaming-mode
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

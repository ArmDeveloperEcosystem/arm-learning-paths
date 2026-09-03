---
title: Decode low-bit weights with Arm SME2 LUTI instructions

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to efficiently decode packed low-bit weights inside a SME2 matrix multiplication kernel.

learning_objectives: 
    - Explain how LUTI2 expands packed 2-bit indices into arithmetic-ready values
    - Explain how to implement equivalent low-bit decode paths using plain C and SME2 LUTI2
    - Validate the implementations against a scalar reference and inspect the generated SME2 instructions
    - A recipe-based approach to programming with LUTI instructions

prerequisites:
    - Familiarity with C, AArch64 assembly, quantization, and matrix multiplication
    - Understanding of SME2 streaming mode and ZA storage; see [Accelerate matrix multiplication performance with SME2](/learning-paths/cross-platform/multiplying-matrices-with-sme2/)
    - A Mac system with Apple silicon (M4 or later), or an Android device with SME2 support
    - Git and LLVM Clang 22 or later for native macOS builds; Apple Clang 21 or later is supported as a fallback
    - Android NDK with LLVM Clang 21 or later for Android builds


author:
    - Aude Vuilliomenet
    - Felix Johnny Thomasmathibalan

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

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


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

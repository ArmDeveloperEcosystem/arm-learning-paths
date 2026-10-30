---
title: Disassemble macOS binaries to check for SME and SME2 instructions

draft: true
cascade:
    draft: true
    
description: Use otool and llvm-objdump on macOS to verify that a compiled binary contains SME and SME2 instructions.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to disassemble binaries on macOS and check for SME and SME2 instructions.

learning_objectives:
    - Identify the architecture, executable code, symbols, and supporting strings in a macOS binary.
    - Use two disassemblers to inspect instruction bytes, names, operands, and addresses.
    - Explain what disassembly can and can't tell you about SME and SME2 instructions.

prerequisites:
    - An Apple silicon Mac. You will compile and inspect the example program without running it, so SME2 hardware support isn't needed.
    - Xcode 26.6 or newer, which includes `clang`, `otool`, `nm`, and `llvm-objdump`
    - Basic familiarity with C, assembly language, and the macOS terminal

author: Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips: []
tools_software_languages:
    - Clang
    - LLVM
    - Assembly
    - Bash
operatingsystems:
    - macOS

further_reading:
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 1)
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: LLVM llvm-objdump command guide
        link: https://llvm.org/docs/CommandGuide/llvm-objdump.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

---
title: Disassemble Arm64 binaries to verify architecture extensions

description: Learn how to disassemble a final arm64 Mach-O executable and verify exact instruction bytes, operands, static addresses, and symbols for an Arm architecture extension.

minutes_to_complete: 45

who_is_this_for: This is for developers who need to verify that Arm architecture extension optimizations are present in a final binary.  Its also an excellent way to learn the basics of binary disassembly on Arm-based systems.

learning_objectives:
    - Identify the arm64 slice, executable code, symbols, and supporting strings in a Mach-O binary.
    - Decode instruction bytes and correlate mnemonics, operands, static program counters, and symbols with two disassemblers.
    - Distinguish build intent and supporting hints from static instruction evidence and runtime proof.

prerequisites:
    - An Apple silicon Mac. SME2 hardware is not required because you will build but not run the SME2 fixture.
    - Xcode 26.6 or compatible Xcode command-line tools with Clang, `otool`, `nm`, and `llvm-objdump`.
    - Basic familiarity with C, assembly language, and the macOS Terminal.

author: Geremy Cohen

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - Clang
    - LLVM
    - Assembly
    - Bash
operatingsystems:
    - macOS

further_reading:
    - resource:
        title: A64 Instruction Set Architecture
        link: https://developer.arm.com/documentation/ddi0602/latest/
        type: documentation
    - resource:
        title: LLVM llvm-objdump command guide
        link: https://llvm.org/docs/CommandGuide/llvm-objdump.html
        type: documentation
    - resource:
        title: Arm Performix install guide
        link: /install-guides/performix/
        type: documentation
    - resource:
        title: Find Code Hotspots with Arm Performix
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: learning-path
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: /learning-paths/servers-and-cloud-computing/performix-microarchitecture/
        type: learning-path
    - resource:
        title: Optimize memory access behavior using Arm Performix and the Arm MCP Server
        link: /learning-paths/servers-and-cloud-computing/performix-memory-access/
        type: learning-path
    - resource:
        title: Optimize memory access behavior using Arm Performix and the Arm MCP Server
        link: https://www.arm.com/technologies/sme2
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

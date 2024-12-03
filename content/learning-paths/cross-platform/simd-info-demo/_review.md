---
review:
    - questions:
        question: >
            What is SIMD.info?
        answers:
            - It's an online resource for SIMD C intrinsics for all major architectures.
            - It's an online forum for SIMD developers.
            - It's a book about SIMD programming.
        correct_answer: 1                    
        explanation: >
            While it allows comments in the SIMD intrinsics, SIMD.info is not a forum. It is an online free resource to assist developers porting C code between popular architectures, for example, from SSE/AVX/AVX512 to Arm ASIMD.

    - questions:
        question: >
            What architectures are listed in SIMD.info?
        answers:
            - Intel SSE and Arm ASIMD.
            - Power VSX and Arm ASIMD/SVE.
            - Intel SSE4.2/AVX/AVX2/AVX512, Arm ASIMD, Power VSX.
        correct_answer: 3
        explanation: >
            SIMD.info supports Intel SSE4.2/AVX/AVX2/AVX512, Arm ASIMD, Power VSX as SIMD architectures. Work is in progress to include Arm SVE/SVE2, MIPS MSA, RISC-V RVV 1.0, s390 Z and others.

    - questions:
        question: >
            What are SIMD.info's major features?
        answers:
            - Hierarchical tree, search, and AI code translation.
            - Search, hierarchical tree, and code examples.
            - Hierarchical tree, search, intrinsics comparison, code examples, equivalents mapping, and links to official documentation.
        correct_answer: 3
        explanation: >
            SIMD.info provides multiple features, including a hierarchical tree, search facility, intrinsics comparison, code examples, equivalents mapping, links to official documentation, and others. AI code translation is not a feature of SIMD.info but is the focus of another project, SIMD.ai.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add aditional context if desired


review:
    - questions:
        question: >
            What SIMD instructions sets are supported by the latest Arm processors?
        answers:
            - "SSE and AVX"
            - "NEON and SVE"
        correct_answer: 2
        explanation: >
            NEON and SVE and supported by Neoverse V1, Neoverse N2 and Cortex-X2.
    - questions:
        question: >
            I need rewrite all my code when migrating to aarch64.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Most applications can be migrated without rewriting any code. Common libraries and tools are already available on aarch64. If your application uses intrinsics, you can use tools like SIMD Everywhere with minimal code changes.
    - questions:
        question: >
            If I don't have physical access to Arm hardware, can I still start migrating to Arm?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            Migration to Arm can be done without physical access to Arm hardware by using e.g., QEMU or remote hardware. A cross-platform built container can run in QEMU and a user can easily access AWS Graviton remote using ssh. Don't forget, the very first step is to analyze the current system!


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

---
review:
    - questions:
        question: >
            How can using MCA be useful?
        answers:
            - It can provide a performance estimation that can be used to understand and improve performance.
            - It can provide an improved version of a given code snippet.
        correct_answer: 1
        explanation: >
            MCA simulates the execution of a given snippet of assembly in a loop and provides performance measurements that can then be used to understand and improve performance.

    - questions:
        question: >
            MCA can offer performance metrics for the following as input:
        answers:
            - A snippet of code, the language does not matter.
            - A snippet of assembly code.
        correct_answer: 2
        explanation: >
            MCA takes assembly code as input.

    - questions:
        question: >
            When using Compiler Explorer, what does llvm-mca take as input?
        answers:
            - The source code provided.
            - The disassembly of the source code.
        correct_answer: 2
        explanation: >
            Compiler explorer takes as input the source code, compiles it and shows the disassembly output. It then can run llvm-mca on the disassembly of the source code.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

---
review:
    - questions:
        question: >
            What is the size of the ZA storage?
        answers:
            - SVL x SVL bits
            - SVL x SVL bytes
            - SVL x SVL floats
        correct_answer: 1
        explanation: >
            The ZA storage is a two-dimensional array of SVL x SVL bits, where SVL (the Effective Streaming SVE Vector Length), is a power of two in the range 128 to 2048 bits.

    - questions:
        question: >
            When is the ZA array activated at run-time?
        answers:
            - When the first FMOPA instruction is executed
            - When an SMSTART instruction is executed
            - When the processor is powered-up/reset (or the FVP model is started)
        correct_answer: 2
        explanation: >
            The ZA array is activated at run-time when an SMSTART instruction is executed.

    - questions:
        question: >
            How can the contents of the ZA tiles be viewed in the Arm Debugger?
        answers:
            - The ZA array is memory mapped, so the tiles can be viewed by their address in the Memory view
            - The tiles reside on the stack, so can be viewed as an offset from the Stack Pointer
            - The Registers view can show the contents of the various tiles in a variety of formats
        correct_answer: 3
        explanation: >
            The ZA tiles can be viewed in the Registers view in a variety of formats.  Their contents can also be viewed in the Commands view by using `output` commands.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

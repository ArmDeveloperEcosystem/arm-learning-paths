---
review:
    - questions:
        question: >
            How large is the ZA storage?
        answers:
            - (SVL/8) x (SVL/8) bits
            - (SVL/8) x (SVL/8) bytes
            - (SVL/8) x (SVL/8) floats
        correct_answer: 2
        explanation: >
            The ZA storage is a two-dimensional array of (SVL/8) x (SVL/8) bytes. Since SVL is a power of two in the range 128 to 2048 bits, (SVL/8) will be a power of two in the range 16 to 256 bytes.

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

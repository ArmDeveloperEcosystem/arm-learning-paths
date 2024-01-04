---
review:
    - questions:
        question: >
            What are the supported sizes for the ZA storage in SME?
        answers:
            - 16x16, 32x32, 64x64, 128x128, and 256x256 bits
            - 16x16, 32x32, 64x64, 128x128, and 256x256 bytes
            - 16x16, 32x32, 64x64, 128x128, and 256x256 floats
        correct_answer: 2
        explanation: >
            The ZA storage is two-dimensional array of 8-bit elements, a power of two in the range 16 to 256 bytes.

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

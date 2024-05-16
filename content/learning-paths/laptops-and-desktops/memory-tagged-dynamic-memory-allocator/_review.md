---
review:
    - questions:
        question: >
            Is MTE a software or hardware solution?
        answers:
            - Hardware
            - Software
            - Both, a combination of software and hardware
        correct_answer: 3
        explanation: >
            Memory tag checks are done by the CPU but software must set those tags and choose their values appropriately.

    - questions:
        question: >
            Of the 16 possible tag values (0-15), which ones are reserved for hardware use?
        answers:
            - 0 and 15
            - No tag values are reserved, software may set any value in the range 0-15.
            - 0
        correct_answer: 2
        explanation: >
            Software may set an allocation tag to any value in the range 0-15.
            It is convention that the tag 0 is used for newly initialised memory. Therefore, software may choose to use it only for that purpose.

    - questions:
        question: >
            How much memory does an allocation tag apply to?
        answers:
            - 16 bytes
            - 1 byte
            - A variable amount of memory.
        correct_answer: 1
        explanation: >
            Each allocation tag applies to a "granule". This granule is 16 bytes in size and is at a 16 byte aligned address.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

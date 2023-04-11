---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add additional context if desired


review:
    - questions:
        question: >
            You only can only emulate 32-bit Arm machine targets in QEMU.
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            With QEMU you can emulate both 32-bit and 64-bit Arm targets. 


    - questions:
        question: >
            Poky is a reference distribution of Yocto Linux that supports QEMU targets by default.
        answers:
            - "True"
            - "False"
        correct_answer: 1                     
        explanation: >
            With Poky recipes to build and run on QEMU example targets are supported by default.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

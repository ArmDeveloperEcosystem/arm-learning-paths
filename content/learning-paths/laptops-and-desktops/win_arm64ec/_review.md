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
            Applications can be built with Arm64EC on Windows 10 machines.
        answers:
            - "True"
            - "False"
        correct_answer: 2               
        explanation: >
            Arm64EC requires an Arm machine running Windows 11.

    - questions:
        question: >
            Arm64EC code is not interoperable with x64 code running under emulation.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Arm64EC code is interoperable with x64 code. Arm64EC code runs with native Arm performance, whereas any x64 code runs using emulation on Windows 11. 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

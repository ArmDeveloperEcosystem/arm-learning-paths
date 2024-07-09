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
            The Raspberry Pi Pico SDK works only on Raspberry Pi OS.
        answers:
            - "True"
            - "False"
        correct_answer: 2                  
        explanation: >
            The Pico SDK works on many different operating systems, including Ubuntu, Debian, Windows, and macOS.
    - questions:
        question: >
            Which build system is used by the Pico SDK and C/C++ applications?
        answers:
            - "ninja"
            - "cmake"
            - "bazel"
            - "nmake"
        correct_answer: 2                  
        explanation: >
            The Pico SDK uses cmake for C/C++ applications
    - questions:
        question: >
            Debugging with gdb requires connecting the SWD pins on the Raspberry Pi Pico using jumper wires.
        answers:
            - "True"
            - "False"
        correct_answer: 1                  
        explanation: >
            True, the SWD pins must be used for interactive debugging. This may require soldering headers to the Pico board if the board didn't arrive with headers installed on the SWD pins.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

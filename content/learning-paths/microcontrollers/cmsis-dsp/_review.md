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
            Which header file must you include in your sources to access the library functions?
        answers:
            - arm_dsp.h
            - arm_math.h
            - arm_cmsis.h
        correct_answer: 2             
        explanation: >
            The library is released in source form. The functions are declared in arm_math.h, which resides in the Include folder of the repository.
    - questions:
        question: >
            Does the CMSIS-DSP library provide vectorized implementations of algorithms?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
            The library is provides vectorized versions of most algorithms for Helium and of most f32 algorithms for Neon.
    - questions:
        question: >
            How is CMSIS-DSP library provided?
        answers:
            - Within a CMSIS-Pack
            - In source code on Github
            - Both
        correct_answer: 3
        explanation: >
            CMSIS-DSP is distributed in source form on Github and within the CMSIS-Core software pack. It is licensed under Apache License 2.0.
              

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

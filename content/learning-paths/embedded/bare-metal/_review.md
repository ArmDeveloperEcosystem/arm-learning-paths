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
            What mechanism does Arm Compiler for Embedded use to define the target memory map?
        answers:
            - "Simple loading"
            - "Shuffle loading"
            - "Scatter loading"
        correct_answer: 3
        explanation: >
            The name derives from the idea that multiple memory regions are _scattered_ in the memory map at load and execution time.

    - questions:
        question: >
            Adding which symbol to your code ensures that all semihosting calls have been removed?
        answers:
            - "__use_no_semihosting"
            - "__no_semihosting"
            - "__semihosting_false"
        correct_answer: 1
        explanation: >
            At link time, an error will be thrown if there are any functions using semihosting.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

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
            Does uVision support semihosting?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            uVision does not support semihosting. It has a feature called Event Recorder for printf functionality.

    - questions:
        question: >
            Which function is used to invoke an OS thread?
        answers:
            - "osKernelInitialize()"
            - "osKernelStart()"
            - "osThreadNew()"
        correct_answer: 3
        explanation: >
            osThreadNew() is called before osKernelStart() to define the main thread, and then by the main thread to start other threads.

    - questions:
        question: >
            Event Recorder can only be used with FVPs?
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Event Recorder supports both FVPs and real hardware.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

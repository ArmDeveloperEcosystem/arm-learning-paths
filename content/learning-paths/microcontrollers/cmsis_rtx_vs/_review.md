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
          What is the purpose of the `osKernelStart()` function?
        answers:
          - "To create the main application thread"
          - "To start the RTOS kernel and begins thread switching"
          - "To update the system clock"
        correct_answer: 2
        explanation: >
          `osKernelStart()` starts the RTOS kernel and enables thread switching, making it essential for multitasking.
  - questions:
        question: >
          What happens if the code execution reaches the infinite while(1) loop in the main function?
        answers:
          - "All threads are successfully started."
          - "Something went wrong, likely with the platform initialization."
          - "The RTOS has successfully initialized the kernel."
        correct_answer: 2
        explanation: >
          Reaching the infinite `while(1)` loop in the main function suggests an error occurred during platform initialization.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

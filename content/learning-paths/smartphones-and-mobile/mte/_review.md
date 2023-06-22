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
            MTE allows developers to find memory-related bugs quickly.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            MTE exposes hard to find buffer overflow errors and use-after-free errors.

    - questions:
        question: >
            Which operating system is not likely to implement MTE?
        answers:
            - "Linux"
            - "Android"
            - "FreeRTOS"
        correct_answer: 3
        explanation: >
            MTE is available in Linux and Android. It can be added to any operating system which runs on Armv8.5-A or Armv9-A processors.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

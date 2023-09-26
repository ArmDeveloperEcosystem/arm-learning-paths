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
            A SysTick timer is a 32-bit down counter.
        answers:
            - "True"
            - "False"
        correct_answer: 2             
        explanation: >
            SysTick timer is a 24-bit down counter in-built within Cortex-M processors.
    - questions:
        question: >
            The MPU regions of Cortex-M processors based of Armv8-M architecture can be programmed in:
        answers:
            - Privileged state only
            - Unprivileged state only
            - Both privileged and unprivileged states
        correct_answer: 1                  
        explanation: >
            MPU registers can be programmed only in privileged state.
              

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

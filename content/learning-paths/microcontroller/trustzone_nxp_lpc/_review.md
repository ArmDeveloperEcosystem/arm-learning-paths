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
            The Keil µVision IDE only works on Windows.
        answers:
            - "True"
            - "False"
        correct_answer: 1                  
        explanation: >
            The Keil MDK Tools are supported only on Windows.
    - questions:
        question: >
            What is the first instruction that has to be executed on the Cortex-M33 when non-secure software calls a secure function?
        answers:
            - "BLXNS"
            - "SG"
            - "BLX"
        correct_answer: 2                  
        explanation: >
            Secure Gateway (SG) should be the very first instruction to avoid security violations
    - questions:
        question: >
            Viewing the UART output from the application requires a connection on which port?
        answers:
            - "COM"
            - "USB"
        correct_answer: 1                  
        explanation: >
            The application uses a UART for I/O. Viewing the UART output requires connecting to the COM port on your machine.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

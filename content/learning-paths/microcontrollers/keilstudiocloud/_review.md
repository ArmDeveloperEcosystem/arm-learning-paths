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
            What do you need to install to access Keil Studio Cloud?
        answers:
            - "Arm Compiler for Embedded"
            - "Arm Fast Models"
            - "Arm Fixed Virtual Platforms (FVPs)"
            - "A browser"
        correct_answer: 4
        explanation: >
            Keil Studio Cloud is a zero-installation tool that runs out of your browser.

    - questions:
        question: >
            Which project formats are supported by Keil Studio Cloud?
        answers:
            - "CMSIS"
            - "Mbed OS"
            - "both"
        correct_answer: 3
        explanation: >
            Keil Studio Cloud supports both, CMSIS and Mbed OS based projects.
               
    - questions:
        question: >
            You must use the supplied compiler version with Keil Studio Cloud?
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Currently, you can only use the compiler version that is supplied with the tool.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

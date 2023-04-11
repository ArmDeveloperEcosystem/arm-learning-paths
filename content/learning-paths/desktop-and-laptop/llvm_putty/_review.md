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
            Visual Studio supports native build of Windows on Arm applications?
        answers:
            - "True"
            - "False"
        correct_answer: 1               
        explanation: >
            Starting with Visual Studio 2022 version 17.4, you can natively build applications for Windows on Arm.

    - questions:
        question: >
            Does LLVM toolchain support native build of Windows on Arm applications?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                     
        explanation: >
            LLVM version 12.0.0 introduced the first release with native build support for Windows on Arm applications.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

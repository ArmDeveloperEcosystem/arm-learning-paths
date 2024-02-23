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
            Which of these are NOT a component of Arm Development Studio?
        answers:
            - "Arm Compiler for Embedded"
            - "Arm Fast Models"
            - "Arm Fixed Virtual Platforms (FVPs)"
            - "Arm Streamline"
        correct_answer: 2
        explanation: >
            Arm Fast Models is a separate component, enabling you to build virtual representations of real hardware. The supplied FVPs are pre-built with Fast Model technology.

    - questions:
        question: >
            Which flavor of DSTREAM hardware supports 32-bit parallel trace output?
        answers:
            - "DSTREAM-ST"
            - "DSTREAM-PT"
            - "DSTREAM-HT"
            - "DSTREAM-XT"
        correct_answer: 2
        explanation: >
            DSTREAM-PT supports 32-bit wide trace capture at up to 300 MHz DDR.
               
    - questions:
        question: >
            You must use the supplied compiler version with your Arm Development Studio installation?
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Other compiler versions can be downloaded and installed for use with Development Studio.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

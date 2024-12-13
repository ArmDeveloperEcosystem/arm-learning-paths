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
            The Arm Total Compute reference software stack is ____?
        answers:
            - "Open source"
            - "Proprietary"
        correct_answer: 1
        explanation: >
            The Total Compute reference software stack is a fully integrated open-source stack, from Firmware up to Android.

    - questions:
        question: >
            Which of the following is NOT a component of the software stack?
        answers:
            - "Trusted firmware"
            - "Android"
            - "CMSIS"
            - "Arm NN"
        correct_answer: 3
        explanation: >
            The stack includes open-source code available from these upstream projects: SCP firmware, Trusted firmware, Linux kernel, Android, and Arm NN.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

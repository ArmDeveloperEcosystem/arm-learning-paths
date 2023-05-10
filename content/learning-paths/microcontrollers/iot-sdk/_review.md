---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add aditional context if desired


review:
    - questions:
        question: >
            Arm Total Solutions for IoT are available as SDKs for use with Arm Virtual Hardware.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            True. Arm Virtual Hardware provides a ready to use environment to build and test your applications, integrated into CI/CD and MLOps workflows.
    - questions:
        question: >
            You can send data from a simulated IoT device to AWS IoT cloud services to test software without having a physical board.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            True. You can use the Corstone-300 Fixed Virtual Platform (FVP) for software testing and confirm operation with AWS IoT services.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

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
            Which command do you use to run the Python interpreter for Arm64?
        answers:
            - "py -3.12-arm64"
            - "python -3.12-arm64"
            - "py -3.12 -arm64"
            - "python -3.12 -arm64"
        correct_answer: 1               
        explanation: >
            You can use py -3.12-arm64 as an alias to the Python interpreter for Arm64

    - questions:
        question: >
            When does pip build a package from the source code?
        answers:
            - "Always"
            - "When the NuGet package is unavailable"
            - "When the wheel is unavailable for a given platform"
            - "Never"
        correct_answer: 3
        explanation: >
            By default, pip builds a Python package from sources when there is no platform-specific wheel available

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

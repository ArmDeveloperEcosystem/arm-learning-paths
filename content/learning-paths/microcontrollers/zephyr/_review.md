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
            Is the Zephyr RTOS open source?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
            The source is freely available for use under the Apache License 2.0.
    - questions:
        question: >
            Has Zephyr RTOS been ported to Corstone-300?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                  
        explanation: >
            This platform is supported (as MPS3 AN547). For a full list of supported Arm platforms, see https://docs.zephyrproject.org/latest/boards/arm/index.html
        

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

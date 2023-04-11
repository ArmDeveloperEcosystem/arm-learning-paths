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
            MDK supports code coverage on FVPs and real hardware
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Both FVPs and (suitable) real hardware are supported.
    - questions:
        question: >
            What feature does real hardware need to perform code coverage
        answers:
            - "SysTick"
            - "JTAG"
            - "ETM trace"
        correct_answer: 3
        explanation: >
            ETM trace is needed to generate the instruction trace data used to determine the code coverage. You will also need to use an appropriate debug adapter such as ulinkPro.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

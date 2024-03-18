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
            Arm IP Explorer simulations are cycle-accurate.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Arm IP Explorer uses RTL simulation technology to enable fully cycle-accurate simulation.

    - questions:
        question: >
            What functions are used in the code to mark particular sections of code to be benchmarked.
        answers:
            - start_marker()
            - stop_marker()
            - both
        correct_answer: 3
        explanation: >
            The use of these two functions allow you to see the cycle count of just the algorithm of interest.
            Other code, such as boot code and initialization, or post-execution printf of results, can be excluded.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

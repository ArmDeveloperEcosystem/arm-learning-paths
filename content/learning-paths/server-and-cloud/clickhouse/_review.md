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
            Can ClickBench be used to measure only the performance of ClickHouse DBMS?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            ClickBench can be used to measure the performance of many different Database Management systems running on different architectures.

    - questions:
        question: >
            How many times is each query run used the standard scripts in ClickBench?
        answers:
            - "One"
            - "Two"
            - "Three"
        correct_answer: 3
        explanation: >
            Each query is run three times.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

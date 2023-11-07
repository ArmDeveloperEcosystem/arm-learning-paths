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
            The `counting model` is used for obtaining aggregate counts of occurrences of special events.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            In counting model, the occurrences of PMU events are simply aggregated over given time period.

    - questions:
        question: >
            The `sampling model` is used for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            In sampling model, the frequencies of event occurrences produced by program determine "hot" locations at the function, basic block, and/or instruction levels.

    - questions:
        question: >
            The purpose of using the PMU is for performance analysis and debugging.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, the purpose of using the PMU is for performance analysis and debugging. The PMU provides a range of events, such as cache miss, TLB miss, CPU cycles, executed instructions, for performance profiling and debugging. The PMU can be used by performance analysis tools.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

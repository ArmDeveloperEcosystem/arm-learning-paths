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
            The counting model is used for obtaining aggregate counts of occurrences of special events.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            In the counting model, the occurrences of PMU events are simply aggregated over a given time period.

    - questions:
        question: >
            The sampling model is used for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            In the sampling model, the frequencies of event occurrences produced by the program determine "hot" locations at the function, basic block, and/or instruction levels.

    - questions:
        question: >
            WindowsPerf can be used and executed only on native Windows on Arm hardware, and not in a virtual environment.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, WindowsPerf currently supports a native Windows on Arm environment only.

    - questions:
        question: >
            The Arm Statistical Profiling Extension (SPE) is an optional feature in ARMv8.2 hardware.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, the Arm Statistical Profiling Extension (SPE) is an optional feature in ARMv8.2 hardware that allows CPU instructions to be sampled and associated with the source code location where that instruction occurred.

    - questions:
        question: >
            SPE stands for Statistical Profiling Extension.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, the Arm Statistical Profiling Extension (SPE) is an optional feature in ARMv8.2 hardware.

    - questions:
        question: >
            load_filter is one of SPE filters supported by WindowsPerf?
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, load_filter together with store_filter and branch_filter are SPE filters supported by WindowsPerf.

    - questions:
        question: >
            store_filter is one of SPE filters supported by WindowsPerf?
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, load_filter together with store_filter and branch_filter are SPE filters supported by WindowsPerf.

    - questions:
        question: >
            branch_filter is one of SPE filters supported by WindowsPerf?
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, load_filter together with store_filter and branch_filter are SPE filters supported by WindowsPerf.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

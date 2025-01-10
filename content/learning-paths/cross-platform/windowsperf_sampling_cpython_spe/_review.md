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
            The Arm Statistical Profiling Extension (SPE) is an optional feature in Armv8-A.2 hardware.
        answers:
            - "True."
            - "False."
        correct_answer: 1
        explanation: >
            Yes, the Arm Statistical Profiling Extension (SPE) is an optional feature in Armv8.2 hardware that allows CPU instructions to be sampled and associated with the source code location where that instruction occurred.
    - questions:
        question: >
            SPE is an acronym for Statistical Profiling Extension. True or false?
        answers:
            - "True."
            - "False."
        correct_answer: 1
        explanation: >
            Yes, SPE is the abbreviated form of Statistical Profiling Extension.
    - questions:
        question: >
            load_filter is one of SPE filters supported by WindowsPerf. True or false?
        answers:
            - "True."
            - "False."
        correct_answer: 1
        explanation: >
            Yes, load_filter, store_filter, and branch_filter are SPE filters that WindowsPerf supports.

   
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

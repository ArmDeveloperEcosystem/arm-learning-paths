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
            Why benchmark cloud-based server instances?
        answers:
            - "Because fastest is best"
            - "To select an appropriate configuration for your workload"
            - "To verify the server is working correctly"
        correct_answer: 2
        explanation: >
            Cloud based server instances are provided with a number of configuration options. It is best to select an appropriate configuration to balance operating cost and necessary performance.

    - questions:
        question: >
            Geekbench is:
        answers:
            - "A cross-platform benchmark"
            - "Only suitable for Arm platforms"
            - "Only suitable for single CPU systems"
        correct_answer: 1
        explanation: >
            Geekbench is a cross-platform benchmark, and can be used on single and multi-core systems.
               
    - questions:
        question: >
            Should you rely only on the Geekbench score when deciding on your server configuration?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            Though useful, Geekbench is only one of a number of available benchmarks. See other learning paths to see how to run and benchmark other applications.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

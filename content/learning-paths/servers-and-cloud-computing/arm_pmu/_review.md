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
            The performance monitoring unit (PMU) can be accessed from user space by default.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            The register pmuserenr_el0 must be written to by EL1 (kernel) software before user space can access all the PMU system registers for configuring event counting.

    - questions:
        question: >
            Which of the following is not an option for accessing HW counters.
        answers:
            - "PAPI"
            - "Assembly"
            - "Linux perf_events"
            - "top"
        correct_answer: 4                  
        explanation: >
            Top is a tool that reports CPU utilization at the process level.
               
    - questions:
        question: >
            CPUs typically support a limited number of event counters.
        answers:
            - "True"
            - "False"
        correct_answer: 1                    
        explanation: >
            Since counters take up area on a die, the number of counters supported is usually limited to 4-8.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

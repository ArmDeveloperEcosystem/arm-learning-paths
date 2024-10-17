---
review:
    - questions:
        question: >
            The Process Watch GitHub repository depends on other GitHub repositories.
        answers:
            - "True."
            - "False."
        correct_answer: 1                    
        explanation: >
            The Process Watch repo is dependent on the bpftool repo and the Capstone repo. Follow the correct instructions to clone, including using the --recursive argument.

    - questions:
        question: >
            Process Watch uses the Linux perf_events interface to sample branch predictions.
        answers:
            - "True."
            - "False."
        correct_answer: 2                   
        explanation: >
            Process Watch does use the Linux perf_events interface but it is for sampling retired instructions.
               
    - questions:
        question: >
            Process Watch can tell me whether my workloads are using specific instructions or features.
        answers:
            - "True."
            - "False."
        correct_answer: 1          
        explanation: >
            Process Watch can be used to indicate whether certain instructions or features or groups of instructions are being retired.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

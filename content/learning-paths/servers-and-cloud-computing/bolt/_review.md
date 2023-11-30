---
review:
    - questions:
        question: >
            Why do you need to compile your executable with additional flags?
        answers:
            - BOLT needs the compiler to do no optimisation itself
            - BOLT prefers to be linked with relocations
            - Speed up compile time
        correct_answer: 2
        explanation: >
            An executable containing helps it get maximum performance gains.

    - questions:
        question: >
            Which of these perf record commands would you use to record ETM?
        answers:
            - perf record -e cs_etm/@tmc_etr0/u
            - perf record -e cycles:u
            - perf record -e arm_spe/branch_filter=1/u
        correct_answer: 1
        explanation: >
            The other answers record cycles samples and Arm SPE.
               
    - questions:
        question: >
            Which aggregation method should you prefer?
        answers:
            - Basic Aggregation
            - Branch Aggregation
            - Neither both perform the same
        correct_answer: 2
        explanation: >
            Branch Aggregation outputs more information into the .fdata file and that can improve performance gains.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

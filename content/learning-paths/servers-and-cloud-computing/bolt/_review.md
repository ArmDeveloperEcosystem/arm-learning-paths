---
review:
    - questions:
        question: >
            Why do you need to compile your executable with additional flags?
        answers:
            - BOLT needs the compiler to do no optimization itself
            - BOLT prefers to be linked with relocations
            - Speed up compile time
        correct_answer: 2
        explanation: >
            An executable containing relocations helps it get maximum performance gains.

    - questions:
        question: >
            Which of these perf record commands would you use to record ETM?
        answers:
            - perf record -e cs_etm//u
            - perf record -e cycles:u
            - perf record -e arm_spe/branch_filter=1/u
        correct_answer: 1
        explanation: >
            The other answers record cycles samples and Arm SPE.
               
    - questions:
        question: >
            Which tool converts the performance profile to BOLT format?
        answers:
            - perf2bolt
            - llvm-bolt
            - perf convert
        correct_answer: 1
        explanation: >
            perf2bolt converts the performance profile to BOLT format.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

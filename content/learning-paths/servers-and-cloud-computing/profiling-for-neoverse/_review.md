---
review:
    - questions:
        question: >
            How do Streamline CLI tools generate reports?
        answers:
            - Using three distinct processes, `sl-record`, `sl-analyze` and `sl-format.py`.
            - Using the Streamline GUI.
        correct_answer: 1                    
        explanation: >
            Streamline CLI tools are command-line operations that enable you to generate reports containing comprehensive performance metrics as your application runs on an Arm-based server.

    - questions:
        question: >
            What should you do if you see functions with a high branch mispredict rate and significant branch MPKI number?
        answers:
            - Nothing, this is not an important metric.
            - Reduce branching in the affected functions.
            - Try to improve the predictability of branches, or convert unpredictable branches into conditional select instructions.
        correct_answer: 3                   
        explanation: >
            Bad speculation is expensive because it causes slots to be kept busy processing instructions that are then discarded. Branches can help to speed up your application, but not when computation is unpredictable.
               
    - questions:
        question: >
            What is the Frontend phase responsible for?
        answers:
            - The execution of micro-ops by the processing pipelines inside the core.
            - Instruction fetch, decode, and dispatch.
            - The resolution of micro-ops that are architecturally complete.
        correct_answer: 2          
        explanation: >
            This phase handles fetching instructions from the instruction cache, decoding those instructions, and adding the resulting micro-ops to the backend execution queues.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

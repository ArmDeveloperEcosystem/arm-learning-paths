---
review:
    - questions:
        question: >
            ITLB_WALK counts page table walks due to TLB maintenance operations.
        answers:
            - True
            - False
        correct_answer: 2                  
        explanation: > 
            ITLB_WALK counts any page table walk driven by an I-side memory access, excluding those caused by TLB maintenance operations.

    - questions:
        question: >
            ASE_SPEC differs from ASE_INST_SPEC because ASE_SPEC only counts speculatively executed Advanced SIMD operations, excluding load, store, and move micro-operations.
        answers:
            - True
            - False
        correct_answer: 1
        explanation: >
            ASE_SPEC does not count any micro-operations that result from the instruction. ASE_INST_SPEC, however, does count micro-operations.

    - questions:
        question: >
            Which of the following is true regarding the difference between PMU events that count speculatively executed instructions/operations and PMU events that count retired instructions/operations (Example: OP_SPEC vs OP_RETIRED)?
        answers:
            - Speculatively executed PMU event counts are always greater than or equal to retired PMU event counts
            - Speculatively executed PMU events count architecturally executed operations or instructions
            - Speculatively executed PMU event counts are always less than retired PMU event counts
            - Speculatively executed PMU event counts and retired PMU event counts can be higher, lower or equal to each other
        correct_answer: 1
        explanation: > 
            Speculatively executed instructions/opertations will count instructions that were architecturally executed as well as instructions that were not architecturally executed. Architecturally executed instructions/operations are also refered to as "retired" or "committed." 

    - questions:
        question: >
            What scenario triggers an ITLB walk? 
        answers:
            - A memory access driven by an instruction
            - An instruction Cache Maintenance Operation
            - A translation fault
            - An instruction-side memory translation that has not been accessed before
        correct_answer: 4
        explanation: >
            An I-TLB walk occurs when there is a translation miss in the L1 I-TLB and the L2 TLB driven by an I-side memory access. 




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

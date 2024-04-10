---
review:
    - questions:
        question: >
            Some PMU events will not occur on the Neoverse CPUs if they are not provided by a system component.
        answers:
            - True
            - False
        correct_answer: 1                    
        explanation: >
            Events like LL_CACHE_RD count transactions returned from outside of the Neoverse N2 CPU. 

    - questions:
        question: >
            ITB_WALK counts page table walks due to TLB maintenance operations.
        answers:
            - True
            - False
        correct_answer: 2                  
        explanation: > 
            ITLB_WALK counts any page table walk driven by an I-side memory access, excluding those caused by TLB maintenance operations.
               
    - questions:
        question: >
            Which of the following events always occurs during an L2 D-cache access from a load instruction?
        answers:
            - L2D_CACHE_REFILL
            - L2D_CACHE_RD
            - BUS_ACCESS
            - L2D_CACHE_WR
        correct_answer: 2          
        explanation: >
            L2D_CACHE_RD counts an L2 D-cache access caused by a load or read. A refill and bus access only occurs when there is a miss. L2D_CACHE_WR is only counted when an L2 D-cache access is caused by a store or write.

    - questions:
        question: >
            What scenario will not trigger L1D_CACHE_WB in a Neoverse N2 core?
        answers:
            - A writeback from the L1-D cache as a result of a Cache Maintenance Operation
            - A full line write to the L2, without writing to the L1 D-cache 
            - A cache line writeback to the L2 cache as a result of a snoop 
            - A victim cache line eviction from the L1 D-cache
        correct_answer: 2
        explanation: >
            L1D_CACHE_WB counts any writeback of dirty data from the L1 D-cache to the L2 cache, including writebacks from snoops, CMOs or evictions. Writing directly to the L2 cache, such as in write-streaming mode, will not result in a writeback from the L1 D-cache to the L2. L1D_CACHE_WB is Implementation Defined whether the event counts for 

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
            Speculatively executed instructions/operations will count instructions that were architecturally executed as well as instructions that were not architecturally executed. Architecturally executed instructions/operations are also referred to as "retired" or "committed." 

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

    - questions:
        question: >
            Why do I-side cache refills typically count less than D-side cache refills?
        answers:
            - There will always be fewer instructions
            - I-side cache accesses can result in a snoop to the D-side cache
            - Instructions use up less memory than data
        correct_answer: 2
        explanation: >
            In the Neoverse N2, instruction fetches that miss in the I-cache will look in the D-cache and the L2 cache.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

---
review:
    - questions:
        question: >
            Which is not a good place to acquire supporting PMU events for the specified CPU?
        answers:
            - CPU TRM
            - ARM-ARM
            - Github repository - Machine-readable data
        correct_answer: 2                   
        explanation: >
            ARM-ARM documents all the common architectural and microarchitectural PMU events. For a specified CPU, not all of them are supported. You should refer to the CPU TRM or Github repository - Machine-readable data.

    - questions:
        question: >
            Profiling with PMU at EL2/EL3 or in the secure state is typically restricted to prevent potential information leakage.
        answers:
            - "True"
            - "False"
        correct_answer: 1                   
        explanation: >
            True. You can set the MDCR_EL2 or MDCR_EL3 to make the PMU profiling working.
               
    - questions:
        question: >
            For each PMU in the Armv8-A CPU, one cycle counter and six event counters are supported.
        answers:
            - "True"
            - "False"
        correct_answer: 2          
        explanation: >
            False. It depends. For the number of the event counters, you should refer to the CPU TRM or the PMCR_EL0.N bit field.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

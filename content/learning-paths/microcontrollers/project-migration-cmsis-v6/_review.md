---
review:
    - questions:
        question: >
            Is there a simple replacement pack available for ARM.CMSIS.5.x.x?
        answers:
            - Yes
            - No
        correct_answer: 2                    
        explanation: >
            Some CMSIS components have been removed from the v6 repository and you now need to install three packs to replace the old version.

    - questions:
        question: >
            Which compiler is not supported in CMSIS v6?
        answers:
            - Arm Compiler v6
            - LLVM 17.x
            - Arm Compiler v5
            - GCC 12.x
        correct_answer: 3                   
        explanation: >
            Arm Compiler v5 is deprecated and not supported in CMSIS v6 anymore.
               
    - questions:
        question: >
            How many packs do you need to install to replace the Keil.ARM_Compiler pack?
        answers:
            - One
            - Two
            - Four
        correct_answer: 2          
        explanation: >
            The Keil.ARM_Compiler pack is replaced by the ARM.CMSIS-View and ARM.CMSIS_Compiler packs.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

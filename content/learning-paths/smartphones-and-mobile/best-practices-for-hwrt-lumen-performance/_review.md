---
review:
    - questions:
        question: >
            How many levels does an acceleration structure have?
        answers:
            - 1
            - 2
            - 4
        correct_answer: 2                    
        explanation: >
            Acceleration structure has 2 levels: TLAS and BLAS.

    - questions:
        question: >
            Can an acceleration structure be updated at run-time?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                    
        explanation: >
            The acceleration structure can be updated at run-time but remember that there is a performance cost.
               
    - questions:
        question: >
            Can developers exclude scene objects from ray tracing in Unreal editor?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1          
        explanation: >
            Developers can exclude objects from ray tracing in Unreal editor. Excluding smaller/unimportant objects from ray tracing can improve ray traversal performance without hurting the final rendering quality.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

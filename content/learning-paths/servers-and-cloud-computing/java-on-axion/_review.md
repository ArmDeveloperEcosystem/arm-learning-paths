---
review:
    - questions:
        question: >
            Which instance type denotes an Axion processor?
        answers:
            - T2A
            - C4A
        correct_answer: 2                
        explanation: >
            C4A denotes an Axion processor. T2A refers to the older Ampere Altra processors.

    - questions:
        question: >
            Which flag is best for long running applications with predictable workloads?
        answers:
            - -XX:InitialCodeCacheSize
            - -XX:-TieredCompilation
            - -XX:ReservedCodeCacheSize
        correct_answer: 2                   
        explanation: >
            Turning off tiered compilation is best for long running applications with predictable workloads.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

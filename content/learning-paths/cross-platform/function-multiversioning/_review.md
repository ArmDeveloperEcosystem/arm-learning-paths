---
review:
    - questions:
        question: >
            What is the main benefit of Function Multiversioning?
        answers:
            - I can reuse my binaries on different targets without sacrificing runtime performance.
            - My application binaries are smaller.
        correct_answer: 1
        explanation: >
            The binaries produced can be reused on different targets, but they might be larger in size.

    - questions:
        question: >
            Can I implement versions of a function in separate translation units?
        answers:
            - Yes, function versions can spread across different translations units.
            - No, all of the functions must be in the same translation unit.
        correct_answer: 1
        explanation: >
            There is no requirement for function versions to be defined in the same translation unit. However, they must all be declared in the translation unit which contains the definition of the default version.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

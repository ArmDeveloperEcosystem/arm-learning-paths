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

    - questions:
        question: >
            Under what circumstances will two targets, one with SVE2 and one with SVE, run the same version of a function?
        answers:
            - The versioned function has versions for SVE2 and default only.
            - The versioned function has versions for SVE2, SVE and default only.
            - The versioned function has versions for SVE and default only.
        correct_answer: 3
        explanation: >
            Answer 3 is the only one where the most specific version for both targets is the same, namely SVE. In answer 1, one target would pick SVE2 and the other default, and in answer two, one would pick SVE2 and the other SVE.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

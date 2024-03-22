---
review:
    - questions:
        question: >
            What are intrinsics?
        answers:
            - A collection of compiler optimization options
            - A set of commands that compile directly to Arm native instructions
            - A set of C++ classes
        correct_answer: 2
        explanation: >
            Neon intrinsics in C# are a collection of functions that the compiler directly translates to Arm native instructions.

    - questions:
        question: >
            What is considered best practice when wanting to improve the compiler’s ability to auto-vectorize your code?
        answers:
            - Favor longer complex loops over small simple loops
            - Favor short, simple, fixed-length loops (preferably multiples of 4 or 8)
            - Avoid inline functions
        correct_answer: 2
        explanation: >
            Programmers should design their code and data to be SIMD friendly and follow best practices (highlighted in this learning path) to help the compiler perform auto-vectorization.

    - questions:
        question: >
            `IsNeonSupported` returns true when Neon intrinsics are supported. Which namespace contains `IsNeonSupported`?
        answers:
            - Unity.Burst.Intrinsics.Arm.Neon
            - UnityEngine
            - UnityEngine.Intrinsics
        correct_answer: 1
        explanation: >
            If `IsNeonSupported` is false, you may wish to fall back to a non-Neon implementation. `IsNeonSupported` is actually evaluated at compile time so it won’t add any overhead to your code.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

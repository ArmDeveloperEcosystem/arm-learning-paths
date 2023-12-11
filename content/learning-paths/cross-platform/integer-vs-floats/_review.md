---
review:
    - questions:
        question: >
            Mixing types (integer, floats) in arithmetic expressions in C:
        answers:
            - Is free, the CPU does automatic conversion on the fly
            - Can imply conversion instructions which can be costly in CPU cycles
        correct_answer: 2
        explanation: >
            Depending on the expression, the compiler might not be able to convert the value to the optimal data type, and conversion might be needed at runtime.
            These conversion instructions have 3-6 CPU cycles latency which can be costly if the calculation is done in a loop.

    - questions:
        question: >
            If you are trying to solve a problem that requires a large range of numbers but is not too demanding on precision, and space is tight which datatype should you choose?
        answers:
            - uint32_t
            - uint16_t
            - float
            - bf16
        correct_answer: 4
        explanation: >
            bf16 is probably the best solution for such a problem, it takes only 16-bits, but has the same range as float (-3.4e+38, 3.4e+38).
               
    - questions:
        question: >
            Type demotion problems are detected by the compiler in C/C++:
        answers:
            - Correct, both C and C++ compilers detect such problems and fail compilation
            - Partially correct, only C reports such problems as warnings.
            - Completely wrong, neither C or C++ compilers care about demotion problems.
            - Partially correct, only C++ detects and reports some demotion problem cases as warnings.
        correct_answer: 4
        explanation: >
            C does not report any error at all, C++ does report warnings when doing bracket initializations of values from a larger datatype to a smaller one. However it ignores assignments.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

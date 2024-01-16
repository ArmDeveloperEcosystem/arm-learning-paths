---
review:
    - questions:
        question: >
            Autovectorization is:
        answers:
            - The automatic generation of 3D vectors so that 3D games run faster.
            - Converting an array of numbers in C to an STL C++ vector object.
            - The process where an algorithm is automatically vectorized by the compiler to use SIMD instructions.
        correct_answer: 3
        explanation: >
            Vectorization is the process that converts a loop to use SIMD instructions and is a manual process. Autovectorization is when the compiler does this conversion automatically by detecting specific patterns in the loop that enable it to use specific SIMD instructions to increase performance.

    - questions:
        question: >
            Can the compiler autovectorize all kinds of loops?
        answers:
            - No, only countable loops.
            - All loops except loops with function calls.
            - Yes, all of them.
            - No, only a few kinds of loops are vectorizable based on specific conditions.
        correct_answer: 4                   
        explanation: >
            There are quite a few requirements so that a loop can be detected as vectorizable by the compiler. In particular, it has to be countable, mostly without branches, no function calls, no data inter-dependency.
               
    - questions:
        question: >
            The purpose of the `SDOT`/`UDOT` instructions on Arm is:
        answers:
            - To evaluate a dot product between 4 x 32-bit float elements in a vector.
            - To change the position of the decimal point ('dot') in a floating-point number
            - To evaluate a sum of products of 4 x 8-bit signed/unsigned integers in each 32-bit element in the input vectors.
        correct_answer: 3
        explanation: >
            For each 32-bit element in the input vectors A[i], B[i], `SDOT`/`UDOT` evaluate the sum of the products between the 4 x 8-bit signed/unsigned integers that comprise the A[i], B[i] elements. The corresponding 32-bit element in the output vector holds the resulting sums. For SVE, `SDOT`/`UDOT` instruction also works on 16-bit signed/unsigned integers.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

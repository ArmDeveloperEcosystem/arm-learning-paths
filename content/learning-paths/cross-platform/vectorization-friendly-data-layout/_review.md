---
review:
    - questions:
        question: >
            Which is the most important factor when considering optimal data layout for SIMD?
        answers:
            - No wasted storage for empty/unused elements
            - Process multiple elements in each iteration, thereby reduce the number of iterations
        correct_answer: 2
        explanation: >
            While not wasting storage in the SIMD vectors is important, what is more important is the reduction of the iterations by processing multiple elements per iteration.

    - questions:
        question: >
            Which data layout is a better fit for SIMD?
        answers:
            - Array of Structs (AoS)
            - Struct of Arrays (SoA)
            - Struct of Structs (SoS)
            - Array of Pointers (AoP)
        correct_answer: 2
        explanation: >
            Struct of Arrays (SoA) is a better because the for loops are more efficient to iterate through the data in the loop  and fewer jump instructions are required.
               
    - questions:
        question: >
            How many elements are unused in a 128-bit SIMD vector when storing 3D positional information (coordinates x,y,z) as 32-bit floats?
        answers:
            - 25%, 1 element is unused
            - 50%, 2 elements are unused
            - 0%, every element is used
        correct_answer: 1      
        explanation: >
            If we store (x, y, z) in a 128-bit SIMD vector, using 32-bit float elements, we would have a representation like `| x | y | z | (unused) |`. This would mean that we would be wasting 25% of the vector's storage. Having said that, Aarch64 does not have an alignment requirement so the lack of aligned data in a packed scenario does not necessarily constitute a performance hit on Arm. That is not the case however with other ISAs.

    - questions:
        question: >
            Similarly to the previous question, what would the percentage be if we used 64-bit floats to store the information in a 256-bit vector?
        answers:
            - 0%, every element is used
            - 50%, 2 elements are unused
            - 25%, 1 x 64-bit element is unused
        correct_answer: 3          
        explanation: >
            Similarly, we have doubled the size of the vector and the element, but we are still having one element unused, so 25% is wasted.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

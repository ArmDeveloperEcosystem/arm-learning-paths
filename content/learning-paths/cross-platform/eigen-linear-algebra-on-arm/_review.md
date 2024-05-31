---
review:
    - questions:
        question: >
            Does Eigen use SIMD code all the time for best performance?
        answers:
            - Yes, always.
            - No, it can be disabled with -DEIGEN_DONT_VECTORIZE.
            - Sometimes, it does runtime detection.
        correct_answer: 2
        explanation: >
            Eigen does compile-time detection of the SIMD engine it will use, but it's possible to disable that with the flag `-DEIGEN_DONT_VECTORIZE` passed to the compiler.

    - questions:
        question: >
            Eigen offers the following types by default:
        answers:
            - Vector and Matrix, Tensor is an unsupported module at the moment.
            - Vector only, Matrix and Tensor are unsupported.
            - Vector, Matrix, and Tensor.
            - Tensor, all the others are subclasses.
        correct_answer: 1
        explanation: >
            Matrix is the generic class, Vector is the 1D special case of the Matrix, and Tensor is currently in the `unsupported` directory of Eigen.
               
    - questions:
        question: >
            Does linear algebra code benefit from large SVE vectors?
        answers:
            - Yes, linear algebra benefits from large vectors.
            - No, it makes no difference.
            - Maybe, it depends on the implementation.
        correct_answer: 1
        explanation: >
            Yes, in general, code that involves calculations with vectors, matrices, and tensors benefits from larger vectors - this is why the A64FX SVE CPU uses 512-bit vectors.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

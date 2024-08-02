---
review:
    - questions:
        question: >
            Are immediate values in SIMD intrinsics handled differently in Rust?
        answers:
            - Yes, they are only passed using generics
            - No, nothing changes as they are still passed via the function arguments
            - Both, one can use the generics version or the original way of passing via the function arguments
        correct_answer: 3
        explanation: >
            While the new syntax tries to use Rust's generics, the one that mimics C prototypes is still supported, to allow easier migration from code bases written in C.
            No decision has been made to obsolete the C syntax.

    - questions:
        question: >
            Rust is safer for SIMD programming because the code is marked safe.
        answers:
            - Correct.
            - Incorrect.
            - Partially correct.
        correct_answer: 3
        explanation: >
            This is partially correct, SIMD code for Rust is marked as `unsafe` so in that sense it is still possible for a security related bug to creep in the code.
            However, the rest of the code still passes through the strict Rust compiler checks.
               
    - questions:
        question: >
            CPU features code generation and feature detection is handled directly in Rust.
        answers:
            - Correct
            - Incorrect
        correct_answer: 1
        explanation: >
            Correct, Rust provides the `#[target_feature(enable = "<extension>")]` which can be used to denote that a particular function requires the needed `<extension>` to be executed. The generated code will use instructions from that `<extension>`. In C there is no common way to do that, though there are some GCC/Clang extensions that might do this. Note that the runtime detection still has to be done manually, using `is_aarch64_feature_detected` macro in the case of Aarch64. In C one would have to check `HWCAPS` directly, but many applications/libraries are doing that in a non-uniform way.

    - questions:
        question: >
            Rust `std::simd` produces code which is as fast as `std::arch`
        answers:
            - Correct
            - Incorrect
            - Sometimes
        correct_answer: 3
        explanation: >
            `std::simd` can be quite powerful and generate optimal code but there are specific instructions on all architectures that do not map well to a portable API. To take advantage of these instructions, you have to use `std::arch` if they have corresponding intrinsics enabled.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

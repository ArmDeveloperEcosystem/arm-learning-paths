---
review:
    - questions:
        question: >
            Where is `restrict` placed in the code?
        answers:
            - In the function declaration
            - As an enum value
            - Between the pointer symbol (*) and the argument name
        correct_answer: 3
        explanation: >
            `restrict` is placed in the arguments list of a function, between the * and the variable name, like this:
            `int func(char *restrict arg)`
    - questions:
        question: >
            What does `restrict` do?
        answers:
            - It increases the performance of the CPU cores, making your program run faster
            - It issues a command to clear the cache, leaving more room for your program
            - It restricts the standard of the C library used to C99
            - It hints the compiler that the memory pointed to by the variable cannot be accessed through any other means apart from this variable, inside the particular function
        correct_answer: 4                   
        explanation: >
            In order for the compiler to better schedule the instructions of a function, it needs to know if there is any
            dependency between the argument variables. If there is none, usually the compiler can group together instructions
            increasing performance and efficiency.
               
    - questions:
        question: >
            Which language supports `restrict`
        answers:
            - Python
            - C and C++
            - C only (after C99)
            - Rust
        correct_answer: 3
        explanation: >
            `restrict` is a C-only keyword, it does nothing on C++.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

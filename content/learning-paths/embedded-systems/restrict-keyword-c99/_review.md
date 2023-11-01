---
review:
- questions:
        question: >
            What does `restrict` do?
        answers:
            - It increases the frequency of the CPU cores, making your program run faster
            - It issues a command to clear the cache, leaving more space for your program
            - It restricts the standard of the C library used to C99
            - It hints to the compiler that the memory pointed to by the parameter cannot be accessed by any other means inside a particular function except using this pointer
        correct_answer: 4                   
        explanation: >
            In order for the compiler to better schedule the instructions of a function, it needs to know if there are any
            dependencies between the parameter variables. If there is no dependency, usually the compiler can group together instructions
            increasing performance and efficiency.
    - questions:
        question: >
            Where is `restrict` placed in the code?
        answers:
            - In the function declaration
            - As an enum value
            - Between the pointer symbol (*) and the parameter name
        correct_answer: 3
        explanation: >
            `restrict` is placed in the arguments list of a function, between the * and the parameter name, like this:
            `int func(char *restrict arg)`   
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
            `restrict` is a C-only keyword, it does not exist on C++ (`__restrict__` does, but it does not have the same function)



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

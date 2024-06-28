---
review:
    - questions:
        question: >
            Which tool can ease the development, configuration, and build of your C++ project on different platforms?
        answers:
            - Autoconf/automake.
            - CMake.
            - Vim.
            - GNU Emacs.
        correct_answer: 2
        explanation: >
            CMake is often used as the configuration and build infrastructure, from small projects to the largest, such as [LLVM](https://www.llvm.org) or [Qt](https://www.qt.io/). Vim and GNU Emacs are powerful text editors. Autoconf and automake are tools that achieve a similar goal across \*nix platforms.

    - questions:
        question: >
            When should you use unit testing ?
        answers:
            - Once the project is finished, to ensure it works.
            - Right from the start so tests can be added during the development phase and ensure it works bottom up.
            - Testing?  My code is always first time right, and I never introduce bugs!
        correct_answer: 2
        explanation: >
            While the first answer is not factually incorrect, the second approach is best as it's much easier to add test along the way as the functionality is developed.

    - questions:
        question: >
            Is there a requirement to rewrite the operators to support Matrices with different data types?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            C++ templates are a powerful feature as they enable generic programming, where code is parameterized by types. This allows to write code once, and let the compiler specialize it for a specific types.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

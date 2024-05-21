---
review:
    - questions:
        question: >
            Which tool can ease the development, configuration and build of your C++ project on different platforms?
        answers:
            - Autoconf / automake
            - CMake
            - Vim
            - GNU Emacs
        correct_answer: 2
        explanation: >
            CMake is often used as the configuration and build infrastructure, from small projects to the largest, like [LLVM](https://www.llvm.org) or [Qt](https://www.qt.io/). Vim and GNU Emacs are very powerful text editors (and more). Autoconf and automake are tools that were achieving a similar goal across \*nix platforms.

    - questions:
        question: >
            When should you use unit testing?
        answers:
            - Once the project is finished, to ensure it works
            - Right from the start so tests can be added along the development and ensure it works bottom up.
            - Testing?  My code is always first time right, and I never introduce bugs!
        correct_answer: 2
        explanation: >
            While the first answer is not fully wrong, it's not that bad if a program has tests, the second approach is the best as it's much easier to add test along the way at the time the functionality is developed.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

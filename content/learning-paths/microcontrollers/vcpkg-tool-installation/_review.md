---
review:
    - questions:
        question: >
            What is vcpkg?
        answers:
            - A commercial package for venture capitalists.
            - A package manager for acquiring and managing libraries.
        correct_answer: 2
        explanation: >
            vcpkg is a free C/C++ package manager for acquiring and managing libraries that runs on all platforms, build systems, and work flows.

    - questions:
        question: >
            When do you need to initialize the vcpkg environment?
        answers:
            - Once, at installation.
            - Once, before running a vcpkg command.
            - Every time you start a fresh Terminal session.
        correct_answer: 3
        explanation: >
            You need to initiliaze vcpkg every time you start a new terminal session.
               
    - questions:
        question: >
            What's the purpose of the vcpkg-configuration.json file?
        answers:
            - It is used to connect your machine to the Internet.
            - It is used to maintain a reproducible installation.
            - It is used to reference other vcpkg projects.
        correct_answer: 2          
        explanation: >
            The vcpkg-configuration.json file forms part of a project's manifest that enables reproducible installations on various machines.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

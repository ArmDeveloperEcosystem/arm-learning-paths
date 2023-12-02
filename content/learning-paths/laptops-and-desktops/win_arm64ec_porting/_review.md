---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add additional context if desired


review:
    - questions:
        question: >
            Is it possible to import C/C++ library to a Python application
        answers:
            - "True"
            - "False"            
        correct_answer: 1
        explanation: >
            Yes, you can import C/C++ DLLs to a Python application using ctypes.

    - questions:
        question: >
            How do you port C/C++ code to ARM64 using ARM64EC and MSBuild
        answers:
            - "Using a command line tool port-to-arm64"
            - "Using a command line tool port-to-arm64-msbuild"
            - "By targeting the ARM64EC build configuration"
        correct_answer: 3                     
        explanation: >
            For the MSBuild projects you use ARM64EC build configuration to compile the DLL to ARM64EC

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

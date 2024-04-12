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
            Why do you need to configure the project dependencies?
        answers:
            - "To ensure the proper build order"
            - "To configure the dependency injection"
        correct_answer: 1
        explanation: >
            You use the project dependencies to ensure the proper build order. For example, the DLL has to be compiled before the main application.

    - questions:
        question: >
            What is the `__declspec` keyword for?
        answers:
            - "__declspec can be used to control symbol visibility (exporting and importing functions or classes in DLLs)"
            - "__declspec specifies the platform"
            - "__declspec specifies the build configuration"
        correct_answer: 1                
        explanation: >
            You typically use `__declspec` along with `dllexport` and `dllimport` to control symbol visibility

    - questions:
        question: >
            If VECTOROPERATIONS_EXPORTS is defined, the VECTOROPERATIONS_API is defined as `__declspec(dllexport)`?
        Answers:
            - True
            - False
        correct_answer: 1
        explanation: >
            `__declspec(dllexport)` marks the specified functions or objects to be exported from the DLL. This is typically defined in the project settings or source code of the DLL being compiled.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

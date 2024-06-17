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
            Arm embedded applications can be built with the Rust compiler rustc.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Though not installed by default, cross-compilation support for Arm architectures can easily be added.

    - questions:
        question: >
            Does Arm Debugger officially support Rust applications?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2
        explanation: >
            At the time of writing (up to the 2024.0 release of Arm Development Studio), Rust applications are not officially supported.
            However as the DWARF5 debug format is supported, the applications can be loaded and have reasonable debug visibility.
            
    - questions:
        question: >
            Variables in Rust are immutable by default.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Rust variables are immutable by default, meaning that once they are set to a value, they cannot be changed.
            Use the "mut" keyword to define a variable as mutable.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

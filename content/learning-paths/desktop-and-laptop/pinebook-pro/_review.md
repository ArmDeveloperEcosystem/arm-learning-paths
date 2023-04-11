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
            Is Arch Linux a rolling-release OS or a long term support OS?
        answers:
            - "rolling release OS"
            - "long term support OS"
        correct_answer: 1               
        explanation: >
            Arch Linux keeps up to date always using the latest available version of the kernel

    - questions:
        question: >
            Can i3 be installed on a fresh Arch Linux ARM install without any additional software packages?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                     
        explanation: >
            For i3 to work on a fresh Arch Linux install it requires display packages, a dynamic menu package, and a terminal emulator at a minimum
               
    - questions:
        question: >
            Neovim is the only editor that is a good choice for the Pinebook Pro
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            Neovim is only one choice out of many that can be used to develop on the Pinebook Pro, and it really comes down to personal preference

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

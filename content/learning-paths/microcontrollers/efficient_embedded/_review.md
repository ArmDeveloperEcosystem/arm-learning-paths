---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 1)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add additional context if desired


review:
    - questions:
        question: >
            When a function calls a subroutine, where is the return address stored?
        answers:
            - "Program Counter"
            - "Link Register"
            - "Stack Pointer"
        correct_answer: 2
        explanation: >
            When a function calls a subroutine, it places the return address in the link register lr.

    - questions:
        question: >
            What keyword can be used to incorporate inline assembly code?
        answers:
            - "__asm"
            - "__arm"
            - "__assembly"
        correct_answer: 1
        explanation: >
            The __asm keyword can incorporate inline assembly code into a function using the GNU inline assembly syntax. 
               
    - questions:
        question: >
            Which registers should be preserved by a subroutine?
        answers:
            - "r1-r3"
            - "r2-r6"
            - "r4-r11"
        correct_answer: 3
        explanation: >
            Registers r4 through r11 must be preserved by a subroutine. r0-r3, and r12, are corruptible by a subroutine, with parameters being passed in r0-r3.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

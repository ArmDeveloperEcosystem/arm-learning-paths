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
            Which compiler option enables debugging symbols?
        answers:
            - "-d"
            - "-g"
        correct_answer: 2                     
        explanation: >
            The -g option produces debugging information for debugging tools like GDB.
            
    - questions:
        question: >
            What type of bugs a parallel debugger can help with?
        answers:
            - "Deadlocks"
            - "Out-of-bounds memory accesses"
            - "Race conditions"
            - "All of the above"
        correct_answer: 4                    
        explanation: >
            Deadlocks and race conditions are specific to parallel behaviour but parallel debuggers can help with memory issues too! 
    - questions:
        question: >
            How can you check SIMD is used to enable performance and which loops were vectorized?
        answers:
            - "Using -fopt-info-vec with GNU Compilers and -Rpass=vector with Arm Compiler for Linux"
            - "Using -fvectorization with GNU Compilers and -Rvectorization with Arm Compiler for Linux"
        correct_answer: 1                   
        explanation: >
            The -fopt-info-vec with GNU Compilers and -Rpass=vector with Arm Compiler for Linux will ask the compiler to report on vectorized loops. You can ask the compiler to specifically report which loop failed to vectorize with -fopt-info-vec-missed and -Rpass-missed=vector.       

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

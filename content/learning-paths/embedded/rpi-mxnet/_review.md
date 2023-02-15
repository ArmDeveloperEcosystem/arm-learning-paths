---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add aditional context if desired


review:
    - questions:
        question: >
            Which command is used to change the root directory to make the file system appear to be another Linux installation?
        answers:
            - "losetup"
            - "chroot"
            - "resizefs"
            - "mount"
        correct_answer: 2                 
        explanation: >
            chroot changes the root directory to make another Linux installation magically appear

    - questions:
        question: >
            Arm servers can be used to reduce compile time for application which take a long time to build
        answers:
            - "True"
            - "False"
        correct_answer: 1                  
        explanation: >
            Using a faster computer with more memory and processors is a good way to reduce compile time
               

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

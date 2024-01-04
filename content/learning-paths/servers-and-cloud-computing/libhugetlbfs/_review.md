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
            To which build stage does information about libhugetlbfs need to be added?
        answers:
            - preprocessing
            - compilation
            - assembly
            - linking
        correct_answer: 4                     
        explanation: >
            libhugetlbfs is a library which is added during the linking stage.

    - questions:
        question: >
            True or False: libhugetlbfs can only be used on read-only sections of code.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            The code section is a typical section to be placed in hugepages, but other sections like data can also be placed in hugepages.
               
    - questions:
        question: >
            After enabling libhugetlbfs on MySQL, which perf event will be decrease dramatically?
        answers:
            - l1d_tlb_refill
            - l1i_tlb_refill
            - l2d_tlb_refill
        correct_answer: 2
        explanation: >
            After enabling libhugetlbfs on MySQL, l1i_tlb_refill decreases dramatically from 490,265,467 to 70,741,621.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

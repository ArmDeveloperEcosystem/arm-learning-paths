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
            How do you select the number of huge pages that should be used?
        answers:
            - "Set to the size of the redo log file"
            - "Divide the buffer pool size by the huge page size"
            - "Set to the buffer pool size"
        correct_answer: 2                     
        explanation: >
            You should divide the buffer pool size by the huge page size because you want as much huge page space as there is buffer pool space. 

    - questions:
        question: >
            What is the recommended size for the MySQL buffer pool?
        answers:
            - "Up to 30-40% of system memory"
            - "Up to 10-20% of system memory"
            - "Up to 70-80% of system memory"
        correct_answer: 3
        explanation: >
            The MySQL documentation suggests up to 80% of system memory. Depending on the use case, it's also possible that a much smaller percentage performs just as well as 80%. Buffer pool size is also automatically set to 75% of system memory if you use the innodb_dedicated_server option (See MySQL docs).
               
    - questions:
        question: >
            Why might it be a good idea to increase how often a mutex lock is checked before the running thread yields?
        answers:
            - "Increasing mutex lock checks before a yield speeds up disk access"
            - "Increasing mutex lock checks before a yield reduces context switching, which is expensive"
            - "Increasing mutex lock checks before a yield speeds up buffer pool reads"
        correct_answer: 2
        explanation: >
            Reducing context switching helps performance. Spending a bit longer in checking locks before yielding by increasing innodb_sync_spin_loops usually provides performance gains.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

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
            When tuning a thread count configuration parameter like innodb_read_io_threads or innodb_write_io_threads. What can often be a good starting value?
        answers:
            - "One"
            - "Total number of CPUs on the system"
            - "Half the number of CPUs on the system"
        correct_answer: 2                     
        explanation: >
            The total number of CPUs is a good starting point because it can ensure you are using all compute resources on the system. 

    - questions:
        question: >
            What is the recommended size for the MySQL buffer pool?
        answers:
            - "Up to 40% of system memory"
            - "Up to 20% of system memory"
            - "Up to 80% of system memory"
        correct_answer: 3
        explanation: >
            The MySQL documentation suggests up to 80% of system memory. Depending on the use case, it's also possible that a much smaller percentage performs just as well as 80%.
               
    - questions:
        question: >
            Why might it be a good idea to increase how often a mutex lock is checked before the running thread yields?
        answers:
            - "Checking locks more often speeds up disk access"
            - "Checking locks more often reduces context switching, which is expensive"
            - "Checking locks more often speeds up buffer pool reads"
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

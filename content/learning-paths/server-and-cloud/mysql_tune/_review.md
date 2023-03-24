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
            When tuning a thread count configuration parameter like innodb_read_io_threads or innodb_write_io_threads. What can often be a good starting value?
        answers:
            - "One"
            - "Total number of CPUs on the system"
            - "Half the number of CPUs on the system"
        correct_answer: 2                     
        explanation: >
            The total number of CPUs is a good starting point because it can ensure we are using all compute resources on the system. That said, it's important to understand the parameter and to also try some experimentation with the parameter. It is also possible that a much smaller number than that total number of CPUs on the system is optimal.

    - questions:
        question: >
            What is the recommended size for the MySQL buffer pool?
        answers:
            - "Up to 40% of system memory"
            - "Up to 20% of system memory"
            - "Up to 80% of system memory"
        correct_answer: 3
        explanation: >
            The MySQL documentation suggests up to 80% of system memory. Our own testing also agrees with this suggestion. That said, depending on the use case, it's also possible that a much smaller percentage performs just as well as 80%.
               
    - questions:
        question: >
            Why might it be a good idea to increase how often a mutex lock is checked before the running thread yields?
        answers:
            - "Checking locks more often speeds up disk access"
            - "Checking locks more often reduces context switching, which is expensive"
            - "Checking locks more often speeds up buffer pool reads"
        correct_answer: 2
        explanation: >
            In our testing, we found that reducing context switching helps performance. Hence, spending a bit longer in checking locks before yielding by increasing innodb_sync_spin_loops gave us performance gains. Note, we suggest that readers try experimenting with this parameter to determine if it will benefit their use case.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

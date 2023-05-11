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
            When tuning a worker process or thread count configuration parameter. What can often be a good starting value?
        answers:
            - "One"
            - "Total number of CPUs on the system"
            - "Half the number of CPUs on the system"
        correct_answer: 2                     
        explanation: >
            The total number of CPUs is a good starting point because it can ensure you are using all compute resources on the system. 

    - questions:
        question: >
            What is the recommended size for the PostgreSQL shared buffer?
        answers:
            - "25%-40%"
            - "10%-20%"
            - "60%-80%"
        correct_answer: 1
        explanation: >
            The PostgreSQL documentation suggests 25%-40%.
               
    - questions:
        question: >
            Enabling huge pages helps performance by increasing shared buffer hit rate.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            This is a bit of a trick question. Huge pages will not increase or decrease the shared buffer hit rate. It does reduce how often physical memory will need to be unmapped/mapped to virtual memory pages.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

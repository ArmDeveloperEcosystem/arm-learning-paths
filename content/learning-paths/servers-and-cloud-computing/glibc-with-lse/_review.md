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
            Can you use LSE on Non-Arm servers?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                    
        explanation: >
            LSE is a feature specific to ARM architecture.

    - questions:
        question: >
            All ARM architectures support LSE.
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                  
        explanation: >
            LSE is supported only on ARM architectures of ARMv8-A and above.
               
    - questions:
        question: >
            LSE can improve all applications performance.
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                    
        explanation: >
            Only the performance of multi-threaded applications that heavily rely on atomic operations and synchronization primitives can be improved potentially.

    - questions:
        question: >
            YCSB can only support MongoDB.
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                    
        explanation: >
            YCSB supports a variety of popular data-serving systems, including Apache Cassandra, MongoDB, Redis, HBase, Amazon DynamoDB, and more. It provides a set of workload scenarios that can be customized to simulate specific application patterns and data access patterns.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 8                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

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
            Memcached cannot cache large objects.
        answers:
            - "True"
            - "False"
        correct_answer: 1                   
        explanation: >
            Memorystore in Memcached has the minimum value of 512 KiB, the maximum value of 128 MiB, and the default value is 1 MiB.
    - questions:
        question: >
            Memcached can retain the stored information even when item from the cache is deleted.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Memcached cannot retain the stored information when item from the cache is deleted.
    - questions:
        question: >
            It is possible to share a single instance of Memcache between multiple projects.
        answers:
            - "True"
            - "False"
        correct_answer: 1
        explanation: >
            Yes, it is possible to share a single instance of Memcache between multiple projects because Memcache is a memory store space and it can be run on one or more servers. 
# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

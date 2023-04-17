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
            Nginx can only be installed by building it from source.
        answers:
            - "True"
            - "False"
        correct_answer: 2                    
        explanation: >
            Nginx can be installed from the package manager or built from source.

    - questions:
        question: >
            What are some of the uses of Nginx?
        answers:
            - "Load balancer"
            - "Reverse proxy server"
            - "Web server"
            - "All of the above"
        correct_answer: 4                  
        explanation: >
            Nginx can handle all of these functions.
               
    - questions:
        question: >
            Nginx can handle a large number of connections.
        answers:
            - "True"
            - "False"
        correct_answer: 1                    
        explanation: >
            Nginx can often serve 10x more requests than other web servers.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

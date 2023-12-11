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
            Can MySQL server run as root?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                     
        explanation: >
            MySQL server can't be run as root, you will need to create a new user to run MySQL server.

    - questions:
        question: >
            After starting mysqld, should you wait few seconds before creating database?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1
        explanation: >
            You'll need to wait few seconds so that mysql.sock is created.
               
    - questions:
        question: >
            Which directories in MySQL server installation path need to be specified when building sysbench?
        answers:
            - "include"
            - "lib"
            - "both of the above"
        correct_answer: 3
        explanation: >
            In order to run Sysbench against MySQL server, both the include and the lib directories under the MySQL server installation need to be specified when building Sysbench.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

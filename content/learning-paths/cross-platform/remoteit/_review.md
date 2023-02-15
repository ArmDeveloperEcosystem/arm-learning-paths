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
            Which connection type offers the highest performance?
        answers:
            - "Proxy connection"
            - "Peer to peer connection"
            - "Encrypted connection"
        correct_answer: 2
        explanation: >
            Peer to peer are persistent and offer the highest performance. 

    - questions:
        question: >
            Remote.it provides simple, secure connectors between computers, as long as both computers run the same operating system.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Remote.it runs on a variety of operating systems and Arm hardware. Any operating systems supported by remote.it can be used and the initiator and target devices do not need to have the same operating system.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

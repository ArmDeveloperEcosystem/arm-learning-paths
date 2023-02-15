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
            In the combined mode, Clair creates three different OS processes for all three modes.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            In combined deployment, the Clair processes run in single OS process. Whereas in distributed deployment, each Clair process runs in its own OS processes.

    - questions:
        question: >
            Clairctl will always look for Clair at port 6060.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            By default, clairctl will look for Clair at localhost:6060. We can configure it to another host and port by using clairctl's "--host" flag.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

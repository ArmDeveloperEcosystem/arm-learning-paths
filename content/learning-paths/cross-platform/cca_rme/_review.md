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
            Arm Confidential Compute Architecture (CCA) is available on all Arm devices.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            CCA requires the Realm Management Extension (RME) of Armv9-A architecture, as well as support within the software stack running on the device.
    - questions:
        question: >
            The Secure Monitor runs in which world?
        answers:
            - "Normal"
            - "Secure"
            - "Root"
            - "Realm"
        correct_answer: 3
        explanation: >
            The Secure Monitor runs in Root world. The Hypervisor runs in Normal world.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

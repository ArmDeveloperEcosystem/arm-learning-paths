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
            Raspberry Pi 4 hardware is similar, but slightly faster than an Arm server from a cloud service provider
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            The Raspberry Pi is similar, but slower than an Arm server


    - questions:
        question: >
            The Raspberry Pi supports peripherals such as USB and Bluetooth, which are also present on an Arm server
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Arm servers do not have peripherals such as USB and Bluetooth, but in many cases can run the same software as a Raspberry Pi 

    - questions:
        question: >
            Raspberry Pi OS is the only Linux distribution which can be run on a Raspberry Pi 4
        answers:
            - "True"
            - "False"
        correct_answer: 2                     
        explanation: >
            Other operating systems, such as Ubuntu, can be installed on the Raspberry Pi. 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

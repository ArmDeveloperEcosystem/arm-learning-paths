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
            What is the minimum requirement to start debugging in Keil MDK (µVision)?
        answers:
            - "A professional license"
            - "A sophisticated debug probe"
            - "Arm Fixed Virtual Platforms (FVPs)"
            - "A browser"
        correct_answer: 3
        explanation: >
            µVision supports debugging with free FVPs. This does not require any hardware or paid-for license.

    - questions:
        question: >
            What hardware is required for power-aware debugging?
        answers:
            - "CMSIS-DAP"
            - "ULINKpro"
            - "ULINKplus"
        correct_answer: 3
        explanation: >
            ULINKplus is the power-aware debug adapter from Arm for Cortex-M based microconotrollers.
               
    - questions:
        question: >
            Event Recorder requires...?
        answers:
            - "...an ETM to be present."
            - "...only a small amount of memory."
            - "...a 20-pin debug connector on the board."
        correct_answer: 2
        explanation: >
            Event Recorder is independent of specific debug interfaces and only uses a small amount of RAM for storing debug data.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

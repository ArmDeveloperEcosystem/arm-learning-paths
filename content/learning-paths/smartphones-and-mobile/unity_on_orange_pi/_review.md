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
            Any SD card imaging software can be used to load the Droid OS image onto a microSD card.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            You will get errors if you don't use SDDiskTool_v1.72

    - questions:
        question: >
            In Unity, what platform needs to be selected when you build your game?
        answers:
            - "iOS"
            - "WebGL"
            - "Android"
            - "Windows, Mac, Linux"
        correct_answer: 3
        explanation: >
            Droid OS runs Android SDKs

    - questions:
        question: >
            You run the game on the Orange Pi by clicking on the APK file.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Clicking the APK file is how you install the game. To run it, you find the game in your app drawer.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

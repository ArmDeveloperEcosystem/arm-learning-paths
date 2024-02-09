---
review:
    - questions:
        question: >
            What makes embedded programming different from application programming?
        answers:
            - Embedded software requires the use of assembly language
            - Embedded software doesn't use language constructs like classes and functions
            - Embedded software typically runs on resource-limited hardware
        correct_answer: 3                    
        explanation: >
            Fundamentally, there is no difference between embedded programming and application programming. The biggest difference is the hardware resources available to your program.

    - questions:
        question: >
            You can only write Arduino code for Arduino brand devices.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            The Arduino core software works with board support packages that cover a number of boards, not all of these are Arduino branded. For example, the Raspberry Pi branded Pico board is not from Arduino.
               
    - questions:
        question: >
            Which function of your sketch does Arduino core call when your board first starts up?
        answers:
            - main()
            - setup()
            - loop()
            - delay()
        correct_answer: 2          
        explanation: >
            Arduino sketches don't have a main() function, instead Arduino core calls the setup() function at start.

    - questions:
        question: >
            Which function of your sketch does Arduino core call continuously after it has started?
        answers:
            - main()
            - setup()
            - loop()
            - delay()
        correct_answer: 3          
        explanation: >
            After startup, Arduino core calls loop() continuously.

    - questions:
        question: >
            What happens when your loop() function completes?
        answers:
            - Your setup() function will be called again
            - Your loop() function will be called again
            - Your Sketch will stop running
            - Your board will turn off
        correct_answer: 2          
        explanation: >
            Arduino core continuously calls loop() until you call exit() or the board loses power.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

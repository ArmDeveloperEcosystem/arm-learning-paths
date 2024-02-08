---
review:
    - questions:
        question: >
            What make embedded programming different from application programming?
        answers:
            - Embedded programming requires using assembly language
            - Embedded programming doesn't use language contructs like classes and functions
            - Embedded programming just runs on more resource-limited hardware
        correct_answer: 3                    
        explanation: >
            Fundamentally there is no difference between embedded programming and application programming. The biggest difference is in what resources are available to your program on your target hardware.

    - questions:
        question: >
            You can only write Arduino code for Arduino brand devices.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            The Arduino Core software works with board packages that cover a number of boards, not all of this are Arduino branded. For example, this Learning Path uses the Raspberry Pi branded Pico board.
               
    - questions:
        question: >
            Which function of your Sketch does the Arduino Core software call when your board first starts up?
        answers:
            - main()
            - setup()
            - loop()
            - delay()
        correct_answer: 2          
        explanation: >
            Arduino Sketches don't have a main() function, instead the Arduino Core software calls the setup() function at start.

    - questions:
        question: >
            Which function of your Sketch does the Arduino Core software call continuously after it has started?
        answers:
            - main()
            - setup()
            - loop()
            - delay()
        correct_answer: 3          
        explanation: >
            Arduino Sketches don't have a main() function, instead the Arduino Core software calls the setup() function at start.

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
            Arduino Core will continuously call the loop() function until you make a call to exit() or the board loses power.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

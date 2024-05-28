---
review:
    - questions:
        question: >
            True or False? There is only one voice option available using OpenAI's text-to-speech.
        answers:
            - "True"
            - "False"
        correct_answer: 2                
        explanation: >
            OpenAI offers a number of different voices.

    - questions:
        question: >
            Which ChatGPT model does the example implementation use?
        answers:
            - gpt-4-turbo-preview
            - gpt-3.5-turbo
            - gpt-4-vision-preview
            - dall-e-3
        correct_answer: 1                   
        explanation: >
            The example uses gpt-4-turbo-preview, though it can be swapped out fairly easily for those who have specific needs.
               
    - questions:
        question: >
            What is the library used to listen for the wake word?
        answers:
            - SpeechRecognition
            - PyAudio
            - pvporcupine
            - python-dotenv
        correct_answer: 3          
        explanation: >
            pvporcupine is Picovoice's Porcupine library, meant to provide an offline wake word solution.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---

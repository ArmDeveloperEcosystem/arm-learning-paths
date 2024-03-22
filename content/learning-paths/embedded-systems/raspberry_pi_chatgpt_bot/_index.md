---
title: Create a ChatGPT voice bot on a Raspberry Pi

minutes_to_complete: 60

who_is_this_for: This is an introductory project for developers interested in integrating a Chatbot (namely ChatGPT) into Raspberry Pi projects.

learning_objectives:
    - Run a bot on a Raspberry Pi that will listen to you and respond to what you say
    - Learn how to listen for a keyword and wake a program when the keyword is heard
    - Convert speech from the microphone to text using Google Speech Recognition
    - Send text created from speech to ChatGPT's gpt-4-turbo-preview model via API and receive a text reply
    - Convert the text reply to speech using ChatGPT's text-to-speech model via API 
    - Play the received speech file 

prerequisites:
    - A Raspberry Pi 4 or 5 (earlier models may also work)
    - A microSD card with at least 16GB of storage
    - A Linux compatible USB microphone and USB speakers or a USB audio device with a microphone and speakers

author_primary: Gabriel Peterson

### Tags
skilllevels: Introductory

subjects: ML

armips:
    - Cortex-A

operatingsystems:
    - Linux

tools_software_languages:
    - ChatGPT
    - Porcupine
    - Python


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

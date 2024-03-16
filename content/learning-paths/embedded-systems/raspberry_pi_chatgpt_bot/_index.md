---
title: Create a ChatGPT voice bot on a Raspberry Pi

minutes_to_complete: 60

who_is_this_for: This is an introductory project for developers interested in integrating ChatGPT into Raspberry Pi projects

learning_objectives:
    - You will create a bot running on a Raspberry Pi that will listen to what you say, and then speak back to you
    - Learn how to listen using a mic and wake the program using a keyword with the Porcupine library
    - Convert speech picked up from the microphone to text using Google Speech Recognition
    - Send the text created from speech to ChatGPT's gpt-4-turbo-preview model via API and receive a text reply
    - Convert the text reply to speech using ChatGPT's text-to-speech model via API 
    - Play the received speech file on speakers

prerequisites:
    - A Raspberry Pi 5 (a 4 or 3 will probably work fine, but I haven't tested this so your results may vary)
    - A microSD card with at least 16GB of storage (per Raspberry Pi's recommendation)
    - Either a Linux compatible USB microphone and USB speakers OR
    - A Linux compatible USB audio device with a microphone and speakers plugged in

author_primary: Gabriel Peterson

### Tags
skilllevels: Introductory

subjects: AI

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

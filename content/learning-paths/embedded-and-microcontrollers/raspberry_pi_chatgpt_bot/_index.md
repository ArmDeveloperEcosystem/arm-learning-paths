---
title: Create a ChatGPT voice bot on a Raspberry Pi

description: Learn how to build a voice-controlled bot on a Raspberry Pi that listens for a wake word, converts speech to text using Google Speech Recognition, sends requests to ChatGPT's API, and plays audio responses.

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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: ed2034f5c95c4148fca355f6d545219c320f2e73267a0725934c792ebc4c0c59
  summary: >-
    Learn how to build a voice-controlled bot on a Raspberry Pi that listens for a wake word,
    converts speech to text using Google Speech Recognition, sends requests to ChatGPT's API,
    and plays audio responses. It is designed for This is an introductory project for developers
    interested in integrating a Chatbot (namely ChatGPT) into Raspberry Pi projects. By the end,
    you will be able to run a bot on a Raspberry Pi that will listen to you and respond to what
    you say, learn how to listen for a keyword and wake a program when the keyword is heard, and
    convert speech from the microphone to text using Google Speech Recognition. It focuses on
    tools and technologies such as ChatGPT, Porcupine, and Python, Linux environments, and Arm
    platforms including Cortex-A. The main steps cover Initial setup, Configure and test audio,
    Create the Python application, and Run and test the bot.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will run a bot on a Raspberry Pi that will listen to you and respond to what you say,
      learn how to listen for a keyword and wake a program when the keyword is heard, and convert
      speech from the microphone to text using Google Speech Recognition. Learn how to build a
      voice-controlled bot on a Raspberry Pi that listens for a wake word, converts speech to
      text using Google Speech Recognition, sends requests to ChatGPT's API, and plays audio responses.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory project for developers interested in integrating a Chatbot (namely
      ChatGPT) into Raspberry Pi projects.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A Raspberry Pi 4 or 5 (earlier models
      may also work); A microSD card with at least 16GB of storage; A Linux compatible USB microphone
      and USB speakers or a USB audio device with a microphone and speakers.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including ChatGPT, Porcupine, and Python, Linux environments,
      and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Initial setup, Configure and test audio, Create the
      Python application, and Run and test the bot.
# END generated_summary_faq

author: Gabriel Peterson

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


further_reading:
    - resource:
        title: OpenAI Documentation
        link: https://github.com/dusty-nv/jetson-inference
        type: documentation
    - resource:
        title: Picovoice's Porcupine Documentation
        link: https://picovoice.ai/docs/porcupine/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


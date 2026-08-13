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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:16:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0f9a4995777d0a7b7acf2cda2fec211ac3c4a99c2ace7334a7eba9e7a702cb5e
  summary_generated_at: '2026-08-12T20:16:07Z'
  summary_source_hash: 0f9a4995777d0a7b7acf2cda2fec211ac3c4a99c2ace7334a7eba9e7a702cb5e
  faq_generated_at: '2026-08-12T20:16:07Z'
  faq_source_hash: 0f9a4995777d0a7b7acf2cda2fec211ac3c4a99c2ace7334a7eba9e7a702cb5e
  summary: >-
    You'll build a voice-driven assistant on Raspberry Pi. First, you'll install 64-bit Raspberry Pi OS,
    configure USB audio, and create a Python virtual environment. Then, you'll run a script that detects
    the “computer” wake word, transcribes speech, sends text to ChatGPT, and plays the reply. You'll
    validate audio recording and output before running the assistant continuously.
  faqs:
  - question: How do I know the microphone recording worked?
    answer: >-
      After recording by running `arecord -d 5 test.wav`, a file named `test.wav` should appear in your current
      directory. Its size should be non-zero.
  - question: Which wake word should I use, and how do I know the bot is listening?
    answer: >-
      Say "computer", pause for about a second, then ask your question. The terminal displays
      output indicating it's waiting for the keyword before it detects the wake word.
  - question: How do I re-activate the Python virtual environment in a new terminal?
    answer: >-
      Run `cd $HOME/assistant` followed by `source env/bin/activate`. Then run `python main.py` to start
      the assistant.
  - question: How do I find the card and device numbers for my USB audio hardware?
    answer: >-
      Run `arecord -l` to list recording devices and `aplay -l` to list playback devices. Use
      the card and device numbers in commands such as `arecord -D plughw:3,0 -d 5 test.wav` and
      `aplay -D plughw:2,0 test.wav`, replacing the values with your hardware's numbers.
  - question: How do I stop the application when I am done testing?
    answer: >-
      Press **Ctrl+C** in the terminal where `python main.py` is running. The process exits and the
      prompt returns.
# END generated_summary_faq

author: Gabriel Peterson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

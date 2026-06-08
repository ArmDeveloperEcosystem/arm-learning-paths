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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:38:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ed2034f5c95c4148fca355f6d545219c320f2e73267a0725934c792ebc4c0c59
  summary_generated_at: '2026-06-01T21:50:55Z'
  summary_source_hash: ed2034f5c95c4148fca355f6d545219c320f2e73267a0725934c792ebc4c0c59
  faq_generated_at: '2026-06-02T22:38:37Z'
  faq_source_hash: ed2034f5c95c4148fca355f6d545219c320f2e73267a0725934c792ebc4c0c59
  summary: >-
    This introductory Learning Path guides you through building and running a voice-controlled
    ChatGPT bot on a Raspberry Pi 4 or 5 using Raspberry Pi OS (64-bit, Linux). You will install
    the OS with Raspberry Pi Imager, configure and test audio I/O, and create a Python application
    that listens for a wake word with Porcupine, converts speech to text using Google Speech Recognition,
    sends text to ChatGPT’s gpt-4-turbo-preview model via API, generates speech via ChatGPT’s
    text-to-speech API, and plays the audio reply. You will work in a Python virtual environment
    and use packages including pyaudio, SpeechRecognition, pydub, openai, python-dotenv, and pvporcupine.
    Prerequisites include a Raspberry Pi, a 16GB microSD card, and a USB microphone and speakers.
  faqs:
  - question: What Raspberry Pi hardware and OS do I need before starting?
    answer: >-
      Use a Raspberry Pi 4 or 5 (earlier models may also work), a microSD card with at least 16GB,
      and Raspberry Pi OS (64-bit) installed via Raspberry Pi Imager. You also need a Linux compatible
      USB microphone and USB speakers or a combined USB audio device.
  - question: How do I verify my microphone and speakers are set up correctly?
    answer: >-
      Plug in the devices, then right-click the speaker icon on the desktop to select your speakers.
      In a terminal, run arecord -d 5 test.wav to create a short recording; if the file is not
      created or contains no audio, adjust audio settings manually and retry.
  - question: Which Python version and packages does the application use?
    answer: >-
      Raspberry Pi OS includes Python 3.11.2. Create a virtual environment and install pyaudio,
      SpeechRecognition, pydub, openai, python-dotenv, and pvporcupine; you can optionally run
      pip freeze to capture versions for troubleshooting.
  - question: How do I run and stop the bot?
    answer: >-
      Activate your virtual environment, then run python main.py from the project directory. The
      application runs indefinitely until you press Ctrl+C to stop it.
  - question: What behavior should I expect when I say the wake word?
    answer: >-
      Say “computer,” pause briefly, then ask a question. After detection, the app converts your
      speech to text, sends it to ChatGPT’s gpt-4-turbo-preview model, converts the reply to speech
      using ChatGPT’s text-to-speech model, and plays the audio response.
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


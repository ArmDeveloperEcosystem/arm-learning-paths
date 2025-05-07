---
title: Overview
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Voice assistant application workflow

The voice assistant application implements a full voice interaction pipeline on Android, enabling real-time, conversational interactions.



![example image alt-text#center](overview.png "The voice interaction pipeline.")

It generates intelligent responses using:
1. **Speech-to-Text (STT)** to transform the user's audio input into text.
2. A **Large Language Model (LLM)** to generate a response in text form.
3. Android **Text-to-Speech (TTS)** API to produce a spoken reply.


The following sections describe how each component works in the application.

## Speech-to-Text 

Speech-to-Text (STT), also known as Automatic Speech Recognition (ASR), converts spoken language into written text.

This process includes the following stages:
- The device's microphone captures spoken language as an audio waveform.
- The audio is segmented into short time frames.
- Features are extracted from each frame.
- A neural network analyzes these features to predict the most likely transcription based on grammar and context.
- The recognized text is passed to the next stage of the pipeline.

## Large Language Model  

Large Language Models (LLMs) enable natural language understanding and, in this application, are used for question-answering.

The text transcription from the previous part of the pipeline is used as input to the neural model. At initialization, the app sets a predefined persona that influences the tone, style, and character of the responses. By default, the LLM runs asynchronously, streaming tokens as they are generated. The UI updates in real time with each token, which is also passed to the final pipeline stage.

## Text-to-Speech 

This part of the application pipeline uses the Android Text-to-Speech API along with additional logic to produce smooth, natural speech.

In synchronous mode, speech playback begins only after the full LLM response is received. By default, the application operates in asynchronous mode, where speech synthesis starts as soon as a full or partial sentence is ready. Remaining tokens are buffered and processed by the Android Text-to-Speech engine to ensure uninterrupted playback.

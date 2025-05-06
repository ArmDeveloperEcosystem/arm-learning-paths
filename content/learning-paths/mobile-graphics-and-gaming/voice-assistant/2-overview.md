---
title: Overview
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The Voice Assistant application showcases a complete voice interaction pipeline running on Android.

It generates intelligent responses using:
1. Speech-to-Text (STT) to transform the user's audio input into text.
2. A Large Language Model (LLM) to generate a response in text form.
3. Android Text-to-Speech (TTS) API to produce a spoken reply.

![example image alt-text#center](overview.png "Figure 1: Overview")

Each of these three steps corresponds to a specific component in the Voice Assistant application. You can find out more about these in the descriptions below.

## Speech-to-Text component

Speech-to-Text, also known as Automatic Speech Recognition (ASR), converts spoken language into written text.

This process includes the following stages:
- The device's microphone captures spoken language as an audio waveform.
- The audio waveform is broken into short time frames, and acoustic features are extracted.
- A neural network analyzes these features to predict the most likely transcription based on grammar and context.
- The recognized text is generated passed to the next stage of the pipeline.

## Large language model component 

Large Language Models (LLMs) are designed for natural language understanding, and in this application, they are used for question-answering.

The text transcription from the previous part of the pipeline is used as input to the neural model. During initialization, the application assigns a predefined persona to guide the tone and style of responses. By default, the LLM runs asynchronously, streaming tokens as they are generated. The UI updates in real time with each token, which is also passed to the final pipeline stage.

## Text-to-Speech component

This part of the application pipeline uses the Android Text-to-Speech API with some extra functionality to ensure smooth and natural speech output.

In synchronous mode, speech is only generated after the full response from the LLM is received. By default, the application operates in asynchronous mode, where speech synthesis starts as soon as a sufficient portion of the response (such as a half or full sentence) is available. Any additional responses are queued for processing by the Android Text-to-Speech engine.

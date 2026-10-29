---
title: What is Compute Flow
description: Learn about Compute Flow bricks, manifests, and shared interfaces to combine multiple AI models and run them locally on-device.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Combine Compute Flow bricks to connect multiple AI models into a local application.

Compute Flow is an SDK for building AI applications from reusable AI building blocks called *bricks*. Each brick exposes an AI capability through a shared interface for that capability. You connect those interfaces in Python or C++ while the brick handles model-specific inference.

A *brick type* defines an input and output contract. A *brick variant* implements that contract using a particular model family. For example, Parakeet TDT and Moonshine are different speech-to-text variants. Both accept audio and its sample rate, and return text.

In this Learning Path, we'll use three different bricks to build the audio translation application. The first recognises human speech, the second translates speech into text, the third generate audio. Each of these bricks use different models to get to our aims of translating English into French.

The figure below illustrate the three stages of our audio translation application, pointing out the AI models that are used at each stage.

You'll use Python to translate a short English recording into French speech on your Apple Silicon Mac. The application processes the recording through three stages:

```text
English WAV (Input)
    |
    v
Stage 1. Speech-to-text: Parakeet TDT
    | English text
    v
Stage 2. Text translation: Hy-MT2
    | French text
    v
Stage 3. Text-to-speech: Qwen3-TTS
    |
    v
French WAV (Output)
```

Python coordinates the stages: it passes the speech-to-text transcription to the translation brick, then passes the translation to the speech synthesis brick. Compute Flow doesn't automatically assemble this pipeline for you.

## Separate the application from the model

Your pipeline uses these contracts:

| Stage | Brick type | Input | Output |
| --- | --- | --- | --- |
| Audio transcription | `speech-to-text (stt)` | `raw_wav` and `sample_rate` | `text` |
| Translate text | `lm_text` | `text_prompt` | `text` |
| Synthesize speech | `text-to-speech (tts)` | `text_prompt` | `left_channel`, `right_channel`, and `sample_rate` |

### Understand the model manifest

A *model package* contains the weights and supporting assets that a brick needs. A *model manifest* is a JSON configuration file in that package. It tells Compute Flow which brick implementation to use and how to load and run the models.

The manifest describes model filenames, inference runtimes, model-specific tensor formats, and supporting assets, such as tokenizers. It also provides configuration values and constants needed by the brick. The weights live in separate files referenced by the manifest.

For example, the Parakeet package includes `parakeet_tdt_0_6b_v3_manifest.json`. Your Python application reads this file with `cf.load_manifest()`, selects the implementation with `cf.load_brick()`, and prepares the models with `brick.setup()`. This keeps model-specific file paths and runtime configuration out of your application code.

## Prepare once, then run locally

To discover and install the required Compute Flow Bricks, alongside with the selected AI models for our audio-to-audio translation pipeline, we will use Compute Flow Brick Manager.
The Brick Manager is responsible for installing the bricks type and brick variant based on users' selected AI model, and builds the user's developed application for the selected runtime platforms.

Setup needs network access to download dependencies and model packages. After setup, the example reads the installed assets and performs inference on your Mac. It writes a WAV file locally and doesn't call a hosted inference service. You don't need a microphone because the input recording is included in a model package.

## What you've learned

Compute Flow provides reusable AI building blocks that you can combine together to build AI application to deploy locally on your device. Compute Flows Bricks allow users to focus on the AI models actions, inputs and outputs, rather than the AI models inference, easing out the combination and replacement of different AI models.

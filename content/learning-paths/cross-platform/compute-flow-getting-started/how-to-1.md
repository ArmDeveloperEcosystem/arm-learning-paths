---
title: Understand the Compute Flow SDK
description: Learn about Compute Flow bricks, manifests, and shared interfaces to combine multiple AI models and run them locally on-device.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compute Flow bricks

Compute Flow is an SDK for building AI applications from reusable AI building blocks called bricks. Each brick exposes an AI capability through a shared interface. You connect the interfaces in Python or C++, while the brick handles model-specific inference.

A brick type defines an input and output contract. A brick variant implements that contract using a particular model family. For example, Parakeet TDT and Moonshine are different speech-to-text variants. Both accept audio and its sample rate, and return text.

You'll use three different bricks to build an audio translation application in Python or C++ on your Arm-based device. The first recognizes human speech, the second translates speech into text, and the third generates audio. Each brick uses different models to accomplish the goal of translating English into French.

The application processes a short English recording into French speech through three stages:

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

Your application coordinates the stages. It passes the speech-to-text transcription to the translation brick, then passes the translation to the speech synthesis brick. Compute Flow doesn't automatically assemble this pipeline for you.

## Separate the application from the model

You'll use the following contracts:

| Stage | Brick type | Input | Output |
| --- | --- | --- | --- |
| Audio transcription | `speech-to-text (stt)` | `raw_wav` and `sample_rate` | `text` |
| Text translation | `lm_text` | `text_prompt` | `text` |
| Speech synthesis | `text-to-speech (tts)` | `text_prompt` | `left_channel`, `right_channel`, and `sample_rate` |

### Understand the model manifest

A model package contains the weights and supporting assets that a brick needs. A model manifest is a JSON configuration file in that package. It tells Compute Flow which brick implementation to use and how to load and run the models.

The manifest describes model filenames, inference runtimes, and model-specific tensor formats. It also describes supporting assets such as tokenizers. The manifest provides configuration values and constants that the brick needs. The weights live in separate files that the manifest references.

For example, the Parakeet package includes `parakeet_tdt_0_6b_v3_manifest.json`. The application reads this file with `cf.load_manifest()`. It selects the implementation with `cf.load_brick()`, and prepares the models with `brick.setup()`. This keeps model-specific file paths and runtime configuration out of your application code.

## Compute Flow Brick Manager

To discover and install the required Compute Flow bricks, you'll use Compute Flow Brick Manager alongside the selected AI models.

The Brick Manager is responsible for installing the brick type and variant based on the selected AI model. It builds the developed application for the selected runtime platforms.

To complete setup, you need network access to download dependencies and model packages. After setup, the application reads the installed assets and performs inference on your device. It writes a `.wav` file locally and doesn't call a hosted inference service. You don't need a microphone because the input recording is included in a model package.

## What you've learned and what's next

You've learned that Compute Flow provides reusable AI building blocks that you can combine to build locally deployable AI applications. You've also learned about Compute Flows Brick Manager.

Next, you'll build and run the example audio translation application with Compute Flow. 

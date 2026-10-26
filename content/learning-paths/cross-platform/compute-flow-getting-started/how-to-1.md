---
title: Understand Compute Flow
description: Understand how you can combine local AI models through Compute Flow bricks, manifests, and shared interfaces.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect models into a local application

Compute Flow is an SDK for building AI applications from reusable components called *bricks*. Each brick exposes an AI capability through a shared interface for that capability. You connect those interfaces in Python or C++ while the brick handles model-specific inference. Compute Flow brings together runtimes such as LiteRT, ONNX Runtime, ExecuTorch, and llama.cpp for Arm devices.

We'll use the example of an application that translates speech needs several models. One recognizes speech, another translates text, and a third generates audio. These models can use different inference runtimes, tensor formats, tokenizers, and configuration files. Connecting them directly means learning each runtime's API and writing code for each model. Replacing a model can mean rewriting that integration.

You'll use Python to translate a short English recording into French speech on your Apple Silicon Mac. The application processes the recording through three stages:

```text
English WAV
    |
    v
Speech-to-text: Moonshine Base English (FP32)
    | English text
    v
Text translation: Hy-MT2
    | French text
    v
Text-to-speech: Qwen3-TTS
    |
    v
French WAV
```

Python coordinates the stages: it passes the transcription to the translation brick, then passes the translation to the speech synthesis brick. Compute Flow doesn't automatically assemble this pipeline for you.

## Separate the application from the model

A *brick type* defines an input and output contract. A *brick variant* implements that contract using a particular model family. For example, Parakeet TDT and Moonshine are different speech-to-text variants. Both accept audio and its sample rate, and return text.

Your pipeline uses these contracts:

| Stage | Brick type | Input | Output |
| --- | --- | --- | --- |
| Recognize speech | `stt` | `raw_wav` and `sample_rate` | `text` |
| Translate text | `lm_text` | `text_prompt` | `text` |
| Synthesize speech | `tts` | `text_prompt` | `left_channel`, `right_channel`, and `sample_rate` |

### Understand the model manifest

A *model package* contains the weights and supporting assets that a brick needs. A *model manifest* is a JSON configuration file in that package. It tells Compute Flow which brick implementation to use and how to load and run the models.

The manifest describes model filenames, inference runtimes, model-specific tensor formats, and supporting assets, such as tokenizers. It also provides configuration values and constants needed by the brick. The weights live in separate files referenced by the manifest.

For example, the Moonshine Base English package includes `moonshine_manifest_base_en.json`. Your Python application reads this file with `cf.load_manifest()`, selects the implementation with `cf.load_brick()`, and prepares the models with `brick.setup()`. This keeps model-specific file paths and runtime configuration out of your application code.

## Use versioned brick APIs

From Python or C++, you use a brick's versioned input/output contract and shared execution methods such as `setup()`, `run()`, and `reset_states()`. Parakeet and Moonshine both implement `stt.v1`, so your script keeps the same input and output handling when switching between them. Compute Flow's compatibility policy requires newer releases to support bricks using earlier API versions.

For details, see the [Brick API guide](https://github.com/ARM-software/ComputeFlow/blob/main/docs/design/brick_api.md), [Brick Runtime Interface V1](https://github.com/ARM-software/ComputeFlow/blob/main/docs/design/brick_runtime_interface_v1.md), and [documentation README](https://github.com/ARM-software/ComputeFlow/blob/main/docs/README.md). These links use the public repository URL placeholder.

## Prepare once, then run locally

*Brick Manager*, the `compute-flow` command, discovers bricks, installs their source and model packages, and builds the native libraries and Python bindings. You'll update its registry, install the three models, and build for your Mac with `compute-flow build native`.

Setup needs network access to download dependencies and model packages. After setup, the example reads the installed assets and performs inference on your Mac. It writes a WAV file locally and doesn't call a hosted inference service. You don't need a microphone because the input recording is included in a model package.

## What you've learned

Compute Flow separates your application from model-specific inference through versioned brick APIs and manifests. Brick Manager prepares the implementations and model assets, while your Python code connects their inputs and outputs. Next, you'll build and run the speech translation pipeline on your Mac.

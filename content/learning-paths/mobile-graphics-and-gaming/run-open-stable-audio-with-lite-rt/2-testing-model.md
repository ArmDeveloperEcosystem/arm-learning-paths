---
title: Test Open Stable Audio model
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Stable Audio Open Model

Stable Audio Open is an open-source model optimized for generating short audio samples, sound effects, and production elements using text prompts.

[Log in](https://huggingface.co/login) to HuggingFace and navigate to the model landing page:

```bash
https://huggingface.co/stabilityai/stable-audio-open-small
```

You may need to fill out a form with your contact information to use the model:

![Agree to share contact information#center](./contact-information.png)

Download and copy the configuration file `model_config.json` and the model itself, `model.ckpt`, to your workspace directory, and verify they exist by running the command:

```bash
ls $WORKSPACE/model_config.json $WORKSPACE/model.ckpt
```

## Test the model

To showcase its capabilities, you can use a website that is set up to experiment with the model:

```bash
https://stableaudio.com/
```

Use the UI to enter a prompt. Here are a few ways to structure a text prompt for your audio file.
A prompt can include:
* music genre and subgenre
* musical elements (texture, rhythm and articulation)
* musical atmosphere (mood and emotion)
* tempo using beats per minute (BPM)

The order of prompt parameters matters, for more information check [Prompt structure user guide](https://stableaudio.com/user-guide/prompt-structure)

Training and inference code for audio generation models can be accessed through the [Stable Sudio Tools](https://github.com/Stability-AI/stable-audio-tools) repository.

Now that you have downloaded and tried out the model, continue to the next section to convert the model to LiteRT.


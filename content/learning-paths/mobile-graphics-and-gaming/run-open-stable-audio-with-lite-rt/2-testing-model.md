---
title: Test Open Stable Audio model
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Stable Audio Open Model 

Stable Audio Open is an open-source model optimized for generating short audio samples, sound effects, and production elements using text prompts.

Download the model weights from [HuggingFace](https://huggingface.co/stabilityai/stable-audio-open-1.0/tree/main)

TODO - point above to new location on huggingFace stable-audio-open-2.0 when available. (https://huggingface.co/stabilityai/stable-audio-open-small/tree/main)

{{% notice Access to HuggingFace models %}}
You may need to sign up or [log in](https://huggingface.co/login) to HuggingFace first
{{% /notice %}}

Download and copy the model files to your workspace directory, we will set a variable for easier access to these in the next steps:
```bash
mkdir $WORKSPACE/models

export LITERT_MODELS_PATH=$WORKSPACE/models
```

## Test the model output

You can try out the model [here](https://stableaudio.com/)

## Text prompt engineering

Here are a few ways to structure a text prompt for your audio file.
A prompt can include:
* music genre and subgenre
* musical elements (texture, rhythm and articulation)
* musical atmosphere (mood and emotion)
* tempo using beats per minute (BPM)

The order of prompt parameters matters, for more information check [Prompt structure user guide](https://stableaudio.com/user-guide/prompt-structure)

Now that you're happy with the quality and specifics of the model, you can convert it to TFLite and ONNX format in the next step.


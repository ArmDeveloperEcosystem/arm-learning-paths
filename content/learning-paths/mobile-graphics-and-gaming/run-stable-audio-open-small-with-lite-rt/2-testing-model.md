---
title: Download and test the model
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the model

Stable Audio Open Small is an open-source model optimized for generating short audio samples, sound effects, and production elements using text prompts.

[Log in](https://huggingface.co/login) to HuggingFace and navigate to the model landing page:

```bash
https://huggingface.co/stabilityai/stable-audio-open-small/tree/main
```

You may need to fill out a form with your contact information to use the model:

![Agree to share contact information#center](./contact-information.png)

Download and copy the configuration file `model_config.json` and the model itself, `model.ckpt`, to your workspace directory, and verify they exist by running the command:

```bash
ls -lha $WORKSPACE/model_config.json $WORKSPACE/model.ckpt
```

You can learn more about [stable-audio-open-small on Hugging Face](https://huggingface.co/stabilityai/stable-audio-open-small).

### Good prompting practices

A good prompt for the Stable Audio Open Small model can include the following elements:

* Music genre and subgenre.
* Musical elements (texture, rhythm and articulation).
* Musical atmosphere (mood and emotion).
* Tempo, using beats per minute (BPM).

The order of prompt parameters matters. For more information, see the [Prompt structure user guide](https://stableaudio.com/user-guide/prompt-structure).

You can explore training and inference code for audio generation models in the [Stable Audio Tools repository](https://github.com/Stability-AI/stable-audio-tools).

Now that you've downloaded the model, you're ready to convert it to LiteRT format in the next step.


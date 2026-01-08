---
title: Download the Stable Audio Open Small model
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## About the Stable Audio Open Small model

Stable Audio Open Small is an open-source model optimized for generating short audio samples, sound effects, and production elements using text prompts. The model consists of three main submodules:
- Conditioners: include a T5-based text encoder for input prompts and a numerical duration encoder. These components encode the inputs into numerical values to be passed to the DiT model.
- Diffusion Transformer (DiT): takes random noise and denoises it through multiple steps to produce structured latent audio, guided by conditioner embeddings.
- AutoEncoder: compresses input waveforms into a manageable sequence length for processing by the DiT model. At the end of the denoising step, it decompresses the result into a waveform.

You can learn more about [stable-audio-open-small on Hugging Face](https://huggingface.co/stabilityai/stable-audio-open-small).

## Download model files

[Log in](https://huggingface.co/login) to Hugging Face and navigate to the model landing page:

```url
https://huggingface.co/stabilityai/stable-audio-open-small/tree/main
```

You will need to fill out a form with your contact information to access the model.

Download the following files:
- `model_config.json` (configuration file)
- `model.ckpt` (model checkpoint)

Copy both files to your workspace directory.

Verify the files exist:

```bash
ls $WORKSPACE/model_config.json 
ls $WORKSPACE/model.ckpt
```


## Understand prompt structure

A good prompt for Stable Audio Open Small includes:

- Music genre and subgenre
- Musical elements (texture, rhythm, articulation)
- Musical atmosphere (mood and emotion)
- Tempo in beats per minute (BPM)

The order of prompt parameters matters. For example:

```text
warm arpeggios on house beats 120BPM with drums effect
```

For more information, see the [Prompt structure user guide](https://stableaudio.com/user-guide/prompt-structure).

You can explore additional training and inference code in the [Stable Audio Tools repository](https://github.com/Stability-AI/stable-audio-tools).

## What you've accomplished and what's next

You've downloaded the Stable Audio Open Small model files and learned how to structure effective prompts. In the next section, you'll convert these model files to ExecuTorch format for on-device deployment.

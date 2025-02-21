---
# User change
title: "Setup the Whisper Model"

weight: 2

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

This Learning Path demonstrates how to run the whisper-large-v3-turbo model as an application that takes the audio input and computes out the text transcript of it. The instructions in this Learning Path have been designed for Arm servers running Ubuntu 24.04 LTS. You need an Arm server instance with 32 cores, atleast 8GB of RAM and 32GB disk to run this example. The instructions have been tested on a AWS c8g.8xlarge instance.

## Overview

OpenAI Whisper is an open-source Automatic Speech Recognition (ASR) model trained on the multilingual and multitask data, which enables the transcript generation in multiple languages and translations from different languages to English. We will explore the foundational aspects of speech-to-text transcription applications, specifically focusing on running OpenAI’s Whisper on an Arm CPU. We will discuss the implementation and performance considerations required to efficiently deploy Whisper using Hugging Face Transformers framework.

## Install dependencies

Install the following packages on your Arm based server instance:

```bash
sudo apt update
sudo apt install python3-pip python3-venv ffmpeg -y
```

## Install Python Dependencies

Create a Python virtual environment:

```bash
python3 -m venv whisper-env
```

Activate the virtual environment:

```bash
source whisper-env/bin/activate
```

Install the required libraries using pip:

```python3
pip install torch transformers accelerate
```

## Download the sample audio file

Download a sample audio file, which is about 33sec audio in .wav format or use your own audio file:
```bash
    wget https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0010_8k.wav
```

## Create a python script for audio to text transcription

Create a python file:

```bash
    vim whisper-application.py
```

Write the following code in the `whisper-application.py` file:
```python
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import time

# Set the device to CPU and specify the torch data type
device = "cpu"
torch_dtype = torch.float32

# Specify the model name
model_id = "openai/whisper-large-v3-turbo"

# Load the model with specified configurations
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)

# Move the model to the specified device
model.to(device)

# Load the processor for the model
processor = AutoProcessor.from_pretrained(model_id)

# Create a pipeline for automatic speech recognition
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
    return_timestamps=True
)

# Record the start time of the inference
start_time = time.time()

# Perform speech recognition on the audio file
result = pipe("OSR_us_000_0010_8k.wav")

# Record the end time of the inference
end_time = time.time()

# Print the transcribed text
print(f'\n{result["text"]}\n')

# Calculate and print the duration of the inference
duration = end_time - start_time
hours = duration // 3600
minutes = (duration - (hours * 3600)) // 60
seconds = (duration - ((hours * 3600) + (minutes * 60)))
msg = f'\nInferencing elapsed time: {seconds:4.2f} seconds\n'

print(msg)

```
---
# User change
title: "Setup the Whisper Model"

weight: 2

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

This Learning Path demonstrates how to run the [whisper-large-v3-turbo model](https://huggingface.co/openai/whisper-large-v3-turbo) as an application that takes an audio input and computes the text transcript of it. The instructions in this Learning Path have been designed for Arm servers running Ubuntu 24.04 LTS. You need an Arm server instance with 32 cores, atleast 8GB of RAM and 32GB disk to run this example. The instructions have been tested on a AWS Graviton4 `c8g.8xlarge` instance.

## Overview

OpenAI Whisper is an open-source Automatic Speech Recognition (ASR) model trained on the multilingual and multitask data, which enables the transcript generation in multiple languages and translations from different languages to English. You will learn about the foundational aspects of speech-to-text transcription applications, specifically focusing on running OpenAI’s Whisper on an Arm CPU. Lastly, you will explore the implementation and performance considerations required to efficiently deploy Whisper using Hugging Face Transformers framework.

### Speech-to-text ML applications

Speech-to-text (STT) transcription applications transform spoken language into written text, enabling voice-driven interfaces, accessibility tools, and real-time communication services. Audio is first cleaned and converted into a format suitable for processing, then passed through a deep learning model trained to recognize speech patterns. Advanced language models help refine the output, improving accuracy by predicting likely word sequences based on context. Whether running on cloud servers, STT applications must balance accuracy, latency, and computational efficiency to meet the needs of diverse use cases.

## Install dependencies

Install the following packages on your Arm based server instance:

```bash
sudo apt update
sudo apt install python3-pip python3-venv ffmpeg wget -y
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

Download a sample audio file, which is about 33 second audio in .wav format. You can use any .wav sound file if you'd like to try some other examples.
```bash
wget https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0010_8k.wav
```

## Create a python script for audio to text transcription

You will use the Hugging Face `transformers` framework to help process the audio. It contains classes that configures the model, and prepares it for inference. `pipeline` is an end-to-end function for NLP tasks. In the code below, it's configured to do pre- and post-processing of the sample in this example, as well as running the actual inference.

Using a file editor of your choice, create a python file named `whisper-application.py` with the content shown below:

```python { file_name="whisper-application.py" }
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

Enable verbose mode for the output and run the script:

```bash
export DNNL_VERBOSE=1
python3 whisper-application.py
```

You should see output similar to the image below with a log output, transcript of the audio and the `Inference elapsed time`.

![frontend](whisper_output_no_flags.png)


You've now run the Whisper model successfully on your Arm-based CPU. Continue to the next section to configure flags that can increase the performance your running model.

---
# User change
title: "Set up an LLM based Vision Chatbot"

weight: 3

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

This Learning Path demonstrates how to build and deploy a vision chatbot using open-source large language models (LLMs) optimized for Arm architecture. The vision chatbot can take both images and text prompts as input, processes them, and generates a text response using the image as context. The instructions in this Learning Path are designed for Arm servers running Ubuntu 24.04 LTS. You will need an Arm server instance with at least 32 cores to run this example. These instructions have been tested on a GCP `c4a-standard-64` instance.

## Overview

In this Learning Path, you will learn how to run a vision chatbot LLM inference using PyTorch and Hugging Face Transformers efficiently on Arm CPUs. You will learn how to perform LLM inference by feeding both text and image inputs, which are then processed to generate a text response.

## Install dependencies

Install the following packages on your Arm based server instance:

```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

## Create a file with your Python dependencies

Using your preferred text editor, add the following python dependencies to your `requirements.txt` file:

```python
streamlit
numpy
sentencepiece
pillow
flask
transformers
huggingface_hub
```

## Install Python Dependencies

Now create a Python virtual environment and install the dependencies.

Create a virtual environment:
```bash
python3 -m venv llama-vision
```

Activate the virtual environment:
```bash
source llama-vision/bin/activate
```

Install the required libraries using pip:
```bash
 pip install -r requirements.txt
```

## Install PyTorch

Install the `PyTorch` package, which includes the Kleidi AI optimizations from the nightly build, using the following command:

```bash
pip install torch==2.7.0.dev20250307 --extra-index-url https://download.pytorch.org/whl/nightly/cpu/
```

{{% notice Note %}}

If the specified PyTorch version fails to install, try installing any PyTorch nightly build from [PyTorch Nightly Builds](https://download.pytorch.org/whl/nightly/cpu/) released after version 2.7.0.dev20250307.
{{% /notice %}}

## Install Torch AO

Clone the Torch AO repository:
```bash
    git clone https://github.com/pytorch/ao.git
    cd ao
```

Checkout the required branch:
```bash
    git checkout 24c966cb8931507ef389715bc5f19a11c28b0484
```

Install Torch AO:
```bash
    python setup.py install
    cd ..
```

## Hugging Face Cli Login

To use the [Llama 3.2 11B Vision Model](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) from Hugging Face, you need to request access or accept the terms. You need to log in to Hugging Face using a token.
```bash
    huggingface-cli login
```
Enter your Hugging Face token. You can generate a token from [Hugging Face Hub](https://huggingface.co/) by clicking your profile on the top right corner and selecting **Access Tokens**. 

You must also visit the Hugging Face link printed in the login output and accept the terms by clicking the **Agree and access repository** button or filling out the request-for-access form, depending on the model.

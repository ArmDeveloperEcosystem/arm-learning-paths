---
title: Run a Large Language model(LLM) on Arm servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this learning path are for any Arm server running Ubuntu 22.04 LTS.

To start, you will need to install [PyTorch](/install-guides/pytorch) on your Arm machine. 
PyTorch is a widely used machine learning framework for Python. You will use PyTorch to deploy a Natural Language Processing (NLP) model on your Arm machine.

## Overview

[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like NLP, audio and computer vision. Hugging Face also has a huge collection of NLP models for tasks like translation, sentiment analysis, summarization and text generation.

In this learning path, you will download a popular [RoBERTa sentiment analysis](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) NLP model from Hugging Face and deploy it using PyTorch on your Arm machine. Sentiment analysis is a type of NLP algorithm used to identify and classify the emotional tone of a piece of text. This model has been trained with over 124 million tweets. 

## Install dependencies 

Before you download and build llama.cpp on your Arm server, install the following packages:

```bash
sudo apt update
sudo apt install make cmake
```

You will also need to install `gcc` on your machine:

```bash
sudo apt install gcc g++ -y
sudo apt install build-essential -y
```

## Download and build llama.cpp

Clone the source repository for llama.cpp:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

Run make to build:

```bash
cd llama.cpp
make
```

Check that llama.cpp has built correctly

```bash
./main -h
```

You should see the help options from llama.cpp


## Install Hugging Face Hub
[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like NLP, audio and computer vision.

The `huggingface_hub` library provides APIs and tools that let you easily download and fine-tune pre-trained models. You will use `huggingface-cli` to download the [Llama-2-7B model](https://huggingface.co/TheBloke/Llama-2-7B-GGUF) from Hugging Face.

Install the `huggingface_hub` python libraru using `pip` and add it to your `PATH`:

```bash
sudo apt install python3-pip
pip3 install huggingface-hub>=0.17.1
export PATH=${PATH}:/home/ubuntu/.local/bin/
```
You can now download the model using the huggingface cli:

```bash
huggingface-cli download TheBloke/Llama-2-7b-Chat-GGUF llama-2-7b-chat.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

## Run the Llama-2-7B LLM model 

```bash
./main  -m llama-2-7b-chat.Q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -i -ins
```

You have successfully run a LLM chatbot, all on your Arm AArch64 CPU on your Arm server. You can continue experimenting and trying out the model with different prompts.

Now that you have run the model, let's look at the timing parameters that are printed from the execution of the model on your Arm CPU. 





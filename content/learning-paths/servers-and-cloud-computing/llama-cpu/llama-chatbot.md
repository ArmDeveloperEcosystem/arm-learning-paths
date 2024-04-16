---
title: Run a Large Language model(LLM) chatbot on Arm servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this learning path are for any Arm server running Ubuntu 22.04 LTS.

To start, you will need to install [PyTorch](/install-guides/pytorch) on your Arm machine. 
PyTorch is a widely used machine learning framework for Python. You will use PyTorch to deploy a Natural Language Processing (NLP) model on your Arm machine.

## Overview

Arm CPUs have been widely used in traditional ML and AI use cases. In this learning path, you will learn how to run generative AI inference based use cases like a LLM chatbot on Arm based CPUs. You will do this by deploying the [Llama-2-7B-Chat model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF) on your Arm based CPU using `llama.cpp`. 

[llama.cpp](https://github.com/ggerganov/llama.cpp) is an open-source C/C++ project developed by Georgi Gerganov that enabl
es efficient LLM inference on a variety of hardware both locally and in the cloud. 

## About the Llama 2 model
The [Llama-2-7B-Chat model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF) from Meta is from the `Llama 2` model family and is free to use for research and commercial use.

Llama 2 models can perform general natural language processing (NLP) tasks like text generation. You can access the base foundation Llama 2 model or select the specalised chat Llama 2 version that is already fine-tuned for back-and-forth dialogue. In this learning path you will run the specialized chat model. 

Traditionally, the training and inference of LLMs has been done on GPUs using full precision 32-bit (FP32) or half precision 16-bit (FP16) data type formats for the model parameter and weights. Recently, a new binary model format called GGUF was introduced by the `llama.cpp` team. This new GGUF model format uses compression and quantization techniques that remove the dependency on using FP32 and FP16 data type formats. For example, GGUF supports quantization where model weights that are generally stored as FP16 data types are scaled down to 4-bit integers. This significantly reduces the need for computational resources and the amount of RAM required. These advancements made in the model format and the data types used make Arm CPUs a great fit for running LLM inferences.   
 
[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like NLP, audio and computer vision. Hugging Face also has a huge collection of NLP models for tasks like translation, sentiment analysis, summarization and text generation.

In this learning path, you will download a popular [RoBERTa sentiment analysis](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) NLP model from Hugging Face and deploy it using PyTorch on your Arm machine. Sentiment analysis is a type of NLP algorithm used to identify and classify the emotional tone of a piece of text. This model has been trained with over 124 million tweets. 

## Install dependencies 

Before you download and build `llama.cpp` on your Arm server instance, install the following packages:

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

You are now ready to start building `llama.cpp`. 

Clone the source repository for llama.cpp:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

Run make to build it:

```bash
cd llama.cpp
make
```

Check that `llama.cpp` has built correctly by running the help command:

```bash
./main -h
```

If `llama.cpp` has built correctly on your machine, you should see the help options being displayed. A snippet of the output is shown below:

```output
usage: ./main [options]

options:
  -h, --help            show this help message and exit
  --version             show version and build info
  -i, --interactive     run in interactive mode
  --interactive-first   run in interactive mode and wait for input right away
  -ins, --instruct      run in instruction mode (use with Alpaca models)
  -cml, --chatml        run in chatml mode (use with ChatML-compatible models)
  --multiline-input     allows you to write or paste multiple lines without ending each in '\'
  -r PROMPT, --reverse-prompt PROMPT
                        halt generation at PROMPT, return control in interactive mode
                        (can be specified more than once for multiple prompts).
  --color               colorise output to distinguish prompt and user input from generations
  -s SEED, --seed SEED  RNG seed (default: -1, use random seed for < 0)
  -t N, --threads N     number of threads to use during generation (default: 4)
```


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





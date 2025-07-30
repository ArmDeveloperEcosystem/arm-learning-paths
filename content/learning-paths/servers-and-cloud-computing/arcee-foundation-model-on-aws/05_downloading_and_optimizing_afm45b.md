---
title: Download and optimize the AFM-4.5B model
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you’ll download the [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) model from Hugging Face, convert it to the GGUF format for compatibility with `llama.cpp`, and generate quantized versions to optimize memory usage and improve inference speed.

**Note: if you want to skip the model optimization process, [GGUF](https://huggingface.co/arcee-ai/AFM-4.5B-GGUF) versions are available.**

Make sure to activate your virtual environment before running any commands. The instructions below walk you through downloading and preparing the model for efficient use on AWS Graviton4.

## Signing up to Hugging Face

In order to download AFM-4.5B, you will need:
- a Hugging Face account: you can sign up at [https://huggingface.co](https://huggingface.co)
- a read-only Hugging Face token: once logged in, you can create one at [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens). Don't forget to store it, as you will only be able to view it once.
- to accept the terms of AFM-4.5B at [https://huggingface.co/arcee-ai/AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B)

## Install the Hugging Face libraries

```bash
pip install huggingface_hub hf_xet
```

This command installs:

- `huggingface_hub`: Python client for downloading models and datasets
- `hf_xet`: Git extension for fetching large model files stored on Hugging Face

These tools include the `hf` command-line interface you'll use next.

## Login to the Hugging Face Hub

```bash
hf auth login

    _|    _|  _|    _|    _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|_|_|_|    _|_|      _|_|_|  _|_|_|_|
    _|    _|  _|    _|  _|        _|          _|    _|_|    _|  _|            _|        _|    _|  _|        _|
    _|_|_|_|  _|    _|  _|  _|_|  _|  _|_|    _|    _|  _|  _|  _|  _|_|      _|_|_|    _|_|_|_|  _|        _|_|_|
    _|    _|  _|    _|  _|    _|  _|    _|    _|    _|    _|_|  _|    _|      _|        _|    _|  _|        _|
    _|    _|    _|_|      _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|        _|    _|    _|_|_|  _|_|_|_|

    To login, `huggingface_hub` requires a token generated from https://huggingface.co/settings/tokens .
Enter your token (input will not be visible):
```

Please enter the token you created above, and answer 'n' to "Add token as git credential? (Y/n)".

## Download the AFM-4.5B model

```bash
hf download arcee-ai/afm-4.5B --local-dir models/afm-4-5b
```

This command downloads the model to the `models/afm-4-5b` directory:
- `arcee-ai/afm-4.5B` is the Hugging Face model identifier. 
- The download includes the model weights, configuration files, and tokenizer data.
- This is a 4.5 billion parameter model, so the download can take several minutes depending on your internet connection.

## Convert to GGUF format

```bash
python3 convert_hf_to_gguf.py models/afm-4-5b
deactivate
```

This command converts the downloaded Hugging Face model to GGUF (GGML Universal Format):
- `convert_hf_to_gguf.py` is a conversion script that comes with Llama.cpp.
- `models/afm-4-5b` is the input directory containing the Hugging Face model files.
- The script reads the model architecture, weights, and configuration from the Hugging Face format.
- It outputs a single `afm-4-5B-F16.gguf` ~15GB file in the same `models/afm-4-5b/` directory.
- GGUF is the native format for Llama.cpp, optimized for efficient loading and inference.

Next, deactivate the Python virtual environment as future commands won't require it.

## Create Q4_0 Quantized Version

```bash
bin/llama-quantize models/afm-4-5b/afm-4-5B-F16.gguf models/afm-4-5b/afm-4-5B-Q4_0.gguf Q4_0
```

This command creates a 4-bit quantized version of the model:
- `llama-quantize` is the quantization tool from Llama.cpp.
- `afm-4-5B-F16.gguf` is the input GGUF model file in 16-bit precision. 
- `Q4_0` applies zero-point 4-bit quantization.
- This reduces the model size by approximately 45% (from ~15GB to ~8GB).
- The quantized model will use less memory and run faster, though with a small reduction in accuracy.
- The output file will be `afm-4-5B-Q4_0.gguf`.

## Arm optimization 

Arm has contributed optimized kernels for Q4_0 that use Neoverse V2 instruction sets. These low-level routines accelerate math operations, delivering strong performance on Graviton4.

These instruction sets allow Llama.cpp to run quantized operations significantly faster than generic implementations, making Arm processors a competitive choice for inference workloads.

## Create a Q8_0 quantized version

```bash
bin/llama-quantize models/afm-4-5b/afm-4-5B-F16.gguf models/afm-4-5b/afm-4-5B-Q8_0.gguf Q8_0
```

This command creates an 8-bit quantized version of the model:
- `Q8_0` specifies 8-bit quantization with zero-point compression.
- This reduces the model size by approximately 70% (from ~15GB to ~4.4GB).
- The 8-bit version provides a better balance between memory usage and accuracy than 4-bit quantization.
- The output file is named `afm-4-5B-Q8_0.gguf`.
- Commonly used in production scenarios where memory resources are available.
  
## Arm optimization

Similar to Q4_0, Arm has contributed optimized kernels for Q8_0 quantization that take advantage of Neoverse V2 instruction sets. These optimizations provide excellent performance for 8-bit operations while maintaining higher accuracy compared to 4-bit quantization.

## Model files ready for inference

After completing these steps, you'll have three versions of the AFM-4.5B model in `models/afm-4-5b`:
- `afm-4-5B-F16.gguf` - The original full-precision model (~15GB)
- `afm-4-5B-Q4_0.gguf` - 4-bit quantized version (~4.4GB) for memory-constrained environments
- `afm-4-5B-Q8_0.gguf` - 8-bit quantized version (~8GB) for balanced performance and memory usage

These models are now ready to be used with the `llama.cpp` inference engine for text generation and other language model tasks.

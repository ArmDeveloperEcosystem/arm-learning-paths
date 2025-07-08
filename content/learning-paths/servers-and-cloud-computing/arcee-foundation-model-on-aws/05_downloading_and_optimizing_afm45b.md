---
title: Downloading and optimizing AFM-4.5B
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you'll download the AFM-4.5B model from Hugging Face, convert it to the GGUF format for use with Llama.cpp, and create quantized versions to optimize memory usage and inference speed.

The first release of the [Arcee Foundation Model](https://www.arcee.ai/blog/announcing-the-arcee-foundation-model-family) family, [AFM-4.5B](https://www.arcee.ai/blog/deep-dive-afm-4-5b-the-first-arcee-foundational-model) is a 4.5-billion-parameter frontier model that delivers excellent accuracy, strict compliance, and very high cost-efficiency. It was trained on almost 7 trillion tokens of clean, rigorously filtered data, and has been tested across a wide range of languages, including Arabic, English, French, German, Hindi, Italian, Korean, Mandarin, Portuguese, Russian, and Spanish

Here are the steps to download and optimize the model for AWS Graviton4. Make sure to run them in the virtual environment you created at the previous step.

## Step 1: Install the Hugging Face libraries

```bash
pip install huggingface_hub hf_xet
```

This command installs the Hugging Face Hub Python library, which provides tools for downloading models and datasets from the Hugging Face platform. The library includes the `huggingface-cli` command-line interface that you can use to download the AFM-4.5B model.

## Step 2: Download the AFM-4.5B Model

```bash
huggingface-cli download arcee-ai/afm-4.5B --local-dir models/afm-4-5b
```

This command downloads the AFM-4.5B model from the Hugging Face Hub:
- `arcee-ai/afm-4.5B` is the model identifier on Hugging Face Hub
- `--local-dir model/afm-4-5b` specifies the local directory where the model files will be stored
- The download includes the model weights, configuration files, and tokenizer data
- This is a 4.5 billion parameter model, so the download may take several minutes depending on your internet connection

## Step 3: Convert to GGUF Format

```bash
python3 convert_hf_to_gguf.py models/afm-4-5b
deactivate
```

The first command converts the downloaded Hugging Face model to the GGUF (GGML Universal Format) format:
- `convert_hf_to_gguf.py` is a conversion script that comes with Llama.cpp
- `models/afm-4-5b` is the input directory containing the Hugging Face model files
- The script reads the model architecture, weights, and configuration from the Hugging Face format
- It outputs a single `afm-4-5B-F16.gguf` ~15GB file in the `models/afm-4-5b/` directory
- GGUF is the native format used by Llama.cpp and provides efficient loading and inference

Next, deactivate the Python virtual environment as future commands won't require it.

## Step 4: Create Q4_0 Quantized Version

```bash
bin/llama-quantize models/afm-4-5b/afm-4-5B-F16.gguf models/afm-4-5b/afm-4-5B-Q4_0.gguf Q4_0
```

This command creates a 4-bit quantized version of the model:
- `llama-quantize` is the quantization tool from Llama.cpp
- `afm-4-5B-F16.gguf` is the input GGUF model file in 16-bit precision 
- `Q4_0` specifies 4-bit quantization with zero-point quantization
- This reduces the model size by approximately 45% (from ~15GB to ~8GB)
- The quantized model will use less memory and run faster, though with a small reduction in accuracy
- The output file will be named `afm-4-5B-Q4_0.gguf`

**ARM Optimization**: ARM has contributed highly optimized kernels for Q4_0 quantization that leverage the Neoverse v2 instruction sets. These low-level math routines accelerate typical deep learning operations, providing significant performance improvements on ARM-based processors like Graviton4.

These instruction sets enable Llama.cpp to perform quantized operations much faster than generic implementations, making ARM processors highly competitive for inference workloads.

## Step 5: Create Q8_0 Quantized Version

```bash
bin/llama-quantize models/afm-4-5b/afm-4-5B-F16.gguf models/afm-4-5b/afm-4-5B-Q8_0.gguf Q8_0
```

This command creates an 8-bit quantized version of the model:
- `Q8_0` specifies 8-bit quantization with zero-point quantization
- This reduces the model size by approximately 70% (from ~15GB to ~4.4GB)
- The 8-bit version provides a better balance between memory usage and accuracy compared to 4-bit
- The output file will be named `afm-4-5B-Q8_0.gguf`
- This version is often preferred for production use when memory constraints allow

**ARM Optimization**: Similar to Q4_0, ARM has contributed optimized kernels for Q8_0 quantization that take advantage of Neoverse v2 instruction sets. These optimizations provide excellent performance for 8-bit operations while maintaining higher accuracy compared to 4-bit quantization.

## What is available now?

After completing these steps, you'll have three versions of the AFM-4.5B model:
- `afm-4-5B-F16.gguf` - The original full-precision model (~15GB)
- `afm-4-5B-Q4_0.gguf` - 4-bit quantized version (~8GB) for memory-constrained environments
- `afm-4-5B-Q8_0.gguf` - 8-bit quantized version (~4.4GB) for balanced performance and memory usage

These models are now ready to be used with the Llama.cpp inference engine for text generation and other language model tasks.
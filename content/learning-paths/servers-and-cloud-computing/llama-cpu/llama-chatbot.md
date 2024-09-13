---
title: Run a Large Language model (LLM) chatbot on Arm servers
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this Learning Path are for any Arm server running Ubuntu 22.04 LTS. You need an Arm server instance with at least four cores and 8GB of RAM to run this example. Configure disk storage up to at least 32 GB. The instructions have been tested on an AWS Graviton3 c7g.16xlarge instance.

## Overview

Arm CPUs are widely used in traditional ML and AI use cases. In this Learning Path, you learn how to run generative AI inference-based use cases like a LLM chatbot on Arm-based CPUs. You do this by deploying the [Llama-3.1-8B model](https://huggingface.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf) on your Arm-based CPU using `llama.cpp`. 

[llama.cpp](https://github.com/ggerganov/llama.cpp) is an open source C/C++ project developed by Georgi Gerganov that enables efficient LLM inference on a variety of hardware - both locally, and in the cloud. 

## About the Llama 3.1 model and GGUF model format

The [Llama-3.1-8B model](https://huggingface.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf) from Meta belongs to the Llama 3.1 model family and is free to use for research and commercial purposes. Before you use the model, visit the Llama [website](https://llama.meta.com/llama-downloads/) and fill in the form to request access.


The [Meta Llama 3.1 collection of models](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md) perform general natural language processing (NLP) tasks such as text generation.
The Llama 3.1 family of models range in size from 8 billion to 405 billion parameters. The greater the number of parameters, the more information the model can store. This directly affects how well the model understands language and the model's general capabilities. LLMs that run efficiently on CPUs typically have lower numbers of parameters. For this example, the 8 billion (8B) model is ideal for retaining quality chatbot capability while also running efficiently on your Arm-based CPU. 

Traditionally, the training and inference of LLMs has been done on GPUs using full-precision 32-bit (FP32) or half-precision 16-bit (FP16) data type formats for the model parameter and weights. Recently, a new binary model format called GGUF was introduced by the `llama.cpp` team. This new GGUF model format uses compression and quantization techniques that remove the dependency on using FP32 and FP16 data type formats. For example, GGUF supports quantization where model weights that are generally stored as FP16 data types are scaled down to 4-bit integers. This significantly reduces the need for computational resources and the amount of RAM required. These advancements made in the model format and the data types used make Arm CPUs a great fit for running LLM inferences.   
 
## Install dependencies 

Install the following packages on your Arm based server instance:

```bash
sudo apt update
sudo apt install make cmake -y
```

You also need to install `gcc` on your machine:

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

By default, `llama.cpp` builds for CPU only on Linux and Windows. You don't need to provide any extra switches to build it for the Arm CPU that you run it on.

Run `make` to build it:

```bash
cd llama.cpp
make GGML_NO_LLAMAFILE=1 -j$(nproc)
```

Check that `llama.cpp` has built correctly by running the help command:

```bash
./llama-cli -h
```

If `llama.cpp` has built correctly on your machine, you will see the help options being displayed. A snippet of the output is shown below:

```output
usage: ./llama-cli [options]

general:

  -h,    --help, --usage          print usage and exit
         --version                show version and build info
  -v,    --verbose                print verbose information
         --verbosity N            set specific verbosity level (default: 0)
         --verbose-prompt         print a verbose prompt before generation (default: false)
         --no-display-prompt      don't print prompt at generation (default: false)
  -co,   --color                  colorise output to distinguish prompt and user input from generations (default: false)
  -s,    --seed SEED              RNG seed (default: -1, use random seed for < 0)
  -t,    --threads N              number of threads to use during generation (default: 4)
  -tb,   --threads-batch N        number of threads to use during batch and prompt processing (default: same as --threads)
  -td,   --threads-draft N        number of threads to use during generation (default: same as --threads)
  -tbd,  --threads-batch-draft N  number of threads to use during batch and prompt processing (default: same as --threads-draft)
         --draft N                number of tokens to draft for speculative decoding (default: 5)
  -ps,   --p-split N              speculative decoding split probability (default: 0.1)
  -lcs,  --lookup-cache-static FNAME
                                  path to static lookup cache to use for lookup decoding (not updated by generation)
  -lcd,  --lookup-cache-dynamic FNAME
                                  path to dynamic lookup cache to use for lookup decoding (updated by generation)
  -c,    --ctx-size N             size of the prompt context (default: 0, 0 = loaded from model)
  -n,    --predict N              number of tokens to predict (default: -1, -1 = infinity, -2 = until context filled)
  -b,    --batch-size N           logical maximum batch size (default: 2048)
```


## Install Hugging Face Hub

There are a few different ways you can download the Meta Llama-3.1 8B model. In this Learning Path, you download the model from Hugging Face.

{{% notice Note %}} Use of Llama 3.1 8B model is governed by the Meta license. Before you proceed to download the model, please visit the Llama [website](https://llama.meta.com/llama-downloads/) and fill in the form. {{% /notice %}}

[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like NLP, audio, and computer vision.

The `huggingface_hub` library provides APIs and tools that let you easily download and fine-tune pre-trained models. You will use `huggingface-cli` to download the [Llama-3.1 8B model](https://huggingface.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf).

Install the required Python packages:

```bash
sudo apt install python-is-python3 python3-pip python3-venv -y
```

Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Your terminal prompt now has the `(venv)` prefix indicating the virtual environment is active. Use this virtual environment for the remaining commands.

Install the `huggingface_hub` python library using `pip`:

```bash
pip install huggingface_hub
```

You can now download the model using the huggingface cli:

```bash
huggingface-cli download cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf dolphin-2.9.4-llama3.1-8b-Q4_0.gguf --local-dir . --local-dir-use-symlinks False
```
Before you proceed and run this model, take a quick look at what `Q4_0` in the model name denotes.

## Quantization format

`Q4_0` in the model name refers to the quantization method the model uses. The goal of quantization is to reduce the size of the model (to reduce the memory space required) and faster (to reduce memory bandwidth bottlenecks transferring large amounts of data from memory to a processor). The primary trade-off to keep in mind when reducing a model's size is maintaining quality of performance. Ideally, a model is quantized to meet size and speed requirements while not having a negative impact on performance. 

This model is `llama3.1-8b-Q4_0.gguf`, so what does each component mean in relation to the quantization level? The main thing to note is the number of bits per parameter, which is denoted by 'Q4' in this case or 4-bit integer. As a result, by only using 4 bits per parameter for 8 billion parameters, the model drops to be 4.7Gb in size.

Here is a quick lookup to the rest of the quantization parts for the Llama-2 model family as it exists today:

| quantization-method | # of bits per parameter | quantization format (does not apply to quantization method 'IQ') | quantization method specifics |
| ------------------- | ----------------------- | ---------------------------------------------------------------- | ------------------ |
| Q, IQ, F, FP        | 2,3,4,5,6,7,8,16,32     | _0, _1, _K                                                       | _XXS, _XS, _S, _M, _L    |

Some examples:

* Q8_0 --> Straightforward quantization method (indicated with _0 or _1), with an 8 bit integer per parameter.
* Q4_K_M --> K-quant method (indicated with _K), with a 4 bit integer per parameter, with the _M quantization mix type used.
* IQ2_XXS --> I-quant method (indicated with _IQ), with the _XXS quantization mix type used.
* F16  --> Using a 16 bit floating point number per parameter (no other quantization method used, only rounding a number if starting from a 32 bit floating point number).

Each quantization method has a unique approach to quantizing parameters. The deeper technical details of different quantization methodologies are outside the scope of this guide. The main takeaway is that selecting the right model quantization is critical to running an LLM effectively on your hardware, and the most impactful quantization decision is the number of bits per parameter. You will need also need to check you have enough system memory before deploying larger models or models with higher precision/quantization. 

In this guide, you will not use any other quantization methods, because Arm has not made kernel optimizations for other quantization types.

## Re-quantize the model weights

To see improvements for Arm optimized kernels, you need to generate a new weights file with rearranged Q4_0 weights. As of [llama.cpp commit 0f1a39f3](https://github.com/ggerganov/llama.cpp/commit/0f1a39f3), Arm has contributed code for three types of GEMV/GEMM kernels corresponding to three processor types:

* AWS Graviton2, where you only have NEON support (you will see less improvement for these GEMV/GEMM kernels),
* AWS Graviton3, where the GEMV/GEMM kernels exploit both SVE 256 and MATMUL INT8 support, and
* AWS Graviton4, where the GEMV/GEMM kernels exploit NEON/SVE 128 and MATMUL_INT8 support

To re-quantize optimally for Graviton3, run

```bash
./llama-quantize --allow-requantize dolphin-2.9.4-llama3.1-8b-Q4_0.gguf dolphin-2.9.4-llama3.1-8b-Q4_0_8_8.gguf Q4_0_8_8
```

This will output a new file, `dolphin-2.9.4-llama3.1-8b-Q4_0_8_8.gguf`, which contains reconfigured weights that allow `llama-cli` to use SVE 256 and MATMUL_INT8 support.

{{% notice Note %}} 
This requantization is optimal only for Graviton3. For Graviton2, requantization should optimally be done in `Q4_0_4_4` format, and for Graviton4, `Q4_0_4_8` is the optimal requantization format. 
{{% /notice %}}

## Compare the pre-quantized Llama-3.1-8B LLM model weights to the optimized weights

First, run the pre-quantized llama-3.1-8b model exactly as the weights were downloaded from huggingface:

```bash
./llama-cli -m dolphin-2.9.4-llama3.1-8b-Q4_0.gguf -p "Building a visually appealing website can be done in ten simple steps:" -n 512 -t 64 
```

This command will use the downloaded model (`-m` flag), with the specified prompt (`-p` flag), and target a 512 token completion (`-n` flag), using 64 threads (`-t` flag).

You will see lots of interesting statistics being printed from llama.cpp about the model and the system, followed by the prompt and completion. The tail of the output from running this model on an AWS Graviton3 c7g.16xlarge instance is shown below:

```output
llm_load_tensors: ggml ctx size =    0.14 MiB
llm_load_tensors:        CPU buffer size =  4437.82 MiB
.......................................................................................
llama_new_context_with_model: n_ctx      = 131072
llama_new_context_with_model: n_batch    = 2048
llama_new_context_with_model: n_ubatch   = 512
llama_new_context_with_model: flash_attn = 0
llama_new_context_with_model: freq_base  = 500000.0
llama_new_context_with_model: freq_scale = 1
llama_kv_cache_init:        CPU KV buffer size = 16384.00 MiB
llama_new_context_with_model: KV self size  = 16384.00 MiB, K (f16): 8192.00 MiB, V (f16): 8192.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.49 MiB
llama_new_context_with_model:        CPU compute buffer size =  8480.01 MiB
llama_new_context_with_model: graph nodes  = 1030
llama_new_context_with_model: graph splits = 1

system_info: n_threads = 64 (n_threads_batch = 64) / 64 | AVX = 0 | AVX_VNNI = 0 | AVX2 = 0 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | AVX512_BF16 = 0 | FMA = 0 | NEON = 1 | SVE = 1 | ARM_FMA = 1 | F16C = 0 | FP16_VA = 1 | RISCV_VECT = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 0 | SSSE3 = 0 | VSX = 0 | MATMUL_INT8 = 1 | LLAMAFILE = 0 |
sampling seed: 4210375779
sampling params:
        repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
        top_k = 40, tfs_z = 1.000, top_p = 0.950, min_p = 0.050, typical_p = 1.000, temp = 0.800
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampler constr:
        logits -> logit-bias -> penalties -> top-k -> tail-free -> typical -> top-p -> min-p -> temp-ext -> softmax -> dist
generate: n_ctx = 131072, n_batch = 2048, n_predict = 512, n_keep = 1


Building a visually appealing website can be done in ten simple steps: Plan, design, wireframe, write content, optimize for SEO, choose the right platform, add interactive elements, test and fix bugs, launch, and finally, maintain. These steps are crucial for creating a user-friendly and effective website that attracts visitors and converts them into customers.
1. Planning the Website
Planning is the first and most crucial stage in building a website. It involves determining your target audience, identifying their needs, and outlining what the website will offer them. The planning process also includes setting goals for the website and figuring out how it will be used. This stage is essential as it will guide the design, content, and functionality of your website.
2. Designing the Website
Once you have a clear plan, you can proceed to design the website. The design stage involves creating a visual representation of your website, including its layout, color scheme, typography, and imagery. A well-designed website is crucial for capturing the attention of your target audience and encouraging them to engage with your content.
3. Creating a Wireframe
A wireframe is a simple, low-fidelity version of your website that outlines its structure and layout. It is a critical stage in the website-building process as it helps you visualize how your website will look and function before you invest in the design and development stages. A wireframe also allows you to gather feedback from stakeholders and refine your design before it goes live.
4. Writing Quality Content
Content is the lifeblood of any website. It is essential to create high-quality, engaging, and informative content that resonates with your target audience. The content should be well-researched, optimized for SEO, and written in a style that is easy to understand. It is also essential to keep your content fresh and up-to-date to keep your audience engaged.
5. Optimizing for SEO
Search Engine Optimization (SEO) is the process of optimizing your website to rank higher in search engine results pages (SERPs). It involves optimizing your website's content, structure, and technical aspects to make it more visible and accessible to search engines. SEO is critical for driving organic traffic to your website and increasing its visibility online.
6. Choosing the Right Platform
Choosing the right platform for your website is essential for its success. There are various website-building platforms available, such as WordPress, Squarespace, and Wix. Each platform has its strengths and weaknesses, and it is essential to choose the one that best suits your needs.
7. Adding Interactive Elements
Interactive elements, such as videos, quizzes, and gam
llama_perf_sampler_print:    sampling time =      41.44 ms /   526 runs   (    0.08 ms per token, 12692.44 tokens per second)
llama_perf_context_print:        load time =    4874.27 ms
llama_perf_context_print: prompt eval time =      87.00 ms /    14 tokens (    6.21 ms per token,   160.92 tokens per second)
llama_perf_context_print:        eval time =   11591.53 ms /   511 runs   (   22.68 ms per token,    44.08 tokens per second)
llama_perf_context_print:       total time =   11782.00 ms /   525 tokens
```

The `system_info` printed from llama.cpp highlights important architectural features present on your hardware that improve the performance of the model execution. In the output shown above from running on an AWS Graviton3 instance, you will see:

  * NEON = 1 This flag indicates support for Arm's Neon technology which is an implementation of the Advanced SIMD instructions
  * ARM_FMA = 1 This flag indicates support for Arm Floating-point Multiply and Accumulate instructions 
  * MATMUL_INT8 = 1 This flag indicates support for Arm int8 matrix multiplication instructions
  * SVE = 1 This flag indicates support for the Arm Scalable Vector Extension


The end of the output shows several model timings:

* load time refers to the time taken to load the model.
* prompt eval time refers to the time taken to process the prompt before generating the new text. In this example, it shows that it evaluated 16 tokens in 1998.79 ms. 
* eval time refers to the time taken to generate the output. Generally anything above 10 tokens per second is faster than what humans can read.

You can compare these timings to the optimized model weights by running:

```bash
./llama-cli -m dolphin-2.9.4-llama3.1-8b-Q4_0_8_8.gguf -p "Building a visually appealing website can be done in ten simple steps:" -n 512 -t 64
```

This is the same command as before, but with the model file swapped out for the re-quantized file.

The timings on this one look like:

```output
llama_perf_sampler_print:    sampling time =      41.13 ms /   526 runs   (    0.08 ms per token, 12789.96 tokens per second)
llama_perf_context_print:        load time =    4846.73 ms
llama_perf_context_print: prompt eval time =      48.22 ms /    14 tokens (    3.44 ms per token,   290.32 tokens per second)
llama_perf_context_print:        eval time =   11233.92 ms /   511 runs   (   21.98 ms per token,    45.49 tokens per second)
llama_perf_context_print:       total time =   11385.65 ms /   525 tokens

```

As you can see, load time improves, but the biggest improvement can be seen in prompt eval times.

You have successfully run a LLM chatbot with Arm optimizations, all running on your Arm AArch64 CPU on your server. You can continue experimenting and trying out the model with different prompts.

